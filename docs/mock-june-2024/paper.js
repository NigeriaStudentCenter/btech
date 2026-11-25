'use strict';

window.mockPaper = (() => {
  const source = 'https://qualifications.pearson.com/content/dam/pdf/BTEC-Nationals/Computing/2016/External-assessments/p75938-btec-l3-computing-31769h-unit-2-jun-2024.pdf';
  const runtime = 'https://cdn.jsdelivr.net/npm/pdfjs-dist@5.6.205/build';
  const checksum = 'b77f724501691d94b7fb52987d34b05a1829c58eb790de9fca5b467d3e3fbf30';
  const get = id => document.getElementById(id);
  let resolvePaper;
  const ready = new Promise(resolve => { resolvePaper = resolve; });
  const pages = new Map();
  let version = 0;

  function setStatus(message, canSelect = false) {
    get('paperStatus').textContent = message;
    get('choosePaper').hidden = !canSelect;
  }

  async function open(bytes) {
    const digest = await crypto.subtle.digest('SHA-256', bytes);
    const hex = Array.from(new Uint8Array(digest), value => value.toString(16).padStart(2, '0')).join('');
    if (hex !== checksum) throw Error('Choose the original June 2024 31769H question paper.');
    const reader = await import(runtime + '/pdf.min.mjs');
    reader.GlobalWorkerOptions.workerSrc = runtime + '/pdf.worker.min.mjs';
    return reader.getDocument({ data: bytes, isEvalSupported: false }).promise;
  }

  function paragraph(container, lines) {
    let buffer = [];
    const flush = () => {
      if (!buffer.length) return;
      const p = document.createElement('p');
      p.textContent = buffer.join(' ');
      container.append(p);
      buffer = [];
    };
    let lastY = -Infinity;
    for (const { y, text } of lines) {
      if (y - lastY > 17 || text.startsWith('•')) flush();
      buffer.push(text);
      lastY = y;
    }
    flush();
  }

  async function pageData(pdf, number) {
    if (!pages.has(number)) {
      pages.set(number, (async () => {
        const page = await pdf.getPage(number);
        const content = await page.getTextContent();
        const byLine = new Map();
        for (const item of content.items) {
          if (!item.str?.trim() || Math.abs(item.transform[1]) > 0.1) continue;
          const x = item.transform[4];
          const y = Math.round(898.583 - item.transform[5] - item.height * 0.76);
          if (x < 50 || x > 590) continue;
          const key = [...byLine.keys()].find(top => Math.abs(top - y) <= 2) ?? y;
          if (!byLine.has(key)) byLine.set(key, []);
          byLine.get(key).push({ x, text: item.str.trim() });
        }
        const lines = Array.from(byLine, ([y, parts]) => ({
          y,
          text: parts.sort((a, b) => a.x - b.x).map(part => part.text).join(' ').replace(/\s+([:;,.!?)])/g, '$1')
        })).sort((a, b) => a.y - b.y);
        return { page, lines };
      })());
    }
    return pages.get(number);
  }

  function figure(container, image, label) {
    const holder = document.createElement('figure');
    const caption = document.createElement('figcaption');
    caption.textContent = label;
    holder.append(image, caption);
    container.append(holder);
  }

  async function append(container, section, pdf, prepared) {
    const key = JSON.stringify(section);
    if (prepared) {
      const item = prepared[key];
      if (item.lines) paragraph(container, item.lines);
      else {
        const image = document.createElement('img');
        image.src = item.src;
        image.alt = section.label;
        figure(container, image, section.label);
      }
      return;
    }
    const { page, lines } = await pageData(pdf, section.page);
    if (!section.bounds) {
      paragraph(container, lines.filter(line => line.y >= section.from && line.y < section.to &&
        !/^(\(\d+\)|[.\s]+)$/.test(line.text) && line.text.split('.').length < 20));
      return;
    }
    const [left, top, right, bottom] = section.bounds;
    const scale = 2;
    const canvas = document.createElement('canvas');
    canvas.width = Math.ceil((right - left) * scale);
    canvas.height = Math.ceil((bottom - top) * scale);
    canvas.setAttribute('role', 'img');
    canvas.setAttribute('aria-label', section.label);
    const viewport = page.getViewport({ scale });
    const offsetX = left - viewport.viewBox[0];
    const offsetY = top - (898.583 - viewport.viewBox[3]);
    await page.render({ canvas, viewport, transform: [1, 0, 0, 1, -offsetX * scale, -offsetY * scale] }).promise;
    figure(container, canvas, section.label);
  }

  async function show(id) {
    const ticket = ++version;
    const question = get('question');
    get('questionTitle').textContent = 'Question ' + id;
    get('scenario').hidden = true;
    get('scenario').open = false;
    question.textContent = 'Loading question…';
    const { pdf, prepared } = await ready;
    if (ticket !== version) return;
    try {
      const content = document.createDocumentFragment();
      for (const section of window.MOCK_LAYOUT.questions[id]) await append(content, section, pdf, prepared);
      const scenario = document.createDocumentFragment();
      if (!id.endsWith('a')) await append(scenario, window.MOCK_LAYOUT.context[id[0]], pdf, prepared);
      if (ticket !== version) return;
      question.replaceChildren(content);
      get('scenarioText').replaceChildren(scenario);
      get('scenario').hidden = id.endsWith('a');
    } catch {
      if (ticket === version) question.textContent = 'The question could not be displayed. Reload the page to retry.';
    }
  }

  function finish(document) {
    resolvePaper(document);
    setStatus('All 18 question parts are ready.');
    get('start').disabled = false;
  }

  if (window.MOCK_PREPARED_PAPER) finish({ prepared: window.MOCK_PREPARED_PAPER });
  else {
    get('sourceFile').onchange = async event => {
      const file = event.target.files[0];
      if (!file) return;
      try {
        finish({ pdf: await open(await file.arrayBuffer()) });
      } catch (error) {
        setStatus(error.message, true);
      } finally {
        event.target.value = '';
      }
    };
    fetch(source, { signal: AbortSignal.timeout(12000) })
      .then(response => {
        if (!response.ok) throw Error('Source paper unavailable.');
        return response.arrayBuffer();
      })
      .then(open)
      .then(pdf => finish({ pdf }))
      .catch(() => setStatus('The source paper could not be loaded. Select your centre’s original June 2024 paper to continue.', true));
  }
  return { show };
})();
