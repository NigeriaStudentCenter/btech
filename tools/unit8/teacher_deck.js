// Unit 8 Security: teacher delivery deck (original content).
// Figures are PNG exports of the Learn page diagrams: set FIGS to their folder (with dims.json).
const pptxgen = require('pptxgenjs');
const path = require('path');
const FIGS = process.env.FIGS || path.join(__dirname, 'figs');
const DIMS = require(path.join(FIGS, 'dims.json'));
const FIG = n => path.join(FIGS, n + '.png');

const C = {navy: '1F2340', teal: 'B03A2E', amber: 'E0A33D', ink: '17334B', muted: '4F6577', tint: 'EAF2F9', mint: 'E6F4EE', white: 'FFFFFF', line: 'C9D7E3', sand: 'FDF1E7'};
const HEAD = 'Cambria', BODY = 'Calibri';
const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.333 x 7.5
pres.author = 'Unit 8 course team';
pres.title = 'Unit 8 Security: teacher delivery deck';
const W = 13.333, H = 7.5, M = 0.6;
const SITE = 'nigeriastudentcenter.github.io/btech/unit8/start.html';

function fitH(name, maxW) { const [w, h] = DIMS[name]; return maxW * h / w; }
function img(slide, name, x, y, maxW, maxH) {
 if (!DIMS[name]) throw Error('Unknown figure ' + name);
 const [w, h] = DIMS[name];
 let iw = maxW, ih = maxW * h / w;
 if (ih > maxH) { ih = maxH; iw = maxH * w / h; }
 slide.addImage({path: FIG(name), x: x + (maxW - iw) / 2, y, w: iw, h: ih});
 return ih;
}
function title(slide, text, opts = {}) {
 slide.addText(text, {x: opts.x ?? M, y: opts.y ?? 0.45, w: opts.w ?? W - 2 * M, h: 0.8, fontFace: HEAD, fontSize: opts.size ?? 32, bold: true, color: opts.color ?? C.ink, margin: 0, isTextBox: true, valign: 'middle'});
}
function chip(slide, code, x = M, y = 0.18) {
 slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y, w: 1.3, h: 0.34, fill: {color: C.teal}, line: {color: C.teal}, rectRadius: 0.08});
 slide.addText(code, {x, y, w: 1.3, h: 0.34, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 12, bold: true, color: C.white, margin: 0, isTextBox: true});
}
function bullets(slide, items, x, y, w, h, size = 16, color = C.ink) {
 slide.addText(items.map((t, i) => ({text: t, options: {bullet: true, breakLine: i < items.length - 1, paraSpaceAfter: 6}})), {x, y, w, h, fontFace: BODY, fontSize: size, color, valign: 'top', margin: 0.05, isTextBox: true});
}
function card(slide, x, y, w, h, head, body, fill = C.tint, headColor = C.navy, size = 13) {
 slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y, w, h, fill: {color: fill}, line: {color: fill}, rectRadius: 0.1});
 slide.addText([{text: head, options: {bold: true, color: headColor, fontSize: size + 2, breakLine: true}}, {text: body, options: {color: C.ink, fontSize: size}}], {x: x + 0.18, y: y + 0.12, w: w - 0.36, h: h - 0.24, fontFace: BODY, valign: 'top', margin: 0, isTextBox: true, paraSpaceAfter: 4});
}
function footer(slide, text) {
 slide.addText(text, {x: M, y: H - 0.42, w: W - 2 * M, h: 0.3, fontFace: BODY, fontSize: 10, color: C.muted, margin: 0, isTextBox: true});
}
function lessonFlow(slide, parts, y) {
 const w = (W - 2 * M - 0.3 * (parts.length - 1)) / parts.length;
 parts.forEach(([h, b], i) => card(slide, M + i * (w + 0.3), y, w, 1.35, h, b, [C.tint, C.mint, C.sand][i % 3], C.navy, 12));
}
function table(slide, head, rows, opts) {
 const hdr = head.map(t => ({text: t, options: {bold: true, color: C.white, fill: {color: C.navy}}}));
 slide.addTable([hdr, ...rows.map(r => r.map(t => ({text: t})))], Object.assign({fontFace: BODY, fontSize: 13, color: C.ink, border: {type: 'solid', pt: 1, color: C.line}, fill: {color: C.white}, margin: 0.06, valign: 'top'}, opts));
}
const notes = (slide, lines) => slide.addNotes(lines.join('\n'));

function divider(label, sub) {
 const s = pres.addSlide(); s.background = {color: C.navy};
 s.addText(label, {x: M, y: 2.3, w: W - 2 * M, h: 1.2, fontFace: HEAD, fontSize: 44, bold: true, color: C.white, margin: 0, isTextBox: true});
 s.addText(sub, {x: M, y: 3.6, w: W - 2 * M, h: 1.0, fontFace: BODY, fontSize: 20, color: 'CADCFC', margin: 0, isTextBox: true});
 return s;
}
function lessonWide(code, t, fig, aim, flow, n) {
 const s = pres.addSlide(); chip(s, code); title(s, t, {y: 0.55, size: 28});
 s.addText('Aim: ' + aim, {x: M, y: 1.3, w: W - 2 * M, h: 0.4, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 const ih = img(s, fig, M, 1.8, W - 2 * M, 3.45);
 lessonFlow(s, flow, 1.8 + ih + 0.2);
 notes(s, n); return s;
}
function lessonSplit(code, t, fig, aim, points, flow, n, fig2) {
 const s = pres.addSlide(); chip(s, code); title(s, t, {y: 0.55, size: 28});
 s.addText('Aim: ' + aim, {x: M, y: 1.3, w: 5.4, h: 0.6, fontFace: BODY, fontSize: 14, italic: true, color: C.muted, margin: 0, isTextBox: true, valign: 'top'});
 bullets(s, points, M, 1.95, 5.3, 3.4, 16);
 const h1 = img(s, fig, 6.25, 1.3, 6.48, fig2 ? 2.05 : 4.0);
 if (fig2) img(s, fig2, 6.25, 1.3 + h1 + 0.12, 6.48, 4.0 - h1 - 0.12);
 lessonFlow(s, flow, 5.55);
 notes(s, n); return s;
}

// 1 Title
{
 const s = pres.addSlide(); s.background = {color: C.navy};
 s.addText('Content area 8', {x: M, y: 1.2, w: 6, h: 0.6, fontFace: BODY, fontSize: 20, bold: true, color: C.amber, margin: 0, isTextBox: true});
 s.addText('Security', {x: M, y: 1.75, w: 6.4, h: 1.0, fontFace: HEAD, fontSize: 54, bold: true, color: C.white, margin: 0, isTextBox: true, valign: 'top'});
 s.addText('Teacher delivery deck · T Level Digital Production, Design and Development (core)', {x: M, y: 3.0, w: 6.2, h: 0.8, fontFace: BODY, fontSize: 18, color: 'CADCFC', margin: 0, isTextBox: true, valign: 'top'});
 s.addText('Risks · Threats · Vulnerabilities · Mitigation · CIA · IAAA', {x: M, y: 4.0, w: 6.2, h: 0.5, fontFace: BODY, fontSize: 16, italic: true, color: C.white, margin: 0, isTextBox: true});
 const th = fitH('the_cia_triad', 5.6);
 s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 6.9, y: 3.2 - th / 2, w: 5.9, h: th + 0.3, fill: {color: C.white}, line: {color: C.white}, rectRadius: 0.15});
 img(s, 'the_cia_triad', 7.05, 3.35 - th / 2, 5.6, 4.5);
 notes(s, ['Purpose: this deck supports delivery of content area 8 alongside the student course site (' + SITE + ').', 'Every lesson slide follows the college routine: starter, aim, teach, practical, task, check, flipped homework.', 'Speaker notes give teaching points, questions, differentiation, and the matching workbook section, practical and quiz.']);
}

// 2 How each lesson runs
{
 const s = pres.addSlide(); title(s, 'How each lesson runs');
 const steps = [['Starter', 'real incident or recap quiz'], ['Aim', 'share the aim and the spec point'], ['Teach', 'diagram-led explanation with questioning'], ['Practical', 'lab task or scenario activity'], ['Task', 'workbook activity on the site'], ['Check', 'quiz or exam-style exit question'], ['Homework', 'flipped: preview the next lesson']];
 const w = (W - 2 * M - 0.15 * 6) / 7;
 steps.forEach(([h, b], i) => {
  const x = M + i * (w + 0.15);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y: 1.7, w, h: 2.2, fill: {color: i % 2 ? C.tint : C.sand}, line: {color: C.line}, rectRadius: 0.1});
  s.addShape(pres.shapes.OVAL, {x: x + w / 2 - 0.35, y: 1.9, w: 0.7, h: 0.7, fill: {color: C.navy}, line: {color: C.navy}});
  s.addText(String(i + 1), {x: x + w / 2 - 0.35, y: 1.9, w: 0.7, h: 0.7, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 18, bold: true, color: C.white, margin: 0, isTextBox: true});
  s.addText([{text: h, options: {bold: true, fontSize: 15, color: C.navy, breakLine: true}}, {text: b, options: {fontSize: 12, color: C.ink}}], {x: x + 0.1, y: 2.75, w: w - 0.2, h: 1.35, align: 'center', valign: 'top', fontFace: BODY, margin: 0, isTextBox: true});
 });
 card(s, M, 4.3, 6.0, 1.5, 'On the student site', 'Each lesson has a Learn page section with diagrams, a real case and exam tips, a workbook activity with the AI tutor, videos, a practical where relevant, and a quiz.');
 card(s, 6.9, 4.3, 5.83, 1.5, 'Start with a real incident', 'Security lands best with a current news story: a breach, a ransomware outage or a scam text. Ask: which information, which threat, which control?', C.sand);
 notes(s, ['Keep your existing starters and the 8.1 eLearning module on Teams.', 'End each lesson with a site quiz question or an exam-style exit question.']);
}

// 3 At a glance
{
 const s = pres.addSlide(); title(s, 'Content area 8 at a glance');
 const stats = [['4', 'topic areas: 8.1–8.4'], ['12', 'specification points'], ['15', 'lessons on the student site'], ['10', 'practical tasks'], ['1', 'written core exam']];
 const w = (W - 2 * M - 0.25 * 4) / 5;
 stats.forEach(([n, l], i) => {
  const x = M + i * (w + 0.25);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y: 1.6, w, h: 2.1, fill: {color: i === 4 ? C.navy : C.tint}, line: {color: i === 4 ? C.navy : C.tint}, rectRadius: 0.12});
  s.addText(n, {x, y: 1.75, w, h: 1.1, align: 'center', fontFace: HEAD, fontSize: 60, bold: true, color: i === 4 ? C.white : C.teal, margin: 0, isTextBox: true});
  s.addText(l, {x: x + 0.15, y: 2.85, w: w - 0.3, h: 0.7, align: 'center', fontFace: BODY, fontSize: 14, color: i === 4 ? C.white : C.ink, margin: 0, isTextBox: true});
 });
 const areas = [['8.1 Security risks', 'confidential information, reasons, impact'], ['8.2 Threats and vulnerabilities', 'technical, human and physical; impact'], ['8.3 Threat mitigation', 'techniques; firewalls, segregation, monitoring'], ['8.4 Effective security', 'CIA triad; IAAA model']];
 const w2 = (W - 2 * M - 0.25 * 3) / 4;
 areas.forEach(([h, b], i) => card(s, M + i * (w2 + 0.25), 4.1, w2, 1.9, h, b, [C.tint, C.sand, C.mint, C.tint][i], C.navy, 13));
 footer(s, '8.2.1 (technical threats) and 8.3.1 (mitigation techniques) are the two largest points: each is split across several lessons on the site.');
 notes(s, ['Content area 8 is part of the T Level core, assessed in the written examination (Paper 2 in the 2025–26 plan). Check current arrangements with the awarding organisation.', 'The specification repeatedly asks for impacts, prevention AND mitigation, and benefits AND drawbacks: build these pairs into every lesson.']);
}

// 4 Assessment
{
 const s = pres.addSlide(); title(s, 'How it is assessed: exam technique');
 table(s, ['Command word', 'What students must do', 'Typical marks'], [
  ['State / identify', 'short fact or name, e.g. a type of malware', '1'],
  ['Describe', 'features or steps; one mark per accurate point', '2–4'],
  ['Explain', 'point + why/how, applied to the scenario', '2–6'],
  ['Discuss', 'benefits, drawbacks and what it depends on', '6–9'],
  ['Evaluate / justify', 'weigh controls against risk and cost; supported judgement', '9–12']], {x: M, y: 1.45, w: 7.6, colW: [1.9, 4.6, 1.1]});
 card(s, 8.5, 1.45, 4.23, 2.35, 'The winning pattern', 'Threat → impact on THIS organisation → prevention → mitigation → drawback of the control. Name the business in every point.', C.mint, C.teal, 13);
 card(s, 8.5, 4.0, 4.23, 2.35, 'On the site', 'Exam practice has two scenario papers (a dental practice, an online shop, a hospital) with self-marking checklists and level descriptors.', C.sand, C.navy, 13);
 notes(s, ['Common weakness: listing controls without saying which threat each one stops.', 'Use official sample assessment materials for timed mocks; the site’s exam practice is original.']);
}

// 5 Student site
{
 const s = pres.addSlide(); title(s, 'The student course site');
 const pages = [['1. Course guide', 'Exam overview and a red/amber/green checklist of all 12 spec points'], ['2. Learn', '15 lessons with original diagrams, real cases and exam tips'], ['3. Workbook + tutor', 'An activity and quick check per lesson; AI study tutor; saves on device'], ['4. Practicals', '10 tasks: phishing, passwords, Diffie-Hellman, hashing, Linux, Nmap, firewall'], ['5. Exam practice', 'Scenario papers with command-word guide and level marking'], ['6. Quizzes', 'Five instant-marked quizzes, one per topic block']];
 pages.forEach(([h, b], i) => card(s, M + (i % 3) * 4.1, 1.5 + Math.floor(i / 3) * 2.35, 3.9, 2.1, h, b, i % 2 ? C.sand : C.tint, C.navy, 14));
 footer(s, 'Plus 7. Videos: 35 embedded videos (MrBrownCS, Computerphile, TED, Cisco, IBM). Link for Teams: ' + SITE);
 notes(s, ['Tour the site in the first lesson and show the RAG checklist.', 'Work saves in the browser only: remind students to download backups on shared PCs.']);
}

// 6 Ethics and the AI tutor
{
 const s = pres.addSlide(); title(s, 'Ethics, the law and the AI tutor');
 card(s, M, 1.5, 5.9, 3.4, 'Teach attack to teach defence', '• every attack is paired with prevention and mitigation\n• Nmap, Kali and cracking only on the isolated lab network\n• written permission and scope = ethical hacking\n• unauthorised access is a criminal offence\n• consider a signed lab acceptable-use agreement', C.sand, C.teal, 14);
 card(s, 6.83, 1.5, 5.9, 3.4, 'The AI tutor is set up to…', '• explain, hint and quiz on the chosen lesson\n• not give the workbook answers\n• refuse exploit code, attack commands, malware or phishing templates\n• remind students that unauthorised access is illegal\n• store nothing on the server; no names', C.tint, C.navy, 14);
 card(s, M, 5.15, W - 2 * M, 1.4, 'Exam-assessed, so no assignment coach', 'Students can use the tutor freely for revision and to check practice answers. It runs on the college Azure service; if it is offline every other page still works.', C.mint, C.navy, 13);
 notes(s, ['Discuss the Computer Misuse Act before the first practical and refer back to it in M4 (penetration testing).', 'The security rule is held on the server, so students cannot remove it from the page.']);
}

// 7 Delivery plan
{
 const s = pres.addSlide(); title(s, 'Delivery plan (2025–26)');
 const phases = [['Week 11', '8.1 confidential information, reasons, impact'], ['Weeks 12–17', '8.2 threats, vulnerabilities (technical, human, physical) and impact'], ['Weeks 18–21', '8.3 mitigation techniques; firewalls, segregation, monitoring'], ['Weeks 22–26', '8.4 CIA triad and IAAA model'], ['Weeks 27–29', 'Revision and exam']];
 const w = (W - 2 * M) / 5;
 s.addShape(pres.shapes.LINE, {x: M, y: 2.35, w: W - 2 * M, h: 0, line: {color: C.navy, width: 3}});
 phases.forEach(([h, b], i) => {
  const x = M + i * w, f = [C.tint, C.sand, C.mint, C.tint, C.sand][i];
  s.addShape(pres.shapes.OVAL, {x: x + w / 2 - 0.18, y: 2.17, w: 0.36, h: 0.36, fill: {color: C.teal}, line: {color: C.white, width: 2}});
  s.addText(h, {x, y: 1.5, w, h: 0.5, align: 'center', fontFace: BODY, fontSize: 15, bold: true, color: C.navy, margin: 0, isTextBox: true});
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: x + 0.1, y: 2.8, w: w - 0.2, h: 2.5, fill: {color: f}, line: {color: f}, rectRadius: 0.1});
  s.addText(b, {x: x + 0.25, y: 2.95, w: w - 0.5, h: 2.2, fontFace: BODY, fontSize: 14, color: C.ink, valign: 'top', margin: 0, isTextBox: true});
 });
 footer(s, 'Based on the 2025–26 Unit 8 teaching outline (January to June, exam in June). The Teachers page maps each week to its lesson, practical and quiz.');
 notes(s, ['Half term and Easter fall inside 8.2 and 8.3: use the site quizzes as holiday retrieval practice.']);
}

divider('8.1 Security risks', 'The information organisations hold, why it must stay confidential, and what happens when it does not');

lessonSplit('8.1', 'Confidential information and its impact', 'confidential_information_held_by_an_orga', 'identify confidential information, explain why it must be kept confidential and the impact of failure',
 ['HR: salaries, staff details', 'Commercial: clients, stakeholders, IP, sales, contracts', 'Access: passwords, PINs, MFA, biometrics', 'Reasons: competitors, privacy, unauthorised access', 'Impacts: fines, licence, trust, image, legal action'],
 [['Starter', 'News story: a recent data breach. What leaked? Who was harmed?'], ['Task', 'Workbook S1: a dental practice’s information.'], ['Check', 'Quiz 1.']],
 ['Use the 8.1 eLearning module from Teams as a flipped task before this lesson.', 'Question: why is access information the most dangerous to lose?', 'Stretch: which impacts are regulatory, reputational, financial or legal?', 'Video (S1): Cyber threats and why cyber attacks happen (MrBrownCS).'], 'what_happens_when_confidentiality_fails');

divider('8.2 Threats and vulnerabilities', 'Technical threats · technical, human and physical vulnerabilities · impact');

lessonSplit('8.2.1', 'Malware, botnets and denial of service', 'a_botnet_launching_a_ddos_attack', 'explain malware types, botnets and DoS/DDoS with prevention and mitigation',
 ['Virus, worm, keylogger, ransomware, spyware, RAT', 'Botnet: bots controlled via a C&C server', 'DoS vs DDoS: one source vs thousands', 'Prevent: anti-malware, patching, trusted sources', 'Mitigate: offline backups, DDoS protection'],
 [['Starter', 'WannaCry in 60 seconds: what stopped hospitals working?'], ['Task', 'Workbook T1: three malware threats to a school.'], ['Check', 'Quiz 2a.']],
 ['Emphasise prevention vs mitigation: backups do not stop ransomware but limit its damage.', 'Question: why is a worm more dangerous on an unpatched network?', 'Videos (T1): Types of malware; Botnets & DDoS; Computerphile WannaCry (stretch).']);

lessonSplit('8.2.1', 'Malicious hacking', 'how_sql_injection_changes_a_query', 'explain hackers’ motives and brute force, XSS, SQL injection and buffer overflow attacks',
 ['Hacktivists, nation states, organised crime, individuals', 'Brute force: length beats complexity', 'SQL injection → parameterised queries', 'XSS → output encoding', 'Buffer overflow → bounds checking, patches'],
 [['Starter', 'Which hacker group is behind each headline?'], ['Practical', 'Practical 2: how strong is that password?'], ['Task', 'Workbook T2: an online shop’s weak points.']],
 ['Demonstrate SQL injection only with the diagram or a local test page, never a live site.', 'Link to Unit 12 (software development): secure coding.', 'Videos (T2): MrBrownCS attacks; Computerphile SQL injection, XSS and password cracking (stretch).'], 'how_password_length_affects_brute_force_');

lessonSplit('8.2.1', 'Social engineering', 'spotting_a_phishing_email', 'explain phishing, spear phishing, smishing, vishing, pharming, watering hole and USB baiting',
 ['Exploits trust, fear, curiosity, urgency', 'Phishing vs spear phishing', 'Smishing (SMS), vishing (voice)', 'Pharming redirects the real address', 'Watering hole; USB baiting'],
 [['Practical', 'Practical 1: spot the phish.'], ['Task', 'Workbook T3: a staff guide for a bank.'], ['Check', 'Quiz 2b.']],
 ['Collect real (sanitised) scam texts and emails from staff for the practical.', 'Question: why does MFA help even when training fails?', 'Videos (T3): MrBrownCS social engineering (two videos).']);

lessonSplit('8.2.1', 'DNS, APIs, man-in-the-middle and open Wi-Fi', 'a_man_in_the_middle_attack_on_open_wi_fi', 'explain network-based threats and their prevention',
 ['DNS attack/redirection → DNSSEC, registrar MFA', 'Insecure APIs → authentication, authorisation, rate limits', 'Man-in-the-middle → HTTPS/TLS, VPN', 'Open Wi-Fi → VPN, HTTPS, WPA2/3'],
 [['Starter', 'Which Wi-Fi networks can you see from this room? Which are open?'], ['Task', 'Workbook T4: staff on hotel Wi-Fi.'], ['Check', 'Exit: why does a VPN help?']],
 ['Link APIs to the Postman demo from content area 7.', 'Videos (T4): Computerphile man-in-the-middle; DNS cache poisoning and KRACK (stretch).']);

lessonSplit('8.2.2–3', 'Technical vulnerabilities and human threats', 'the_life_of_a_software_vulnerability', 'explain technical vulnerabilities and human threats with prevention',
 ['Weak encryption, poor password policy, no MFA', 'Out-of-date hardware, software, firmware', 'Zero-day and legacy systems', 'Human error, malicious employee', 'Disguised criminal, poor cyber hygiene'],
 [['Starter', 'An unlocked PC: what could a visitor do in 30 seconds?'], ['Task', 'Workbook V1 and V2.'], ['Check', 'Quiz 3.']],
 ['Order of actions when dismissing staff: suspend accounts, remove from premises, recover devices.', 'Videos (V1, V2): Vulnerabilities; Avi Rubin TED talk; Cisco Anatomy of an IoT Attack; Internal threats.']);

lessonSplit('8.2.4–5', 'Physical vulnerabilities and impact', 'layers_of_physical_security', 'explain physical vulnerabilities, their prevention, and the impact of threats',
 ['Entry control systems', 'No tailgating; complex, changed codes; monitoring; audits', 'Shoulder surfing, environment, vandalism', 'Rugged machines; natural disasters', 'Impacts: data loss, access, corruption, disruption'],
 [['Practical', 'Practical 8: perimeter security proposal (worksheet on Teams).'], ['Task', 'Workbook V3.'], ['Check', 'Quiz 3.']],
 ['Walk the college perimeter (or use a floor plan) and spot vulnerabilities layer by layer.', 'Videos (V3): Physical security measures & biometrics; Physical security methods.']);

divider('8.3 Threat mitigation', 'Techniques, their purposes, benefits and drawbacks · processes that assure internet security');

lessonSplit('8.3.1', 'Technical defences', 'where_defences_sit_on_a_network', 'explain security settings, anti-malware, IDS, hardening, updates and air gaps',
 ['Security settings (hardware, software)', 'Anti-malware: function and actions', 'Intrusion detection', 'Device hardening; updates; firmware', 'Air gaps'],
 [['Starter', 'Open Windows Security: what is it protecting?'], ['Task', 'Workbook M1: four defences for a charity.'], ['Check', 'Quiz 4a.']],
 ['For every technique, insist on one benefit and one drawback.', 'Videos (M1): Protecting against malware; Detection and prevention; Prevention measures.']);

lessonSplit('8.3.1', 'Encryption', 'symmetric_and_asymmetric_encryption', 'explain hashing, symmetric and asymmetric encryption',
 ['Hashing: one-way; passwords, integrity', 'Symmetric: one key; fast; key sharing problem', 'Asymmetric: public/private keys; slower', 'HTTPS uses both', 'Diffie-Hellman: agree a key in public'],
 [['Practical', 'Practicals 3 and 4: Diffie-Hellman and hashing.'], ['Task', 'Workbook M2: a surgery’s three needs.'], ['Check', 'Quiz 4a.']],
 ['Use the teacher’s dh.xlsx spreadsheet (P = 23, G = 9, a = 4, b = 3 → shared key 9).', 'Videos (M2): Symmetric and asymmetric encryption; Computerphile hashing and Diffie-Hellman.'], 'diffie_hellman_key_exchange_with_small_n');

lessonSplit('8.3.1', 'People and access controls', 'the_factors_of_authentication', 'explain policies, vetting, training, access control, MFA, password managers, VPNs and API certification',
 ['User access policies; staff vetting', 'Staff training', 'Software-based access control', 'MFA: know, have, are', 'Password managers; VPNs; API certification'],
 [['Starter', 'Is password + security question MFA? Vote and justify.'], ['Task', 'Workbook M3.'], ['Check', 'Quiz 4a.']],
 ['Use the NCSC password guidance PDF on Teams.', 'Videos (M3): Computerphile 2FA; Tom Scott on 2FA; password managers.']);

lessonSplit('8.3.1', 'Backups, port scanning and penetration testing', 'the_stages_of_a_penetration_test', 'explain backup types and storage, port scanning and ethical vs unethical hacking',
 ['Full, incremental, differential', 'Safe storage: offsite, offline, encrypted, tested', 'Port scanning finds open services', 'Penetration test: plan, recon, scan, exploit, report', 'Ethical = permission + scope'],
 [['Practical', 'Practical 6: Nmap on the lab network only.'], ['Task', 'Workbook M4: a backup plan.'], ['Check', 'Quiz 4a.']],
 ['Students’ John the Ripper presentations (Teams) fit here as a discussion of password auditing.', 'Videos (M4): Backup policies; Ethical hacking and penetration testing.'], 'full_incremental_and_differential_backup');

lessonSplit('8.3.2', 'Firewalls, segregation and monitoring', 'firewall_rules_and_network_segregation', 'explain firewall configuration, network segregation, monitoring and port scanning',
 ['Inbound and outbound rules', 'Traffic type, application and IP rules', 'Default deny', 'Segregation: virtual, physical, offline; DMZ', 'Network monitoring; regular port scans'],
 [['Practical', 'Practical 7: firewall in Packet Tracer.'], ['Task', 'Workbook M5: a hotel network.'], ['Check', 'Quiz 4b.']],
 ['Revisit VLANs from content area 7 as virtual segregation.', 'Videos (M5): Firewalls; Cisco Anatomy of an Attack.']);

divider('8.4 Effective security', 'How confidentiality, integrity and availability interrelate · the IAAA model');

lessonWide('8.4.1', 'The CIA triad', 'the_cia_triad', 'explain confidentiality, integrity and availability and how they interrelate',
 [['Starter', 'Sort five incidents by the element they hit.'], ['Practical', 'Practical 9: a security policy mapped to CIA.'], ['Check', 'Quiz 5a.']],
 ['Specification wording: confidentiality controls access; integrity is supported by confidentiality; availability is only useful with integrity.', 'Question: how can too much confidentiality harm availability?', 'Video (C1): IBM Technology, What is the CIA triad.']);

lessonWide('8.4.2', 'The IAAA model', 'the_iaaa_model', 'explain identification, authentication, authorisation and accountability, with techniques, benefits and drawbacks',
 [['Practical', 'Practical 5: Linux users, groups and permissions.'], ['Task', 'Workbook C2: the shared till login.'], ['Check', 'Quiz 5b.']],
 ['Authentication proves who you are; authorisation decides what you may do. Students confuse these every year.', 'Shared logins break accountability: a common scenario question.', 'Video (C2): Professor Messer, AAA (stretch).']);

// Practicals overview
{
 const s = pres.addSlide(); title(s, 'Ten practicals on the student site');
 const labs = ['Spot the phish', 'How strong is that password?', 'Diffie-Hellman key exchange', 'Hashing and integrity', 'Linux users and permissions', 'Nmap in the lab network', 'Firewall in Packet Tracer', 'Perimeter security proposal', 'Security policy', 'Cisco Cybersecurity Essentials'];
 labs.forEach((t, i) => {
  const col = i % 5, row = Math.floor(i / 5), w = (W - 2 * M - 0.25 * 4) / 5, x = M + col * (w + 0.25), y = 1.6 + row * 2.45;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y, w, h: 2.2, fill: {color: row ? C.sand : C.tint}, line: {color: row ? C.sand : C.tint}, rectRadius: 0.12});
  s.addText(String(i + 1), {x: x + 0.2, y: y + 0.15, w: 1, h: 0.8, fontFace: HEAD, fontSize: 36, bold: true, color: C.teal, margin: 0, isTextBox: true});
  s.addText(t, {x: x + 0.2, y: y + 1.0, w: w - 0.4, h: 1.05, fontFace: BODY, fontSize: 15, bold: true, color: C.ink, margin: 0, isTextBox: true, valign: 'top'});
 });
 footer(s, 'Scanning and cracking only on the isolated lab network, with permission. Cisco activity files and Pearson worksheets stay on Teams.');
 notes(s, ['Map: 1 T3 · 2 T2 · 3–4 M2 · 5 C2 · 6 M4 · 7 M5 · 8 V3 · 9 C1 · 10 T1.']);
}

// Revision
{
 const s = pres.addSlide(); title(s, 'Revision and exam technique');
 const steps = ['RAG the spec', 'Re-learn reds', 'Quiz', 'Exam practice', 'Mark with levels', 'Re-do'];
 const w = (W - 2 * M - 0.2 * 5) / 6;
 steps.forEach((t, i) => {
  const x = M + i * (w + 0.2);
  s.addShape(pres.shapes.CHEVRON, {x, y: 1.6, w, h: 0.9, fill: {color: i % 2 ? C.teal : C.navy}, line: {color: C.white}});
  s.addText(t, {x: x + 0.35, y: 1.6, w: w - 0.6, h: 0.9, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 13, bold: true, color: C.white, margin: 0, isTextBox: true});
 });
 card(s, M, 2.9, 3.9, 2.3, 'Pair everything', 'Threat ↔ control. Benefit ↔ drawback. Prevention ↔ mitigation. The specification asks for pairs.', C.tint, C.navy, 14);
 card(s, M + 4.1, 2.9, 3.9, 2.3, 'Weak → strong', '“Use a firewall.”\n→ “A default-deny inbound rule stops attackers reaching StitchBox’s staff PCs from the internet.”', C.sand, C.teal, 14);
 card(s, M + 8.2, 2.9, 3.93, 2.3, 'Timing', 'About 1 minute per mark. Plan long answers for 2–3 minutes: risks, controls, judgement.', C.mint, C.navy, 14);
 notes(s, ['Revision weeks: target red spec points from the Course guide checklist, then Exam practice 1 and 2 before a timed official sample paper.']);
}

// Closing
{
 const s = pres.addSlide(); s.background = {color: C.navy};
 s.addText('Ready to deliver', {x: M, y: 1.2, w: 7, h: 1.0, fontFace: HEAD, fontSize: 42, bold: true, color: C.white, margin: 0, isTextBox: true});
 bullets(s, ['Share the start page link in Teams', 'Lesson 1: ethics, the law and the RAG checklist', 'Start each lesson with a real incident', 'Pair every threat with a control', 'Exam practice from spring term'], M, 2.4, 6.6, 3.5, 18, C.white);
 const ch = fitH('the_iaaa_model', 5.03);
 s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 7.4, y: 2.4, w: 5.33, h: ch + 0.3, fill: {color: C.white}, line: {color: C.white}, rectRadius: 0.15});
 img(s, 'the_iaaa_model', 7.55, 2.55, 5.03, 2.45);
 notes(s, ['Site: ' + SITE, 'The AI tutor depends on the college Azure subscription being active; the rest of the site works without it.']);
}

pres.writeFile({fileName: path.join(process.env.OUT || __dirname, 'Unit8-Security-Teacher-Deck.pptx')}).then(f => console.log('wrote', f));
