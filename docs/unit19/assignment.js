'use strict';
(async () => {
const KEY = 'unit19-assignment-v1', FORMAT = 'unit19-assignment-v1';
const $ = id => document.getElementById(id);
let data, tasks = [], current, saved = true;
let state = {checks: {}, plan: {}, draft: {}, tables: {}, ailog: []};
const chats = {};

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
function status(m, err = false) { $('status').textContent = m; $('status').className = err ? 'error' : ''; }
function save() {
 try { localStorage.setItem(KEY, JSON.stringify(state)); saved = true; status('Saved on this device. Download a backup before changing computers.'); }
 catch { saved = false; status('Browser saving is unavailable. Download your work before closing.', true); }
}
const words = t => (String(t || '').match(/[A-Za-z0-9’'-]+/g) || []).length;

// ---------- planning tables ----------
const SCHEMAS = {
 components: {title: 'Component table (A.P2)', cols: ['Component', 'Function (what it does)', 'Characteristics (what you compare)', 'Example'], prefill: ['End user devices (incl. mobile)', 'Switch', 'Router', 'Access point', 'Copper cable', 'Wireless', 'Fibre optic', 'Networking systems software', 'Monitoring / management / troubleshooting tools', 'Network applications']},
 inventory: {title: 'Equipment inventory', cols: ['Item', 'Qty', 'Model / specification', 'Where it goes', 'Why this choice', 'Cost (£)']},
 ipplan: {title: 'IP addressing plan', cols: ['Site / network', 'Network address', 'Mask / prefix', 'Default gateway', 'Static range (servers, printers, devices)', 'DHCP range', 'VLAN']},
 naming: {title: 'Naming scheme', cols: ['Device', 'Name', 'Location', 'IP address']},
 access: {title: 'Users, groups and permissions', cols: ['User', 'Group', 'Folder', 'Owner permissions', 'Group permissions', 'Others permissions', 'Linux number']},
 testplan: {title: 'Test plan and results', cols: ['No.', 'What is tested', 'How (method / command)', 'Expected result', 'Actual result', 'Pass / fail', 'Evidence ref.', 'Action taken'], select: {5: ['', 'Pass', 'Fail', 'Pass after fix']}},
 evaluation: {title: 'Evaluation grid', cols: ['Requirement', 'Met?', 'Evidence (which test / screenshot)', 'Strengths', 'Limitations', 'Future improvement'], select: {1: ['', 'Fully', 'Partly', 'Not met']}},
 targets: {title: 'Plan: targets and deadlines', cols: ['Target', 'Deadline', 'Done?', 'Notes'], select: {2: ['', 'Not started', 'In progress', 'Done']}},
 diary: {title: 'Diary / log', cols: ['Date', 'What I did', 'Problems and how I solved them', 'Next step']},
 feedback: {title: 'Feedback log', cols: ['Date', 'Who gave feedback', 'Their feedback', 'What I changed as a result']}
};
const TOOLS = {table: ['components'], design: ['inventory', 'ipplan', 'naming', 'access'], testplan: ['testplan'], evaluation: ['evaluation'], diary: ['targets', 'diary', 'feedback'], notes: []};

function tableRows(tid, schema, task) {
 const key = task.id + ':' + tid;
 if (!state.tables[key]) {
  let rows;
  if (schema.prefill) rows = schema.prefill.map(p => [p, ...Array(schema.cols.length - 1).fill('')]);
  else if (tid === 'evaluation') rows = (assignmentOf(task).requirements || []).map(r => [r, ...Array(schema.cols.length - 1).fill('')]);
  else rows = [Array(schema.cols.length).fill(''), Array(schema.cols.length).fill('')];
  state.tables[key] = rows;
 }
 return state.tables[key];
}
function renderTable(task, tid) {
 const schema = SCHEMAS[tid], key = task.id + ':' + tid;
 const rows = tableRows(tid, schema, task);
 const tbody = el('tbody');
 const draw = () => {
  tbody.replaceChildren(...rows.map((row, r) => el('tr', {}, schema.cols.map((c, ci) => {
   const opts = schema.select && schema.select[ci];
   const input = opts ? el('select', {'aria-label': `${c}, row ${r + 1}`}, opts.map(o => el('option', {value: o, text: o || 'choose'}))) : el('input', {type: 'text', 'aria-label': `${c}, row ${r + 1}`, maxlength: 600});
   input.value = row[ci] || '';
   input.addEventListener(opts ? 'change' : 'input', () => { row[ci] = input.value; save(); });
   return el('td', {}, input);
  }), el('td', {class: 'del'}, el('button', {type: 'button', title: 'Delete row', 'aria-label': `Delete row ${r + 1}`, text: '×', onclick: () => { rows.splice(r, 1); save(); draw(); }})))));
 };
 draw();
 const csv = () => {
  const q = v => '"' + String(v ?? '').replace(/"/g, '""') + '"';
  const text = [schema.cols.map(q).join(','), ...rows.map(r => r.map(q).join(','))].join('\r\n');
  const url = URL.createObjectURL(new Blob([text], {type: 'text/csv'}));
  const a = el('a', {href: url, download: `${task.id}-${tid}.csv`}); a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
 };
 return el('section', {class: 'card'}, el('h3', {text: schema.title}),
  el('div', {class: 'tablewrap'}, el('table', {class: 'grid-table'}, el('thead', {}, el('tr', {}, schema.cols.map(c => el('th', {scope: 'col', text: c})), el('th', {text: ''}))), tbody)),
  el('div', {class: 'tools noprint'}, el('button', {type: 'button', text: '+ Add row', onclick: () => { rows.push(Array(schema.cols.length).fill('')); save(); draw(); }}), el('button', {type: 'button', text: 'Download as CSV (opens in Excel)', onclick: csv})));
}

// ---------- coach ----------
const MODES = [['task-explain', 'Explain this task'], ['task-plan', 'Help me plan'], ['task-review', 'Review my draft'], ['task-accuracy', 'Check my technical accuracy']];
function logAI(task, mode, question, reply) {
 state.ailog.push({when: new Date().toISOString(), task: task.id, criteria: task.criteria, mode, question: question.slice(0, 500), reply: String(reply).slice(0, 700)});
 if (state.ailog.length > 400) state.ailog = state.ailog.slice(-400);
 save(); renderLog();
}
async function ask(task, mode, box) {
 const log = box.querySelector('.coachlog'), input = box.querySelector('input'), buttons = box.querySelectorAll('button');
 const note = input.value.trim(), draft = (state.draft[task.id] || '').trim(), plan = (state.plan[task.id] || '').trim();
 if ((mode === 'task-review' || mode === 'task-accuracy') && words(draft) < 30) { log.append(el('p', {class: 'bot', text: 'Write at least a few sentences of your own draft first (30+ words), then ask for a review.'})); return; }
 if (!window.TUTOR_API_URL) { log.append(el('p', {class: 'bot', text: 'The AI coach is not connected yet. Use the checklist to review your own work for now.'})); return; }
 const parts = [];
 if (mode === 'task-plan' && plan) parts.push('My plan so far:\n' + plan);
 if (mode === 'task-review' || mode === 'task-accuracy') parts.push('My draft:\n' + draft);
 parts.push(note || {'task-explain': 'Please explain what this task is asking me to do.', 'task-plan': 'Please help me plan this task.', 'task-review': 'Please review my draft against the checklist.', 'task-accuracy': 'Please check the technical accuracy of my draft.'}[mode]);
 const message = parts.join('\n\n').slice(0, 6000);
 const history = chats[task.id] ||= [];
 buttons.forEach(b => b.disabled = true);
 const label = note || MODES.find(m => m[0] === mode)[1];
 const thinking = el('p', {class: 'bot', text: 'Thinking…'});
 log.append(el('p', {class: 'you', text: 'You: ' + label}), thinking);
 try {
  const r = await fetch(window.TUTOR_API_URL, {method: 'POST', credentials: 'omit', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({course: 'u19', task: task.id, mode, message, history: history.slice(-6)}), signal: AbortSignal.timeout(60000)});
  const d = await r.json();
  if (!r.ok) throw Error(d.error || 'The coach is unavailable.');
  thinking.textContent = d.reply;
  history.push({role: 'user', content: message}, {role: 'assistant', content: d.reply}); chats[task.id] = history.slice(-6);
  input.value = '';
  logAI(task, label, message, d.reply);
 } catch (e) {
  thinking.textContent = e.name === 'TimeoutError' ? 'The coach took too long. Please try again.' : e instanceof TypeError || e instanceof SyntaxError ? 'The coach is offline or busy at the moment. Keep working with the checklist and try again later.' : e.message;
 } finally { buttons.forEach(b => b.disabled = false); }
}
function renderLog() {
 const list = $('ailogList');
 list.replaceChildren(...(state.ailog.length ? state.ailog.map(x => el('li', {}, el('strong', {text: `${new Date(x.when).toLocaleString()} · ${x.criteria} · ${x.mode}: `}), x.question.split('\n').pop().slice(0, 160))) : [el('li', {text: 'No coach questions yet.'})]));
}
$('downloadLog').onclick = () => {
 const lines = ['UNIT 19 AI-USE LOG', 'Generated ' + new Date().toLocaleString(), 'This log lists every question I asked the course AI assignment coach and a short extract of its reply.', ''];
 for (const x of state.ailog) lines.push(`[${new Date(x.when).toLocaleString()}] Task ${x.task} (${x.criteria}) · ${x.mode}`, 'I asked: ' + x.question.replace(/\s+/g, ' ').slice(0, 500), 'Coach replied (extract): ' + x.reply.replace(/\s+/g, ' ').slice(0, 500), '');
 const url = URL.createObjectURL(new Blob([lines.join('\n')], {type: 'text/plain'}));
 const a = el('a', {href: url, download: 'unit19-ai-use-log.txt'}); a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
};

// ---------- task page ----------
const assignmentOf = t => data.assignments.find(a => a.tasks.includes(t));
function progress(task) { const c = state.checks[task.id] || []; return `${c.filter(Boolean).length}/${task.checklist.length}`; }
function renderList() {
 $('tasklist').replaceChildren(...data.assignments.flatMap(a => [el('h3', {text: a.title.split(':')[0]}), ...a.tasks.map(t => el('button', {type: 'button', 'data-task': t.id, class: t === current ? 'current' : '', onclick: () => show(t.id)}, el('span', {class: 'prog', text: progress(t)}), `${t.criteria} · ${t.title.split(':')[0].slice(0, 44)}`))]));
}
function show(id) {
 current = tasks.find(t => t.id === id) || tasks[0];
 const t = current, a = assignmentOf(t);
 const checks = state.checks[t.id] ||= [];
 const list = el('ul', {class: 'checklist'}, t.checklist.map((c, i) => {
  const cb = el('input', {type: 'checkbox', id: `c-${t.id}-${i}`}); cb.checked = !!checks[i];
  cb.addEventListener('change', () => { checks[i] = cb.checked; save(); renderList(); });
  return el('li', {}, cb, el('label', {for: cb.id, text: c}));
 }));
 const planTa = el('textarea', {rows: 6, maxlength: 20000, placeholder: 'Headings, bullet points, ideas, sources to check. This is for you.', 'aria-label': 'My plan'});
 planTa.value = state.plan[t.id] || '';
 planTa.addEventListener('input', () => { state.plan[t.id] = planTa.value; save(); });
 const draftTa = el('textarea', {rows: 14, maxlength: 40000, placeholder: 'Write your own draft here, or paste a section from your document to get feedback on it.', 'aria-label': 'My draft'});
 draftTa.value = state.draft[t.id] || '';
 const wc = el('p', {class: 'wc'});
 const upd = () => wc.textContent = `${words(draftTa.value)} words`;
 draftTa.addEventListener('input', () => { state.draft[t.id] = draftTa.value; save(); upd(); }); upd();
 const coach = el('div', {class: 'coach'}, el('h3', {text: 'AI assignment coach'}),
  el('p', {class: 'small', text: 'Explains the task, helps you plan, and gives feedback on your own draft against the checklist. It will not write your work. Questions are saved to your AI-use log.'}),
  el('div', {class: 'modes'}, MODES.map(([m, lab]) => el('button', {type: 'button', text: lab, onclick: () => ask(t, m, coach)}))),
  el('input', {type: 'text', maxlength: 600, placeholder: 'Optional: ask the coach something specific about this task', 'aria-label': 'Question for the coach', style: 'margin-top:10px'}),
  el('div', {class: 'coachlog', role: 'log', 'aria-live': 'polite'}));
 $('task').replaceChildren(
  el('section', {class: 'card', id: t.id}, el('p', {class: 'small', text: a.title}), el('h2', {}, el('span', {class: 'badge', text: t.criteria}), ' ', t.title),
   el('p', {text: t.asks}), el('p', {class: 'small'}, 'Revise: ', t.lessons.flatMap((l, i) => [i ? ', ' : '', el('a', {href: 'learning.html#' + l, text: 'lesson ' + l})])),
   el('h3', {text: 'Success checklist'}), el('p', {class: 'small', text: 'Tick each point only when your work really does it.'}), list),
  ...(TOOLS[t.tool] || []).map(tid => renderTable(t, tid)),
  el('section', {class: 'card'}, el('h3', {text: 'My plan'}), planTa, el('h3', {text: 'My draft'}), draftTa, wc,
   el('p', {class: 'small', text: 'Tip: write your final version in Word or your teacher’s template. Paste a section here when you want feedback.'})),
  coach);
 renderList();
 try { history.replaceState(null, '', '#' + t.id); } catch {}
}

// ---------- backup ----------
function validState(v) {
 if (!v || typeof v !== 'object' || Array.isArray(v)) throw Error('Invalid backup.');
 const out = {checks: {}, plan: {}, draft: {}, tables: {}, ailog: []};
 const okId = id => tasks.some(t => t.id === id);
 for (const [id, c] of Object.entries(v.checks || {})) if (okId(id) && Array.isArray(c)) out.checks[id] = c.map(Boolean).slice(0, 20);
 for (const k of ['plan', 'draft']) for (const [id, s] of Object.entries(v[k] || {})) if (okId(id) && typeof s === 'string') out[k][id] = s.slice(0, 40000);
 for (const [key, rows] of Object.entries(v.tables || {})) { const [id, tid] = key.split(':'); if (okId(id) && SCHEMAS[tid] && Array.isArray(rows)) out.tables[key] = rows.slice(0, 200).map(r => Array.isArray(r) ? r.slice(0, 10).map(x => String(x ?? '').slice(0, 600)) : []); }
 if (Array.isArray(v.ailog)) out.ailog = v.ailog.slice(-400).filter(x => x && typeof x === 'object').map(x => ({when: String(x.when || ''), task: String(x.task || ''), criteria: String(x.criteria || ''), mode: String(x.mode || ''), question: String(x.question || '').slice(0, 500), reply: String(x.reply || '').slice(0, 700)}));
 return out;
}
$('download').onclick = () => {
 save();
 const url = URL.createObjectURL(new Blob([JSON.stringify({format: FORMAT, ...state}, null, 2)], {type: 'application/json'}));
 const a = el('a', {href: url, download: 'my-unit19-assignment-work.json'}); a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
};
$('restore').onclick = () => $('backup').click();
$('backup').onchange = async e => {
 try {
  const f = e.target.files[0]; if (!f) return;
  if (f.size > 3000000) throw Error('That backup is too large.');
  const d = JSON.parse(await f.text());
  if (d.format !== FORMAT) throw Error('Choose a backup from the Unit 19 Assignment builder.');
  const incoming = validState(d);
  if (!confirm('This replaces the assignment work on this device with the backup. Continue?')) return;
  state = incoming; save(); show(current.id); renderLog(); status('Backup restored.');
 } catch (err) { status(err.message || 'That file could not be read.', true); } finally { $('backup').value = ''; }
};
$('clear').onclick = () => {
 if (!confirm('Clear all assignment work and the AI-use log from this browser? Download a backup first if you want to keep it.')) return;
 try { localStorage.removeItem(KEY); } catch { status('Could not clear browser storage.', true); return; }
 state = {checks: {}, plan: {}, draft: {}, tables: {}, ailog: []}; show(current.id); renderLog(); saved = true; status('Cleared from this browser.');
};
$('print').onclick = () => window.print();
window.addEventListener('beforeunload', e => { if (!saved) { e.preventDefault(); e.returnValue = ''; } });
window.addEventListener('hashchange', () => { const id = location.hash.slice(1); if (data && current && id !== current.id && tasks.some(t => t.id === id)) show(id); });

// ---------- start ----------
try { data = await (await fetch('assignments.json')).json(); } catch { status('The assignment tasks could not load. Refresh the page.', true); return; }
tasks = data.assignments.flatMap(a => a.tasks);
let bad = false;
try { state = validState(JSON.parse(localStorage.getItem(KEY) || '{}')); } catch { bad = true; }
show(location.hash.slice(1));
renderLog();
status(bad ? 'Saved work could not load. Keep any backup safe.' : 'Ready. Your work saves on this device as you type.', bad);
})();
