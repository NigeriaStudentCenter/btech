'use strict';
(async () => {
const KEY = 'unit2-pastpapers-v1', FORMAT = 'unit2-pastpapers-v1';
const $ = id => document.getElementById(id);
let data, state = {answers: {}, qtext: {}, marks: {}}, saved = true, current;
const chats = {}; // tutor conversations stay in page memory only

function el(tag, attrs = {}, ...kids) {
 const e = document.createElement(tag);
 for (const [k, v] of Object.entries(attrs)) {
  if (v === undefined || v === null || v === false) continue;
  if (k === 'class') e.className = v; else if (k === 'text') e.textContent = v;
  else if (k.startsWith('on')) e.addEventListener(k.slice(2), v); else e.setAttribute(k, v === true ? '' : v);
 }
 for (const k of kids.flat()) if (k !== null && k !== undefined && k !== false) e.append(k);
 return e;
}
function status(msg, error = false) { $('status').textContent = msg; $('status').className = error ? 'error' : ''; }
function save() {
 try { localStorage.setItem(KEY, JSON.stringify(state)); saved = true; status('Saved on this device. Download your answers before changing computers.'); }
 catch { saved = false; status('Browser saving is unavailable. Download your answers before closing.', true); }
}
function validState(v) {
 if (!v || typeof v !== 'object' || Array.isArray(v)) throw Error('Invalid backup.');
 const out = {answers: {}, qtext: {}, marks: {}};
 for (const k of Object.keys(out)) if (v[k] && typeof v[k] === 'object' && !Array.isArray(v[k])) for (const [id, val] of Object.entries(v[k])) {
  if (!/^[a-z]{3}\d{2}-[1-4][a-h]$/.test(id)) continue;
  if (k === 'marks' ? Number.isInteger(val) && val >= 0 && val <= 12 : typeof val === 'string' && val.length <= 8000) out[k][id] = val;
 }
 return out;
}
const pid = (paper, q, p) => `${paper.id}-${q.q}${p.p}`;

function paperScore(paper) {
 let got = 0, done = 0;
 for (const q of paper.questions) for (const p of q.parts) { const m = state.marks[pid(paper, q, p)]; if (Number.isInteger(m)) { got += m; done += p.marks; } }
 return {got, done};
}
function updateScore(paper) {
 const s = paperScore(paper);
 $('score').textContent = s.done ? `Your marks so far: ${s.got} out of ${s.done} marked (paper total 80).` : 'Record your marks after checking the mark scheme to see your total here.';
}

// ---------- tutor ----------
async function askTutor(paper, q, p, mode, box) {
 const key = pid(paper, q, p), log = box.querySelector('.tutorlog'), buttons = box.querySelectorAll('button');
 const note = box.querySelector('input').value.trim();
 const qtext = (state.qtext[key] || '').trim(), answer = (state.answers[key] || '').trim();
 if (mode === 'check' && answer.length < 5) { log.textContent = 'Write your answer in the box above first, then press Check my answer.'; return; }
 if (!window.TUTOR_API_URL) { log.textContent = 'The AI tutor is not connected yet. Keep practising, then use the mark scheme.'; return; }
 const parts = [];
 if (qtext) parts.push('Question wording: ' + qtext);
 if (mode === 'check') parts.push('My answer: ' + answer);
 if (mode === 'plan' && answer) parts.push('My notes so far: ' + answer);
 parts.push(note || {start: 'Please help me start this question.', check: 'Please check my answer.', plan: 'Please help me plan my answer.'}[mode]);
 const message = parts.join('\n\n').slice(0, 6000);
 const history = chats[key] ||= [];
 buttons.forEach(b => b.disabled = true);
 const thinking = el('p', {class: 'bot', text: 'Thinking…'});
 log.append(el('p', {class: 'you', text: 'You: ' + (note || {start: 'Help me start', check: 'Check my answer', plan: 'Plan my long answer'}[mode])}), thinking);
 try {
  const r = await fetch(window.TUTOR_API_URL, {method: 'POST', credentials: 'omit', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({paper: paper.id, part: `${q.q}${p.p}`, mode, message, history: history.slice(-6)}), signal: AbortSignal.timeout(60000)});
  const d = await r.json();
  if (!r.ok) throw Error(d.error || 'The tutor is unavailable.');
  history.push({role: 'user', content: message}, {role: 'assistant', content: d.reply});
  chats[key] = history.slice(-6);
  thinking.textContent = d.reply;
  box.querySelector('input').value = '';
 } catch (e) {
  thinking.textContent = e.name === 'TimeoutError' ? 'The tutor took too long. Please try again.' : e instanceof TypeError || e instanceof SyntaxError ? 'The tutor is offline or busy at the moment. Keep going with your answer, then use the mark scheme.' : e.message;
 } finally { buttons.forEach(b => b.disabled = false); }
}

// ---------- rendering ----------
function renderPart(paper, q, p) {
 const key = pid(paper, q, p);
 const qtext = el('textarea', {rows: 3, placeholder: 'Optional: copy the question wording from the PDF so the tutor can see exactly what is asked.', 'aria-label': 'Question wording'});
 qtext.value = state.qtext[key] || '';
 qtext.addEventListener('input', () => { state.qtext[key] = qtext.value; save(); });
 const ans = el('textarea', {rows: Math.min(16, 3 + Math.round(p.marks * 1.2)), placeholder: p.marks >= 6 ? 'Write in paragraphs: make a point, explain it, apply it to the scenario.' : 'Your answer', 'aria-label': `Answer ${q.q}(${p.p})`});
 ans.value = state.answers[key] || '';
 ans.addEventListener('input', () => { state.answers[key] = ans.value; save(); });
 const mark = el('select', {'aria-label': `My mark for ${q.q}(${p.p})`}, el('option', {value: '', text: 'not marked yet'}), Array.from({length: p.marks + 1}, (_, i) => el('option', {value: String(i), text: `${i} / ${p.marks}`})));
 mark.value = Number.isInteger(state.marks[key]) ? String(state.marks[key]) : '';
 mark.addEventListener('change', () => { if (mark.value === '') delete state.marks[key]; else state.marks[key] = Number(mark.value); save(); updateScore(paper); });
 const box = el('div', {class: 'tutor'});
 box.append(
  el('div', {class: 'tools', style: 'margin-top:0'},
   el('strong', {text: 'AI tutor:'}),
   el('button', {type: 'button', text: 'Help me start', onclick: () => askTutor(paper, q, p, 'start', box)}),
   el('button', {type: 'button', text: 'Check my answer', onclick: () => askTutor(paper, q, p, 'check', box)}),
   p.marks >= 6 ? el('button', {type: 'button', text: 'Plan my long answer', onclick: () => askTutor(paper, q, p, 'plan', box)}) : null),
  el('input', {type: 'text', maxlength: 500, placeholder: 'Optional: ask the tutor a follow-up question', 'aria-label': 'Question for the tutor', style: 'margin-top:8px'}),
  el('div', {class: 'tutorlog', role: 'log', 'aria-live': 'polite'}));
 return el('div', {class: 'part'},
  el('div', {class: 'phead'}, el('h4', {text: `${q.q}(${p.p})`}), el('span', {class: 'badge', text: `${p.marks} mark${p.marks > 1 ? 's' : ''} · ${p.cmd}`})),
  el('p', {class: 'topic', text: 'Topic: ' + p.topic + ' · ', }, el('a', {href: 'learning.html#' + p.section, text: 'revise ' + p.section})),
  el('details', {class: 'qtext', open: !!state.qtext[key]}, el('summary', {text: 'Paste the question wording (optional)'}), qtext),
  ans,
  box,
  el('label', {class: 'mymark small'}, 'After checking the mark scheme, my mark: ', mark));
}
function renderPaper(paper) {
 const base = data.base, wrap = $('paper');
 const link = (file, text, cls) => file ? el('a', {href: base + file, target: '_blank', rel: 'noopener', class: cls, text}) : el('span', {class: 'small', text: 'Examiner’s report: not published for this series'});
 const card = el('section', {class: 'paper'},
  el('h2', {text: `${paper.title} paper`}),
  el('p', {class: 'small', text: `${paper.date} · 80 marks · 1 hour 45 minutes · 4 questions`}),
  el('div', {class: 'links'}, link(paper.qp, 'Open the question paper (PDF) ↗', 'qp')),
  el('details', {class: 'after'}, el('summary', {text: 'After your attempt: mark scheme and examiner’s report'}),
   el('p', {class: 'small', text: 'Mark your own answers honestly. The examiner’s report explains what strong and weak answers looked like.'}),
   el('div', {class: 'links'}, link(paper.ms, 'Mark scheme (PDF) ↗'), link(paper.er, 'Examiner’s report (PDF) ↗'))),
  el('p', {class: 'score', id: 'score'}));
 const qs = paper.questions.map(q => el('details', {class: 'q'},
  el('summary', {}, el('span', {text: `Question ${q.q}: ${q.scenario}`}), el('span', {class: 'badge', text: q.parts.reduce((n, p) => n + p.marks, 0) + ' marks'})),
  el('div', {class: 'qbody'}, q.parts.map(p => renderPart(paper, q, p)))));
 wrap.replaceChildren(card, ...qs);
 updateScore(paper);
}
function showPaper(id) {
 current = data.papers.find(p => p.id === id) || data.papers[0];
 for (const b of $('tabs').children) { const on = b.dataset.paper === current.id; b.classList.toggle('current', on); b.setAttribute('aria-pressed', String(on)); }
 renderPaper(current);
 try { history.replaceState(null, '', '#' + current.id); } catch {}
}

// ---------- backup ----------
$('download').onclick = () => {
 save();
 const url = URL.createObjectURL(new Blob([JSON.stringify({format: FORMAT, ...state}, null, 2)], {type: 'application/json'}));
 const a = el('a', {href: url, download: 'my-past-paper-answers.json'}); a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
};
$('restore').onclick = () => $('backup').click();
$('backup').onchange = async e => {
 try {
  const file = e.target.files[0]; if (!file) return;
  if (file.size > 800000) throw Error('That backup is too large.');
  const d = JSON.parse(await file.text());
  if (d.format !== FORMAT) throw Error('Choose a backup from the Past Exam Papers page.');
  const incoming = validState(d);
  if (!confirm('This replaces the past paper answers on this device with the backup. Continue?')) return;
  state = incoming; save(); showPaper(current.id); status('Backup restored.');
 } catch (err) { status(err.message || 'That file could not be read.', true); } finally { $('backup').value = ''; }
};
$('clear').onclick = () => {
 if (!confirm('Clear every past paper answer saved in this browser? Download your answers first if you want to keep them.')) return;
 try { localStorage.removeItem(KEY); } catch { status('Could not clear browser storage. Use the browser’s site-data settings.', true); return; }
 state = {answers: {}, qtext: {}, marks: {}}; showPaper(current.id); saved = true; status('Answers cleared from this browser. Your downloaded files are unchanged.');
};
window.addEventListener('hashchange', () => { if (data && location.hash.slice(1) !== current.id) showPaper(location.hash.slice(1)); });
window.addEventListener('beforeunload', e => { if (!saved) { e.preventDefault(); e.returnValue = ''; } });

// ---------- start ----------
try { data = await (await fetch('past-papers.json')).json(); }
catch { status('The list of papers could not load. Check your connection and refresh.', true); return; }
let loadError = false;
try { state = validState(JSON.parse(localStorage.getItem(KEY) || '{}')); } catch { loadError = true; }
for (const p of data.papers) $('tabs').append(el('button', {type: 'button', 'data-paper': p.id, text: p.title, onclick: () => showPaper(p.id)}));
showPaper(location.hash.slice(1));
status(loadError ? 'Saved answers could not load. Keep any backup safe.' : 'Ready. Answers save on this device as you type.', loadError);
})();
