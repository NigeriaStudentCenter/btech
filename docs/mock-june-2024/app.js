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
const paperUrl = document.getElementById('paperLink').href;
const element = id => document.getElementById(id);
const storageKey = 'mock-31769H-jun2024-v1';
const questions = EXAM.questions;
const tableRows = { '2e': 3, '2f': 4 };
const initial = { version: 1, examId: EXAM.id, startedAt: null, deadline: null, submitted: false };
let state = { ...initial, answers: {} };
let current = 0;

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
  return { ...initial, startedAt: copy.startedAt, deadline: copy.deadline, submitted: copy.submitted, answers };
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
  element('answerTitle').textContent = 'Question ' + id + ' · ' + question.max + ' marks';
  element('pageNumber').textContent = 'PDF page ' + question.pages.join('–');
  element('questionLink').href = paperUrl + '#page=' + question.pages[0];
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
  if (seconds === 0) finish(true);
}

function finish(automatic = false) {
  if (state.submitted) return;
  const unanswered = questions.filter(question => !attempted(question.id)).length;
  if (!automatic && !confirm('Finish and lock your answers? ' + unanswered + ' parts have no answer.')) return;
  state.submitted = true;
  if (save()) announce('Answers locked. Download or print a copy for your teacher.');
  render();
  tick();
}

function start() {
  element('intro').hidden = true;
  element('exam').hidden = false;
  if (state.startedAt === null) {
    state.startedAt = Date.now();
    state.deadline = state.startedAt + EXAM.minutes * 60000;
    save();
  }
  render();
  tick();
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
    if (!confirm('Replace the answers saved in this browser with this backup?')) return;
    state = copy;
    start();
    if (save()) announce('Backup restored.');
  } catch (error) {
    announce('Could not restore backup. ' + error.message);
  } finally {
    event.target.value = '';
  }
};

element('download').onclick = () => {
  const url = URL.createObjectURL(new Blob([JSON.stringify(state, null, 2)], { type: 'application/json' }));
  const link = document.createElement('a');
  link.href = url;
  link.download = 'unit2-june2024-answers.json';
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
};
element('clear').onclick = () => {
  if (!confirm('Clear this mock and its answers from this browser? Download a copy first.')) return;
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
  output.append(title);
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
if (state.startedAt !== null) start();
setInterval(tick, 1000);
