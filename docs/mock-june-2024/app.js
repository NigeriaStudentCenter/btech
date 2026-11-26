'use strict';
const EXAM = {
  id: '31769H-2024-06',
  minutes: 105,
  questions: [
    { id: '1a', max: 3, pages: [2] },
    { id: '1b', max: 3, pages: [3] },
    { id: '1c', max: 4, pages: [4] },
    { id: '1d', max: 2, pages: [5] },
    { id: '1e', max: 1, pages: [6] },
    { id: '1f', max: 4, pages: [7] },
    { id: '1g', max: 3, pages: [8] },
    { id: '2a', max: 2, pages: [10] },
    { id: '2b', max: 4, pages: [10] },
    { id: '2c', max: 4, pages: [11] },
    { id: '2d', max: 3, pages: [12] },
    { id: '2e', max: 3, pages: [12] },
    { id: '2f', max: 4, pages: [14, 15] },
    { id: '3a', max: 4, pages: [16] },
    { id: '3b', max: 6, pages: [16, 17] },
    { id: '3c', max: 8, pages: [18, 19] },
    { id: '4a', max: 10, pages: [20, 21] },
    { id: '4b', max: 12, pages: [22, 23] },
  ]
};
const element = id => document.getElementById(id);
const storageKey = 'mock-31769H-jun2024-v1';
const questions = EXAM.questions;
const tableRows = { '2e': 3, '2f': 4 };
const initial = { version: 1, examId: EXAM.id, candidate: null, startedAt: null, deadline: null, submitted: false, report: null };
const candidateFields = ['surname', 'otherNames', 'centre', 'candidateNumber'];
let state = { ...initial, answers: {} };
let current = 0;
let marking = false;

function announce(message) {
  const target = element('exam').hidden ? 'introStatus' : 'status';
  element(target).textContent = message;
}

function save() {
  try {
    localStorage.setItem(storageKey, JSON.stringify(state));
    return true;
  } catch {
    announce('Browser saving failed. Download a copy before leaving.');
    return false;
  }
}

function cleanCandidate(value) {
  if (!value || typeof value !== 'object') return null;
  const surname = String(value.surname ?? '').trim().slice(0, 60);
  const otherNames = String(value.otherNames ?? '').trim().slice(0, 60);
  const centre = String(value.centre ?? '').trim();
  const candidateNumber = String(value.candidateNumber ?? '').trim();
  if (!surname || !otherNames || !/^\d{5}$/.test(centre) || !/^\d{4}$/.test(candidateNumber)) return null;
  return { surname, otherNames, centre, candidateNumber };
}

function candidateFromForm() {
  const values = Object.fromEntries(candidateFields.map(id => [id, element(id).value]));
  const candidate = cleanCandidate(values);
  if (candidate) return candidate;
  if (!values.surname.trim()) throw Error('Enter your surname.');
  if (!values.otherNames.trim()) throw Error('Enter your other names.');
  if (!/^\d{5}$/.test(values.centre.trim())) throw Error('Enter your 5-digit centre number.');
  throw Error('Enter your 4-digit candidate number.');
}

function showCandidate() {
  const candidate = state.candidate;
  for (const id of candidateFields) {
    element(id).value = candidate?.[id] ?? element(id).value;
    element(id).readOnly = state.startedAt !== null;
  }
  element('candidateBadge').textContent = candidate
    ? candidate.surname + ', ' + candidate.otherNames + ' · Centre ' + candidate.centre + ' · Candidate ' + candidate.candidateNumber
    : '';
}

function validate(copy) {
  if (copy?.version !== 1 || copy.examId !== EXAM.id || typeof copy.submitted !== 'boolean' ||
      !copy.answers || typeof copy.answers !== 'object' || Array.isArray(copy.answers)) {
    throw Error('Choose a June 2024 mock backup.');
  }
  if (!Number.isSafeInteger(copy.startedAt) || copy.startedAt <= 0 ||
      copy.deadline !== copy.startedAt + EXAM.minutes * 60000) {
    throw Error('The backup has an invalid timer.');
  }
  const answers = {};
  for (const [id, answer] of Object.entries(copy.answers)) {
    if (!questions.some(question => question.id === id)) throw Error('Unknown question in backup.');
    const rows = tableRows[id];
    const valid = rows
      ? Array.isArray(answer) && answer.length === rows && answer.every(value => typeof value === 'string' && value.length <= 200)
      : typeof answer === 'string' && answer.length <= 15000;
    if (!valid) throw Error('Invalid answer in backup.');
    answers[id] = answer;
  }
  return { ...initial, candidate: cleanCandidate(copy.candidate), startedAt: copy.startedAt, deadline: copy.deadline, submitted: copy.submitted, answers, report: copy.submitted && validReport(copy.report) ? copy.report : null };
}

function attempted(id) {
  const answer = state.answers[id];
  return Array.isArray(answer) ? answer.some(value => value.trim()) : Boolean(answer?.trim());
}

function updateNavigation() {
  const active = questions[current].id;
  for (const button of element('nav').children) {
    button.classList.toggle('current', button.dataset.id === active);
    button.classList.toggle('answered', attempted(button.dataset.id));
    button.setAttribute('aria-current', button.dataset.id === active ? 'step' : 'false');
  }
  const count = questions.filter(question => attempted(question.id)).length;
  element('progress').textContent = count + ' / ' + questions.length + ' parts attempted';
}

function render() {
  const question = questions[current];
  const id = question.id;
  const rows = tableRows[id];
  const answer = state.answers[id];
  element('answerTitle').textContent = 'Your answer · ' + question.max + (question.max === 1 ? ' mark' : ' marks');
  window.mockPaper.show(id);
  element('fields').replaceChildren();

  for (let row = 0; row < (rows ?? 1); row++) {
    const label = document.createElement('label');
    const input = document.createElement(rows ? 'input' : 'textarea');
    input.id = 'response-' + row;
    label.htmlFor = input.id;
    label.textContent = rows ? 'Row ' + (row + 1) : 'Your answer to ' + id;
    input.maxLength = rows ? 200 : 15000;
    input.spellcheck = false;
    input.autocomplete = 'off';
    input.value = (rows ? answer?.[row] : answer) ?? '';
    input.readOnly = state.submitted;
    input.addEventListener('input', () => {
      if (rows) {
        state.answers[id] ??= Array(rows).fill('');
        state.answers[id][row] = input.value;
      } else {
        state.answers[id] = input.value;
      }
      if (save()) announce('Saved. Download a copy before leaving.');
      updateNavigation();
    });
    element('fields').append(label, input);
  }

  element('previous').disabled = current === 0;
  element('next').disabled = current === questions.length - 1;
  element('submit').disabled = state.submitted;
  updateNavigation();
}

function tick() {
  if (state.startedAt === null) return;
  if (state.submitted) {
    element('clock').textContent = 'Finished';
    return;
  }
  const seconds = Math.max(0, Math.ceil((state.deadline - Date.now()) / 1000));
  element('clock').textContent = String(Math.floor(seconds / 60)).padStart(2, '0') + ':' +
    String(seconds % 60).padStart(2, '0');
  if (seconds === 0) {
    if (element('ask').open) element('askNo').click();
    finish(true);
  }
}

// On-page confirmation, because some browsers (in-app and embedded ones) block pop-ups.
function ask(message, yes) {
  const box = element('ask');
  element('askText').textContent = message;
  element('askYes').textContent = yes;
  return new Promise(resolve => {
    const done = answer => { box.close(); element('askYes').onclick = element('askNo').onclick = box.oncancel = null; resolve(answer); };
    element('askYes').onclick = () => done(true);
    element('askNo').onclick = () => done(false);
    box.oncancel = event => { event.preventDefault(); done(false); };
    box.showModal();
    element('askNo').focus();
  });
}

async function finish(automatic = false) {
  if (state.submitted) return;
  const unanswered = questions.filter(question => !attempted(question.id)).length;
  if (!automatic) {
    if (element('ask').open) return;
    const sure = await ask('Finish and lock your answers? ' + (unanswered ? unanswered + (unanswered === 1 ? ' part has' : ' parts have') + ' no answer.' : 'Every part has an answer.') + ' You cannot change them after this.', 'Yes, submit');
    if (!sure || state.submitted) return;
  }
  state.submitted = true;
  if (save()) announce('Answers submitted and saved on this device.');
  render();
  tick();
  mark();
}

function start() {
  if (state.startedAt === null || !state.candidate) {
    try {
      state.candidate = candidateFromForm();
    } catch (error) {
      if (state.startedAt === null) {
        announce(error.message);
        element(candidateFields.find(id => !element(id).checkValidity() || !element(id).value.trim()) ?? 'surname').focus();
        return;
      }
    }
  }
  element('intro').hidden = true;
  element('exam').hidden = false;
  showCandidate();
  if (state.startedAt === null) {
    state.startedAt = Date.now();
    state.deadline = state.startedAt + EXAM.minutes * 60000;
    save();
  }
  render();
  tick();
  renderReport();
}

element('start').onclick = start;
element('submit').onclick = () => finish();
element('previous').onclick = () => { current--; render(); };
element('next').onclick = () => { current++; render(); };
element('restore').onclick = () => element('file').click();
element('restoreDuringExam').onclick = () => element('file').click();
element('file').onchange = async event => {
  const file = event.target.files[0];
  if (!file) return;
  try {
    if (file.size > 400000) throw Error('The backup file is too large.');
    const copy = validate(JSON.parse(await file.text()));
    if (!await ask('Replace the answers saved in this browser with this backup?', 'Replace')) return;
    state = copy;
    start();
    if (save()) announce('Backup restored.');
  } catch (error) {
    announce('Could not restore backup. ' + error.message);
  } finally {
    event.target.value = '';
  }
};

function validReport(report) {
  if (report?.examId !== EXAM.id || !Array.isArray(report.questions) || report.questions.length !== questions.length) return false;
  const marks = new Map(report.questions.map(row => [row?.id, row]));
  return questions.every(question => {
    const row = marks.get(question.id);
    return row && row.max === question.max && Number.isInteger(row.mark) &&
      row.mark >= 0 && row.mark <= question.max && typeof row.feedback === 'string';
  }) && report.total === report.questions.reduce((total, row) => total + row.mark, 0);
}

function renderReport() {
  const report = state.report;
  const endpoint = window.MOCK_MARKING_ENDPOINT;
  element('retryMarking').hidden = !state.submitted || !!report || !endpoint;
  element('retryMarking').disabled = marking;
  element('downloadReport').hidden = !report;
  element('markingReport').hidden = !report;
  const results = element('results');
  results.replaceChildren();
  if (!report) return;
  const total = document.createElement('p');
  total.textContent = 'Provisional mark ' + report.total + ' / 80. Your teacher reviews the result.';
  results.append(total);
  for (const row of report.questions) {
    const article = document.createElement('article');
    const heading = document.createElement('h3');
    const feedback = document.createElement('p');
    heading.textContent = row.id + ' · ' + row.mark + ' / ' + row.max + (row.review ? ' · Teacher review' : '');
    feedback.textContent = row.feedback;
    article.append(heading, feedback);
    results.append(article);
  }
}

async function mark() {
  if (marking || state.report || !state.submitted) return;
  const endpoint = window.MOCK_MARKING_ENDPOINT;
  if (!endpoint) {
    announce('Answers saved. Automatic marking is available through the centre marking service. Download your answers for your teacher.');
    return;
  }
  marking = true;
  element('restoreDuringExam').disabled = true;
  element('clear').disabled = true;
  renderReport();
  announce('Marking in progress. Your answers are saved on this device.');
  try {
    const response = await fetch(endpoint, {
      method: 'POST',
      credentials: 'same-origin',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ examId: EXAM.id, candidate: state.candidate, answers: state.answers }),
      signal: AbortSignal.timeout(120000)
    });
    const report = await response.json();
    if (!response.ok || !validReport(report)) throw Error('Marking did not complete.');
    state.report = report;
    if (save()) announce('Marking complete. Download the provisional report for your teacher.');
  } catch {
    announce('Marking could not finish. Your answers are saved. Retry or download a copy.');
  } finally {
    marking = false;
    element('restoreDuringExam').disabled = false;
    element('clear').disabled = false;
    renderReport();
  }
}

function downloadJson(value, name) {
  const url = URL.createObjectURL(new Blob([JSON.stringify(value, null, 2)], { type: 'application/json' }));
  const link = document.createElement('a');
  link.href = url;
  link.download = name;
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

element('retryMarking').onclick = mark;
async function downloadPdf(withMarks) {
  const button = element(withMarks ? 'downloadReport' : 'download');
  button.disabled = true;
  announce('Preparing the PDF…');
  try {
    await window.mockReport.download(withMarks);
    announce(withMarks ? 'Marking report downloaded.' : 'Answers downloaded.');
  } catch {
    announce('The PDF could not be made. Use Print answers or Save backup file instead.');
  } finally {
    button.disabled = false;
  }
}

element('downloadReport').onclick = () => downloadPdf(true);
element('download').onclick = () => downloadPdf(false);
element('backup').onclick = () => downloadJson(state, 'unit2-june2024-backup-' + (state.candidate?.candidateNumber ?? 'candidate') + '.json');
element('clear').onclick = async () => {
  if (!await ask('Clear this mock and its answers from this browser? Download a copy first.', 'Clear')) return;
  try {
    localStorage.removeItem(storageKey);
    location.reload();
  } catch {
    announce('Could not clear this browser’s saved copy.');
  }
};
element('print').onclick = () => {
  document.querySelector('.printOnly')?.remove();
  const output = document.createElement('div');
  output.className = 'printOnly';
  const title = document.createElement('h1');
  title.textContent = 'Unit 2 June 2024 mock answers';
  const who = document.createElement('p');
  who.textContent = element('candidateBadge').textContent;
  output.append(title, who);
  for (const question of questions) {
    const article = document.createElement('article');
    const heading = document.createElement('h2');
    const response = document.createElement('pre');
    const answer = state.answers[question.id];
    heading.textContent = question.id + ' · ' + question.max + ' marks';
    response.textContent = Array.isArray(answer)
      ? answer.map((value, row) => 'Row ' + (row + 1) + ': ' + value).join('\n')
      : answer || '(No answer)';
    article.append(heading, response);
    output.append(article);
  }
  document.body.append(output);
  window.print();
};

for (const [position, question] of questions.entries()) {
  const button = document.createElement('button');
  button.textContent = question.id;
  button.dataset.id = question.id;
  button.onclick = () => { current = position; render(); };
  element('nav').append(button);
}

try {
  const saved = localStorage.getItem(storageKey);
  if (saved) state = validate(JSON.parse(saved));
} catch {
  announce('Saved work is unavailable. You can restore a backup or start a new mock.');
}
showCandidate();
element('candidateForm').onsubmit = event => { event.preventDefault(); start(); };
for (const id of ['centre', 'candidateNumber']) {
  element(id).addEventListener('input', () => { element(id).value = element(id).value.replace(/\D/g, ''); });
}
if (state.startedAt !== null) start();
setInterval(tick, 1000);
