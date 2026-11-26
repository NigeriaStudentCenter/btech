'use strict';

// Builds the candidate's answers or marking report as a PDF.
// Uses app.js globals (state, questions) when a download is requested.
window.mockReport = (() => {
  const LIBRARY = 'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js';
  let loading = null;

  function library() {
    if (window.jspdf) return Promise.resolve(window.jspdf);
    loading ??= new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = LIBRARY;
      script.crossOrigin = 'anonymous';
      script.onload = () => (window.jspdf ? resolve(window.jspdf) : reject(Error('PDF tool missing')));
      script.onerror = () => { loading = null; reject(Error('PDF tool could not load')); };
      document.head.append(script);
    });
    return loading;
  }

  // Standard PDF fonts only cover Western European characters.
  const clean = text => String(text ?? '')
    .replace(/[‘’]/g, "'").replace(/[“”]/g, '"')
    .replace(/[–—]/g, '-').replace(/…/g, '...').replace(/\t/g, '    ')
    .replace(/[^\n\x20-\x7E\xA0-\xFF]/gu, '?');

  const when = ms => ms ? new Date(ms).toLocaleString('en-GB', { dateStyle: 'medium', timeStyle: 'short' }) : '-';

  function answerText(id, answer) {
    if (Array.isArray(answer)) {
      return answer.map((value, row) => 'Row ' + (row + 1) + ': ' + (value.trim() || '(blank)')).join('\n');
    }
    return answer?.trim() || '(No answer)';
  }

  async function build(withMarks) {
    const { jsPDF } = await library();
    const doc = new jsPDF({ unit: 'mm', format: 'a4' });
    const page = { w: 210, h: 297, margin: 18 };
    const width = page.w - page.margin * 2;
    let y = page.margin;

    const room = needed => {
      if (y + needed > page.h - 18) { doc.addPage(); y = page.margin; }
    };
    const text = (value, size = 10, style = 'normal', gap = 1.5) => {
      doc.setFont('helvetica', style);
      doc.setFontSize(size);
      const lineHeight = size * 0.42;
      for (const line of doc.splitTextToSize(clean(value), width)) {
        room(lineHeight);
        doc.text(line, page.margin, y + lineHeight * 0.8);
        y += lineHeight;
      }
      y += gap;
    };
    const rule = () => { room(4); doc.setDrawColor(0); doc.setLineWidth(0.3); doc.line(page.margin, y, page.w - page.margin, y); y += 4; };

    const candidate = state.candidate || {};
    const report = withMarks ? state.report : null;

    // Heading and candidate box, laid out like the paper's front cover.
    text('Pearson BTEC Level 3 Nationals - Computing', 10, 'bold', 0.5);
    text('Unit 2: Fundamentals of Computer Systems (31769H) - June 2024 timed mock', 10, 'normal', 3);
    text(withMarks ? 'Marking report' : 'Candidate answers', 18, 'bold', 3);

    const boxTop = y;
    const half = width / 2;
    const cell = (label, value, x, top) => {
      doc.setFont('helvetica', 'bold'); doc.setFontSize(8);
      doc.text(label, x + 3, top + 5);
      doc.setFont('helvetica', 'normal'); doc.setFontSize(12);
      doc.text(clean(value || '-'), x + 3, top + 11.5);
    };
    doc.setLineWidth(0.4);
    doc.rect(page.margin, boxTop, width, 30);
    doc.line(page.margin, boxTop + 15, page.margin + width, boxTop + 15);
    doc.line(page.margin + half, boxTop, page.margin + half, boxTop + 30);
    cell('Candidate surname', candidate.surname, page.margin, boxTop);
    cell('Other names', candidate.otherNames, page.margin + half, boxTop);
    cell('Centre Number', candidate.centre, page.margin, boxTop + 15);
    cell('Candidate Number', candidate.candidateNumber, page.margin + half, boxTop + 15);
    y = boxTop + 35;

    text('Started: ' + when(state.startedAt) + '     Status: ' + (state.submitted ? 'Submitted' : 'Not yet submitted'), 9, 'normal', 1);
    text('Downloaded: ' + when(Date.now()), 9, 'normal', 3);

    const marks = new Map((report?.questions || []).map(row => [row.id, row]));
    if (report) {
      const review = report.questions.filter(row => row.review).map(row => row.id);
      text('Provisional mark: ' + report.total + ' / 80', 16, 'bold', 1);
      text('Marked automatically against the June 2024 mark scheme. Your teacher reviews every result before it is final.', 9, 'italic', 1);
      if (review.length) text('Parts for teacher review: ' + review.join(', '), 9, 'normal', 3);

      // Mark summary table: question, mark, out of.
      const cols = [page.margin, page.margin + 40, page.margin + 80];
      room(8);
      doc.setFont('helvetica', 'bold'); doc.setFontSize(9);
      ['Question', 'Mark', 'Out of'].forEach((label, i) => doc.text(label, cols[i] + 2, y + 4));
      doc.setLineWidth(0.3);
      doc.line(page.margin, y + 6, page.margin + 120, y + 6);
      y += 7;
      doc.setFont('helvetica', 'normal');
      for (const question of questions) {
        const row = marks.get(question.id);
        room(5.5);
        doc.text(question.id + (row?.review ? '  (review)' : ''), cols[0] + 2, y + 4);
        doc.text(String(row?.mark ?? '-'), cols[1] + 2, y + 4);
        doc.text(String(question.max), cols[2] + 2, y + 4);
        y += 5.5;
      }
      room(7);
      doc.setFont('helvetica', 'bold');
      doc.line(page.margin, y + 0.5, page.margin + 120, y + 0.5);
      doc.text('Total', cols[0] + 2, y + 5);
      doc.text(String(report.total), cols[1] + 2, y + 5);
      doc.text('80', cols[2] + 2, y + 5);
      y += 10;
    }

    // Every question part with the candidate's answer (and mark and feedback).
    for (const question of questions) {
      const row = marks.get(question.id);
      room(22);
      rule();
      const heading = 'Question ' + question.id + '  -  ' + (row ? row.mark + ' / ' + question.max + ' marks' : question.max + (question.max === 1 ? ' mark' : ' marks'));
      text(heading + (row?.review ? '   [Teacher review]' : ''), 11.5, 'bold', 1.5);
      text('Answer', 9, 'bold', 0.5);
      text(answerText(question.id, state.answers[question.id]), 10, 'normal', 2);
      if (row) {
        text('Feedback', 9, 'bold', 0.5);
        text(row.feedback, 10, 'italic', 2);
      }
    }

    // Footer on every page.
    const pages = doc.getNumberOfPages();
    const name = [candidate.otherNames, candidate.surname].filter(Boolean).join(' ') || 'Candidate';
    for (let n = 1; n <= pages; n++) {
      doc.setPage(n);
      doc.setFont('helvetica', 'normal'); doc.setFontSize(8); doc.setTextColor(90);
      doc.text(clean(name + ' - ' + (candidate.candidateNumber || '') + ' - 31769H June 2024 mock'), page.margin, page.h - 10);
      doc.text('Page ' + n + ' of ' + pages, page.w - page.margin, page.h - 10, { align: 'right' });
      doc.setTextColor(0);
    }

    const slug = (candidate.surname || 'candidate').replace(/[^A-Za-z0-9-]+/g, '-').replace(/^-|-$/g, '') || 'candidate';
    doc.save('unit2-june2024-' + (withMarks ? 'report' : 'answers') + '-' + slug + '-' + (candidate.candidateNumber || '0000') + '.pdf');
  }

  return { download: withMarks => build(withMarks) };
})();
