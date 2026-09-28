'use strict';
(() => {
const TESTS = window.REVISION_TESTS, KEY = 'unit2-revision-v1', FORMAT = 'unit2-revision-v1';
const $ = id => document.getElementById(id);
let state = {answers: {}, ticks: {}, marked: {}}, saved = true, current = TESTS[0].id;

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
const pid = (q, p) => q.id + p.id;
const label = p => p.label || '(' + p.id + ')';
const norm = v => String(v ?? '').trim().replace(/\s+/g, ' ');

function status(msg, error = false) { $('status').textContent = msg; $('status').className = error ? 'error' : ''; }
function save() {
 try { localStorage.setItem(KEY, JSON.stringify(state)); saved = true; status('Saved on this device. Download your revision before changing computers.'); }
 catch { saved = false; status('Browser saving is unavailable. Download your revision before closing.', true); }
}
function validState(v) {
 if (!v || typeof v !== 'object' || Array.isArray(v)) throw Error('Invalid backup.');
 const out = {answers: {}, ticks: {}, marked: {}};
 for (const k of ['answers', 'ticks', 'marked']) if (v[k] && typeof v[k] === 'object' && !Array.isArray(v[k])) out[k] = v[k];
 if (JSON.stringify(out).length > 400000) throw Error('That backup is too large.');
 return out;
}

// ---------- marking ----------
function markFields(p, ans) {
 ans = ans || {};
 const ok = {};
 for (const f of p.fields) {
  const v = norm(ans[f.id]);
  ok[f.id] = f.accept.some(a => f.exact || f.options ? v.replace(/\s/g, '') === a.replace(/\s/g, '') && (f.options ? v === a : true) : v.toLowerCase().replace(/\s/g, '') === a.toLowerCase().replace(/\s/g, ''));
 }
 for (const group of p.unordered || []) {  // same answers in any order, but no repeats
  const vals = group.map(id => norm(ans[id]));
  const distinct = new Set(vals).size === vals.length;
  for (const id of group) ok[id] = ok[id] && distinct;
 }
 const right = Object.values(ok).filter(Boolean).length;
 return {ok, score: Math.floor(right / p.fields.length * p.marks + 1e-9)};
}
function truthRows(p) {
 const rows = [];
 for (let n = 0; n < 8; n++) { const a = n >> 2 & 1, b = n >> 1 & 1, c = n & 1; rows.push({a, b, c, out: p.answer(a, b, c)}); }
 return rows;
}
function markTruth(p, ans) {
 ans = ans || {};
 const ok = {}; let right = 0, total = 0;
 truthRows(p).forEach((r, i) => r.out.forEach((v, j) => { const k = i + '-' + j; total++; ok[k] = ans[k] === String(v); if (ok[k]) right++; }));
 return {ok, score: Math.floor(right / total * p.marks + 1e-9)};
}
function markOrder(p, ans) {
 ans = ans || {};
 const seq = p.steps.map(s => s.id).filter(id => ans[id]).sort((x, y) => ans[x] - ans[y]);
 const positions = new Set(p.steps.map(s => ans[s.id]).filter(Boolean));
 if (seq.length !== p.steps.length || positions.size !== p.steps.length) return {ok: {}, score: 0, note: 'Give every step a different number.'};
 if (!p.floating) {
  const right = seq.filter((id, i) => id === p.base[i]).length, full = right === p.base.length;
  return {ok: {}, score: full ? p.marks : Math.min(p.marks - 1, Math.floor(right / p.base.length * p.marks)), note: full ? 'Correct order.' : `${right} of ${p.base.length} steps are in the right place.`};
 }
 const baseRight = JSON.stringify(seq.filter(id => id !== p.floating)) === JSON.stringify(p.base);
 const fi = seq.indexOf(p.floating), floatRight = fi > seq.indexOf(p.floatAfter) && fi < seq.indexOf(p.floatBefore);
 const score = (baseRight ? p.marks - 1 : 0) + (floatRight ? 1 : 0);
 return {ok: {}, score, note: baseRight && floatRight ? 'Correct order.' : baseRight ? 'The fetch, decode and execute steps are in the right order. Check when the PC is increased.' : 'Not quite. The address must go out before the instruction comes back, and decoding happens before executing.'};
}
function markChoice(p, ans) { return {score: ans === p.answer ? p.marks : 0}; }
const MARKERS = {fields: markFields, truth: markTruth, order: markOrder, choice: markChoice};

function selfScore(p, key) { return Math.min(p.marks, (state.ticks[key] || []).filter(Boolean).length); }
function questionScore(q) {
 let auto = 0, autoMax = 0, self = 0, selfMax = 0;
 for (const p of q.parts) {
  const key = pid(q, p);
  if (p.type === 'text') { selfMax += p.marks; self += selfScore(p, key); }
  else if (p.type === 'essay') { selfMax += p.marks; self += Math.min(p.marks, Number(state.marked[key]) || 0); }
  else { autoMax += p.marks; if (state.marked[key] !== undefined) auto += state.marked[key]; }
 }
 return {auto, autoMax, self, selfMax, total: auto + self, max: autoMax + selfMax};
}

// ---------- rendering ----------
function links(p) {
 return el('p', {class: 'links'}, 'Revise: ', el('a', {href: 'learning.html#' + p.section, text: 'lesson ' + p.section}), ' · ', el('a', {href: 'index.html?section=' + p.section, text: 'ask the tutor about ' + p.section}));
}
function hintBox(p, guided) {
 if (!p.hint) return null;
 return guided ? el('p', {class: 'hint'}, el('strong', {text: 'Hint: '}), p.hint) : el('details', {class: 'hint'}, el('summary', {text: 'Need a hint?'}), el('p', {text: p.hint}));
}
function result(key, text, good) { const r = $('r-' + key); if (r) { r.textContent = text; r.className = 'result ' + (good ? 'good' : 'try'); } }

function renderText(q, p, key, guided) {
 const box = el('div');
 const ta = el('textarea', {id: 'a-' + key, rows: Math.min(18, 3 + p.marks * 1.5 | 0), placeholder: guided && p.starter ? 'Start: ' + p.starter : 'Write your answer here.', 'aria-label': 'Answer ' + label(p)});
 ta.value = state.answers[key] || '';
 const check = el('details', {class: 'check'});
 const summary = el('summary', {text: 'Check my answer'});
 const list = el('ul', {class: 'criteria'});
 p.criteria.forEach((c, i) => {
  const cb = el('input', {type: 'checkbox', id: 'c-' + key + '-' + i});
  cb.checked = !!(state.ticks[key] || [])[i];
  cb.addEventListener('change', () => { (state.ticks[key] ||= [])[i] = cb.checked; save(); updateScores(q); });
  list.append(el('li', {}, cb, el('label', {for: cb.id, text: ' ' + c})));
 });
 const note = el('p', {class: 'small', text: p.criteria.length > p.marks ? `Tick each point your answer really makes. Up to ${p.marks} mark${p.marks > 1 ? 's' : ''}: a mark usually needs the point explained or linked to the scenario.` : 'Tick each point your answer really makes. One mark per point.'});
 check.append(summary, note, list);
 const lockCheck = () => { const empty = ta.value.trim().length < 10; check.classList.toggle('locked', empty); if (empty) check.open = false; summary.textContent = empty ? 'Check my answer (write your answer first)' : 'Check my answer'; };
 check.addEventListener('toggle', () => { if (check.open && ta.value.trim().length < 10) check.open = false; });
 ta.addEventListener('input', () => { state.answers[key] = ta.value; save(); lockCheck(); });
 lockCheck();
 box.append(ta, check);
 return box;
}
function renderChoice(q, p, key) {
 const box = el('fieldset', {class: 'choice'}, el('legend', {class: 'sr', text: 'Choose one'}));
 p.options.forEach((o, i) => {
  const r = el('input', {type: 'radio', name: 'n-' + key, id: 'o-' + key + '-' + i, value: o});
  r.checked = state.answers[key] === o;
  r.addEventListener('change', () => { state.answers[key] = o; delete state.marked[key]; save(); result(key, '', true); updateScores(q); });
  box.append(el('div', {}, r, el('label', {for: r.id, text: ' ' + o})));
 });
 return box;
}
function fieldInput(q, p, key, f, ans) {
 const id = 'f-' + key + '-' + f.id;
 const input = f.options
  ? el('select', {id}, el('option', {value: '', text: 'Choose…'}), f.options.map(o => el('option', {value: o, text: o})))
  : el('input', {id, type: 'text', autocomplete: 'off', spellcheck: 'false', inputmode: /^\d+$/.test(f.accept[0]) ? 'numeric' : undefined});
 input.value = ans[f.id] || '';
 input.addEventListener(f.options ? 'change' : 'input', () => { (state.answers[key] ||= {})[f.id] = input.value; delete state.marked[key]; save(); input.classList.remove('good', 'try'); result(key, '', true); updateScores(q); });
 return el('label', {class: 'field', for: id}, el('span', {text: f.label}), input);
}
function renderFields(q, p, key) {
 const ans = state.answers[key] || {};
 return el('div', {class: 'fields' + (p.grid ? ' grid' + p.grid : '')}, p.fields.map(f => fieldInput(q, p, key, f, ans)));
}
function renderTruth(q, p, key) {
 const ans = state.answers[key] || {};
 const head = el('tr', {}, ['A', 'B', 'C', ...p.columns].map(h => el('th', {scope: 'col', text: h})));
 const body = truthRows(p).map((r, i) => el('tr', {}, [r.a, r.b, r.c].map(v => el('td', {class: 'given', text: v})), p.columns.map((c, j) => {
  const k = i + '-' + j, s = el('select', {id: 't-' + key + '-' + k, 'aria-label': `${c} when A=${r.a} B=${r.b} C=${r.c}`}, el('option', {value: '', text: '–'}), el('option', {value: '0', text: '0'}), el('option', {value: '1', text: '1'}));
  s.value = ans[k] || '';
  s.addEventListener('change', () => { (state.answers[key] ||= {})[k] = s.value; delete state.marked[key]; save(); s.classList.remove('good', 'try'); result(key, '', true); updateScores(q); });
  return el('td', {}, s);
 })));
 return el('div', {class: 'scroll'}, el('table', {class: 'truth'}, el('thead', {}, head), el('tbody', {}, body)));
}
function renderOrder(q, p, key) {
 const ans = state.answers[key] || {};
 // shuffled but stable display order
 const hash = t => [...t].reduce((h, c) => (h * 31 + c.charCodeAt(0)) >>> 0, 7) % 9973;
 let shown = [...p.steps].sort((x, y) => hash(key + x.id) - hash(key + y.id));
 if (shown.every((s, i) => s.id === (p.base.includes(s.id) ? p.steps[i].id : s.id))) shown = shown.reverse();
 return el('ol', {class: 'order'}, shown.map(s => {
  const sel = el('select', {id: 's-' + key + '-' + s.id, 'aria-label': 'Position of: ' + s.text}, el('option', {value: '', text: '#'}), p.steps.map((_, i) => el('option', {value: String(i + 1), text: String(i + 1)})));
  sel.value = ans[s.id] || '';
  sel.addEventListener('change', () => { (state.answers[key] ||= {})[s.id] = sel.value ? Number(sel.value) : ''; delete state.marked[key]; save(); result(key, '', true); updateScores(q); });
  return el('li', {}, sel, el('span', {text: ' ' + s.text}));
 }));
}
function showMarks(q, p, key, announce) {
 const m = MARKERS[p.type](p, state.answers[key]);
 if (p.type === 'fields') for (const f of p.fields) { const i = $('f-' + key + '-' + f.id); if (i) { i.classList.toggle('good', m.ok[f.id]); i.classList.toggle('try', !m.ok[f.id]); } }
 if (p.type === 'truth') for (const [k, good] of Object.entries(m.ok)) { const s = $('t-' + key + '-' + k); if (s) { s.classList.toggle('good', good); s.classList.toggle('try', !good); } }
 const full = m.score === p.marks;
 let text = `${m.score} / ${p.marks}. ` + (m.note || (p.type === 'choice' ? (full ? 'Correct. ' : 'Not this one — think again, then check. ') + (full ? p.feedback || '' : '') : full ? 'All correct.' : 'Items marked in orange need another look.'));
 if (announce) result(key, text, full);
 return m.score;
}
// Extended answers are marked by level, so the student plans, writes, then judges the level.
const LEVELS = [
 {n: 1, text: 'Makes some relevant points, but few are explained. Little or no link to the scenario. Any conclusion is not supported.'},
 {n: 2, text: 'Explains several relevant points with some links to the scenario. Looks at more than one side, but not evenly. Gives a conclusion with some support.'},
 {n: 3, text: 'Develops a range of relevant points in detail, applied to the scenario throughout. Weighs up both sides and reaches a clear conclusion that follows from the argument.'}
];
function bands(marks) { const w = marks / 3; return LEVELS.map((l, i) => ({...l, lo: Math.round(i * w) + 1, hi: Math.round((i + 1) * w)})); }
function words(t) { return (t.match(/[A-Za-z0-9’'-]+/g) || []).length; }
function renderEssay(q, p, key) {
 const ans = state.answers[key] && typeof state.answers[key] === 'object' ? state.answers[key] : {};
 const put = (k, v) => { const a = state.answers[key] && typeof state.answers[key] === 'object' ? state.answers[key] : (state.answers[key] = {}); a[k] = v; save(); };
 const plan = el('details', {class: 'plan', open: !ans.text}, el('summary', {text: 'Plan first (2–3 minutes)'}),
  el('div', {class: 'planGrid'}, p.plan.map((h, i) => { const ta = el('textarea', {rows: 3, id: `pl-${key}-${i}`, placeholder: h.hint}); ta.value = ans['plan' + i] || ''; ta.addEventListener('input', () => put('plan' + i, ta.value)); return el('label', {class: 'field', for: ta.id}, el('span', {text: h.label}), ta); })));
 const ta = el('textarea', {id: 'a-' + key, rows: 14, placeholder: 'Write your answer in paragraphs. Each paragraph: make a point, explain it, apply it to the scenario, then link it to the question.', 'aria-label': 'Answer ' + label(p)});
 ta.value = ans.text || '';
 const count = el('p', {class: 'small wc'});
 const target = p.marks * 25;
 const check = el('details', {class: 'check'});
 const summary = el('summary');
 const list = el('ul', {class: 'criteria'});
 p.criteria.forEach((c, i) => {
  const cb = el('input', {type: 'checkbox', id: 'c-' + key + '-' + i});
  cb.checked = !!(state.ticks[key] || [])[i];
  cb.addEventListener('change', () => { (state.ticks[key] ||= [])[i] = cb.checked; save(); });
  list.append(el('li', {}, cb, el('label', {for: cb.id, text: ' ' + c})));
 });
 const sel = el('select', {id: 'lv-' + key}, el('option', {value: '', text: 'Choose a mark…'}), el('option', {value: '0', text: '0 — nothing relevant yet'}),
  bands(p.marks).map(b => el('optgroup', {label: 'Level ' + b.n}, Array.from({length: b.hi - b.lo + 1}, (_, i) => el('option', {value: String(b.lo + i), text: `${b.lo + i} (level ${b.n})`})))));
 sel.value = state.marked[key] !== undefined ? String(state.marked[key]) : '';
 sel.addEventListener('change', () => { if (sel.value === '') delete state.marked[key]; else state.marked[key] = Number(sel.value); save(); updateScores(q); });
 check.append(summary,
  el('p', {class: 'small', text: '1. Tick the points your answer develops (explained and applied, not just mentioned). You do not need them all: a top answer covers a good range in depth.'}), list,
  el('p', {class: 'small', text: '2. Decide which level best describes your answer as a whole, then choose a mark in that level: higher if it fits the level well, lower if it only just fits.'}),
  el('table', {class: 'levels'}, el('tbody', {}, bands(p.marks).map(b => el('tr', {}, el('th', {scope: 'row', text: `Level ${b.n} (${b.lo}–${b.hi})`}), el('td', {text: b.text}))))),
  el('label', {class: 'field', for: sel.id}, el('span', {text: 'My mark'}), sel));
 const refresh = () => {
  const n = words(ta.value), ready = n >= Math.min(60, target / 2);
  count.textContent = `${n} words · a strong ${p.marks}-mark answer is often around ${target}–${target + 100} words, but depth matters more than length.`;
  check.classList.toggle('locked', !ready); if (!ready) check.open = false;
  summary.textContent = ready ? 'Check and mark my answer' : `Check and mark my answer (write at least ${Math.min(60, target / 2)} words first)`;
 };
 check.addEventListener('toggle', () => { if (check.open && check.classList.contains('locked')) check.open = false; });
 ta.addEventListener('input', () => { put('text', ta.value); refresh(); });
 refresh();
 return el('div', {}, p.structure ? el('p', {class: 'hint'}, el('strong', {text: 'Structure: '}), p.structure) : null, plan, ta, count, check);
}

function renderPart(q, p, guided) {
 const key = pid(q, p);
 const kinds = {text: renderText, choice: renderChoice, fields: renderFields, truth: renderTruth, order: renderOrder, essay: renderEssay};
 const auto = p.type !== 'text' && p.type !== 'essay';
 const checkBtn = auto ? el('button', {type: 'button', text: 'Check', onclick: () => { state.marked[key] = showMarks(q, p, key, true); save(); updateScores(q); }}) : null;
 const node = el('div', {class: 'part', id: 'p-' + key},
  el('div', {class: 'phead'}, el('h4', {text: label(p)}), el('span', {class: 'marks', text: p.marks + (p.marks === 1 ? ' mark' : ' marks') + (auto ? ' · auto-marked' : p.type === 'essay' ? ' · level-marked' : ' · self-check')})),
  p.context ? el('p', {class: 'context', text: p.context}) : null,
  el('p', {class: 'prompt', text: p.prompt}),
  hintBox(p, guided),
  kinds[p.type](q, p, key, guided),
  auto ? el('div', {class: 'tools'}, checkBtn, el('span', {id: 'r-' + key, class: 'result', role: 'status'})) : null,
  links(p));
 return node;
}
function diagram() {
 return el('figure', {class: 'diagram', 'aria-label': 'Diagram: boxes P, Q and Memory. Clock joined to box Q. Control bus above; address bus and data bus below.'}, (() => {
  const d = document.createElement('div');
  d.innerHTML = `<svg viewBox="0 0 420 200" role="img" aria-hidden="true" style="max-width:520px;width:100%"><g fill="none" stroke="currentColor" stroke-width="2"><line x1="20" y1="30" x2="400" y2="30"/><line x1="20" y1="150" x2="400" y2="150"/><line x1="20" y1="180" x2="400" y2="180"/><rect x="30" y="70" width="90" height="45"/><rect x="170" y="70" width="90" height="45"/><rect x="300" y="70" width="90" height="45"/><rect x="115" y="45" width="45" height="20"/><line x1="160" y1="55" x2="170" y2="80"/><line x1="215" y1="30" x2="215" y2="70"/><line x1="345" y1="30" x2="345" y2="70"/><line x1="75" y1="30" x2="75" y2="70"/><line x1="75" y1="115" x2="75" y2="180"/><line x1="215" y1="115" x2="215" y2="180"/><line x1="345" y1="115" x2="345" y2="180"/></g><g fill="currentColor" font-family="system-ui" font-size="14" text-anchor="middle"><text x="75" y="97">P</text><text x="215" y="97">Q</text><text x="345" y="97">Memory</text><text x="137" y="59" font-size="11">Clock</text><text x="210" y="22">Control bus</text><text x="145" y="144">Address bus</text><text x="145" y="197">Data bus</text></g></svg>`;
  return d.firstChild;
 })(), el('figcaption', {text: 'Figure: a simple computer system. Decide the bus directions in part (a).'}));
}
function renderTable(t) {
 return el('div', {class: 'scroll'}, el('table', {class: 'data'}, el('thead', {}, el('tr', {}, t.head.map(h => el('th', {scope: 'col', text: h})))), el('tbody', {}, t.rows.map(r => el('tr', {}, r.map(c => el('td', {text: c})))))));
}
function renderTest(t) {
 const wrap = $('test'); wrap.replaceChildren();
 const sumMax = t.questions.reduce((n, q) => n + q.parts.reduce((m, p) => m + p.marks, 0), 0);
 wrap.append(el('div', {class: 'intro'}, el('h2', {text: t.title}), el('p', {text: t.intro}), t.guide ? el('dl', {class: 'guide'}, t.guide.flatMap(g => [el("dt", {text: g.term}), el("dd", {text: g.text})])) : null, el('p', {class: 'total', id: 'testTotal', text: ''}), el('p', {class: 'small', text: `Total: ${sumMax} marks. Written answers are self-checked: tick only what your answer really says. Auto-marked answers are checked when you press Check.`})));
 t.questions.forEach((q, i) => {
  const qm = q.parts.reduce((m, p) => m + p.marks, 0);
  wrap.append(el('section', {class: 'question', id: q.id},
   el('h3', {text: `Question ${i + 1}: ${q.title}`}),
   el('p', {class: 'scenario', text: q.scenario}),
   q.diagram ? diagram() : null,
   q.table ? renderTable(q.table) : null,
   q.parts.map(p => renderPart(q, p, t.guided)),
   el('p', {class: 'qtotal', id: 'qt-' + q.id, text: `Total for question ${i + 1}: ${qm} marks`})));
 });
 for (const q of t.questions) { for (const p of q.parts) if (MARKERS[p.type] && state.marked[pid(q, p)] !== undefined) state.marked[pid(q, p)] = showMarks(q, p, pid(q, p), true); updateScores(q); }
}
function updateScores(q) {
 const t = TESTS.find(t => t.id === current);
 if (q && $('qt-' + q.id)) { const s = questionScore(q); $('qt-' + q.id).textContent = `Your score so far: ${s.total} / ${s.max}` + (s.autoMax && s.selfMax ? ` (auto-marked ${s.auto}/${s.autoMax}, self-checked ${s.self}/${s.selfMax})` : s.selfMax ? ' (self-checked)' : ' (auto-marked)'); }
 let total = 0, max = 0; for (const qq of t.questions) { const s = questionScore(qq); total += s.total; max += s.max; }
 if ($('testTotal')) $('testTotal').textContent = `Score so far: ${total} / ${max}`;
}
function showTest(id) {
 current = id;
 for (const b of $('tabs').children) { const on = b.dataset.test === id; b.classList.toggle('current', on); b.setAttribute('aria-pressed', String(on)); }
 renderTest(TESTS.find(t => t.id === id));
 try { history.replaceState(null, '', '#' + id); } catch {}
}

// ---------- backup ----------
function download() {
 save();
 const url = URL.createObjectURL(new Blob([JSON.stringify({format: FORMAT, ...state}, null, 2)], {type: 'application/json'}));
 const a = el('a', {href: url, download: 'my-computing-revision.json'}); a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
}
$('download').onclick = download;
$('restore').onclick = () => $('backup').click();
$('backup').onchange = async e => {
 try {
  const file = e.target.files[0]; if (!file) return;
  if (file.size > 500000) throw Error('That backup is too large.');
  const data = JSON.parse(await file.text());
  if (data.format !== FORMAT) throw Error(data.format === 'unit2-workbook-v1' ? 'That is a workbook backup. Restore it on the workbook page.' : 'Choose a backup from this revision page.');
  const incoming = validState(data);
  if (!confirm('This replaces the revision answers on this device with the backup. Continue?')) return;
  state = incoming; save(); showTest(current); status('Backup restored.');
 } catch (err) { status(err.message || 'That file could not be read.', true); } finally { $('backup').value = ''; }
};
$('clear').onclick = () => {
 if (!confirm('Clear every revision answer saved in this browser? Download your revision first if you want to keep it.')) return;
 try { localStorage.removeItem(KEY); } catch { status('Could not clear browser storage. Use the browser’s site-data settings.', true); return; }
 state = {answers: {}, ticks: {}, marked: {}}; showTest(current); saved = true; status('Revision cleared from this browser. Your downloaded files are unchanged.');
};
$('print').onclick = () => window.print();
window.addEventListener('beforeunload', e => { if (!saved) { e.preventDefault(); e.returnValue = ''; } });
window.addEventListener('storage', e => { if (e.key === KEY) status('Revision changed in another tab. Use one revision tab at a time.', true); });

// ---------- start ----------
let loadError = false;
try { state = validState(JSON.parse(localStorage.getItem(KEY) || '{}')); } catch { loadError = true; }
for (const t of TESTS) $('tabs').append(el('button', {type: 'button', 'data-test': t.id, text: t.short, onclick: () => showTest(t.id)}));
showTest(TESTS.some(t => '#' + t.id === location.hash) ? location.hash.slice(1) : TESTS[0].id);
status(loadError ? 'Saved revision could not load. Keep any backup safe.' : 'Ready. Answers save on this device as you type.', loadError);
})();
