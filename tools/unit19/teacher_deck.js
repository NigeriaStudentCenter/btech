// Unit 19 Computer Networking: teacher delivery deck (original content).
const pptxgen = require('pptxgenjs');
const path = require('path');
const FIG = n => path.join(__dirname, 'figs', n + '.png');
const DIMS = {scale_fig: [760, 300], company_fig: [760, 370], topo_fig: [760, 420], models_fig: [760, 300], hypervisor_fig: [760, 260], cloud_fig: [760, 250], devices_fig: [760, 240], switch_fig: [760, 260], osi_fig: [760, 420], encap_fig: [760, 250], dns_fig: [760, 250], dhcp_fig: [760, 200], lifecycle_fig: [760, 170], hier_fig: [760, 330], and_fig: [760, 230], nat_fig: [760, 200], vlan_fig: [760, 220], perm_fig: [760, 200], ios_fig: [760, 200], baseline_fig: [760, 250]};

const C = {navy: '12324F', teal: '20857B', amber: 'E8A33D', ink: '17334B', muted: '4F6577', tint: 'EAF2F9', mint: 'E6F4F1', white: 'FFFFFF', line: 'C9D7E3', sand: 'FDF1E7'};
const HEAD = 'Cambria', BODY = 'Calibri';
const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.333 x 7.5
pres.author = 'Unit 19 course team';
pres.title = 'Unit 19 Computer Networking: teacher delivery deck';
const W = 13.333, H = 7.5, M = 0.6;

function img(slide, name, x, y, maxW, maxH) {
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
 slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y, w: 1.0, h: 0.34, fill: {color: C.teal}, line: {color: C.teal}, rectRadius: 0.08});
 slide.addText(code, {x, y, w: 1.0, h: 0.34, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 12, bold: true, color: C.white, margin: 0, isTextBox: true});
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
function lessonFlow(slide, parts, y) { // starter / task / check strip
 const w = (W - 2 * M - 0.3 * (parts.length - 1)) / parts.length;
 parts.forEach(([h, b], i) => card(slide, M + i * (w + 0.3), y, w, 1.35, h, b, [C.tint, C.mint, C.sand][i % 3], C.navy, 12));
}
const notes = (slide, lines) => slide.addNotes(lines.join('\n'));

// 1 Title
{
 const s = pres.addSlide(); s.background = {color: C.navy};
 s.addText('Unit 19', {x: M, y: 1.2, w: 6, h: 0.6, fontFace: BODY, fontSize: 20, bold: true, color: C.amber, margin: 0, isTextBox: true});
 s.addText('Computer Networking', {x: M, y: 1.75, w: 6.4, h: 1.5, fontFace: HEAD, fontSize: 48, bold: true, color: C.white, margin: 0, isTextBox: true, valign: 'top'});
 s.addText('Teacher delivery deck · BTEC Level 3 Nationals in Computing', {x: M, y: 3.35, w: 6.2, h: 0.5, fontFace: BODY, fontSize: 18, color: 'CADCFC', margin: 0, isTextBox: true});
 s.addText('Learn it · Build it · Test it · Evaluate it', {x: M, y: 4.1, w: 6.2, h: 0.5, fontFace: BODY, fontSize: 16, italic: true, color: C.white, margin: 0, isTextBox: true});
 s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 6.9, y: 2.05, w: 5.9, h: 3.25, fill: {color: C.white}, line: {color: C.white}, rectRadius: 0.15});
 img(s, 'company_fig', 7.05, 2.2, 5.6, 2.95);
 notes(s, ['Purpose: this deck launches and supports delivery of Unit 19 alongside the student course site (/btech/unit19/start.html).', 'Every lesson slide follows the college lesson structure: starter, aim, teach, practical, task, check, homework (flipped).', 'Speaker notes on each slide give teaching points, questions, differentiation and the matching workbook section and lab.']);
}

// 2 How this deck works
{
 const s = pres.addSlide(); title(s, 'How each lesson runs');
 const steps = [['Starter', '5 min hook or recap quiz'], ['Aim', 'share the learning aim and the criteria it builds'], ['Teach', 'diagram-led explanation with questioning'], ['Practical', 'Packet Tracer or Linux lab'], ['Task', 'workbook activity linked to the assignment'], ['Check', 'quiz or exit question'], ['Homework', 'flipped: preview the next lesson']];
 const w = (W - 2 * M - 0.15 * 6) / 7;
 steps.forEach(([h, b], i) => {
  const x = M + i * (w + 0.15);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y: 1.7, w, h: 2.2, fill: {color: i % 2 ? C.tint : C.mint}, line: {color: C.line}, rectRadius: 0.1});
  s.addShape(pres.shapes.OVAL, {x: x + w / 2 - 0.35, y: 1.9, w: 0.7, h: 0.7, fill: {color: C.navy}, line: {color: C.navy}});
  s.addText(String(i + 1), {x: x + w / 2 - 0.35, y: 1.9, w: 0.7, h: 0.7, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 18, bold: true, color: C.white, margin: 0, isTextBox: true});
  s.addText([{text: h, options: {bold: true, fontSize: 15, color: C.navy, breakLine: true}}, {text: b, options: {fontSize: 12, color: C.ink}}], {x: x + 0.1, y: 2.75, w: w - 0.2, h: 1.35, align: 'center', valign: 'top', fontFace: BODY, margin: 0, isTextBox: true});
 });
 card(s, M, 4.3, 6.0, 1.5, 'On the student site', 'Each lesson has a matching Learn page section, workbook activity (with AI tutor), Packet Tracer lab and quiz. Students can revisit everything outside class.');
 card(s, 6.9, 4.3, 5.83, 1.5, 'In the speaker notes', 'Teaching points, questions to ask, stretch and support ideas, the workbook section and lab to use, and the flipped homework.', C.mint);
 notes(s, ['Mirror the existing Unit 19 PowerPoint structure so students recognise the routine.', 'Starters from the department bank (Millionaire, catchphrase, Hollywood Squares) still work well here.', 'End every lesson with the online test or the site quiz and the lesson feedback form.']);
}

// 3 Unit at a glance
{
 const s = pres.addSlide(); title(s, 'Unit 19 at a glance');
 const stats = [['60', 'guided learning hours'], ['2', 'internally assessed assignments'], ['3', 'learning aims: A, B, C'], ['16', 'lessons on the student site'], ['10', 'hands-on labs']];
 const w = (W - 2 * M - 0.25 * 4) / 5;
 stats.forEach(([n, l], i) => {
  const x = M + i * (w + 0.25);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y: 1.6, w, h: 2.1, fill: {color: i === 0 ? C.navy : C.tint}, line: {color: i === 0 ? C.navy : C.tint}, rectRadius: 0.12});
  s.addText(n, {x, y: 1.75, w, h: 1.1, align: 'center', fontFace: HEAD, fontSize: 60, bold: true, color: i === 0 ? C.white : C.teal, margin: 0, isTextBox: true});
  s.addText(l, {x: x + 0.15, y: 2.85, w: w - 0.3, h: 0.7, align: 'center', fontFace: BODY, fontSize: 14, color: i === 0 ? C.white : C.ink, margin: 0, isTextBox: true});
 });
 const aims = [['A', 'Investigate how networks use communication protocols to give effective, secure access to services and resources', 'Assignment 1 · report'], ['B', 'Investigate network design to meet client requirements', 'Assignment 2 · design documents'], ['C', 'Develop a network to meet client requirements', 'Assignment 2 · build, test, evaluate, portfolio']];
 aims.forEach(([a, t, e], i) => card(s, M + i * 4.1, 4.1, 3.9, 2.4, `Learning aim ${a}`, `${t}.\n\n${e}`, [C.tint, C.mint, C.sand][i]));
 notes(s, ['Unit type: internal. Maximum of two summative assignments: A (A.P1, A.P2, A.M1, A.D1) and B+C (B.P3, B.P4, C.P5, C.P6, C.P7, B.M2, C.M3, BC.D2, BC.D3).', 'Resource requirement: a physical or virtual networking environment. Packet Tracer covers this safely; Linux VMs cover users, groups and permissions.', 'Links: Unit 20 Managing and Supporting Systems, Unit 21 Virtualisation, Unit 29 Network Operating Systems, Unit 30 Communication Technologies.']);
}

// 4 Assessment map
{
 const s = pres.addSlide(); title(s, 'Assessment map');
 const hdr = ['Assignment', 'Pass', 'Merit', 'Distinction'].map(t => ({text: t, options: {bold: true, color: C.white, fill: {color: C.navy}}}));
 const rows = [
  ['1 · Investigating computer networks (aim A)', 'A.P1 Explain the need for network types and models\nA.P2 Explain characteristics and functions of components', 'A.M1 Analyse the functions of components needed to build different network types', 'A.D1 Evaluate network models and their suitability for different client requirements'],
  ['2 · Design, build, test, evaluate (aims B and C)', 'B.P3 Explain the need for design and planning\nB.P4 Design a network to meet client requirements\nC.P5 Develop and configure it\nC.P6 Test it\nC.P7 Review it against requirements', 'B.M2 Justify design decisions\nC.M3 Optimise the network', 'BC.D2 Evaluate the design and the optimised network against requirements\nBC.D3 Demonstrate individual responsibility and self-management']];
 s.addTable([hdr, ...rows.map(r => r.map(t => ({text: t})))], {x: M, y: 1.45, w: W - 2 * M, colW: [2.6, 3.9, 2.8, 2.83], fontFace: BODY, fontSize: 12, color: C.ink, border: {type: 'solid', pt: 1, color: C.line}, fill: {color: C.white}, valign: 'top', margin: 0.08});
 card(s, M, 4.55, W - 2 * M, 1.1, 'Grading reminder', 'Pass: accurate, complete explanations and working evidence. Merit: analyse, justify, optimise (how and why). Distinction: evaluate with evidence and reasoned examples to justified conclusions; BC.D3 needs a portfolio kept throughout.', C.mint);
 notes(s, ['The student Assignment guide page restates every criterion in plain English with a success checklist; it is generated from the same data the AI coach uses.', 'Assignment 2 specification must be complex enough: more than one network type (wired and wireless) plus user requirements such as shared folders, printers, email and intranet access (Pearson guidance).', 'For C.M3, optimisation should follow from testing: performance, security loopholes or usability.']);
}

// 5 Student course site
{
 const s = pres.addSlide(); title(s, 'The student course site');
 const pages = [['1. Assignment guide', 'Both assignments in plain English, P/M/D explained, success checklists, AI rules'], ['2. Learn', '16 lessons with original diagrams, key terms, real-world examples and Packet Tracer tasks'], ['3. Workbook + tutor', 'Practice activity and quick check per lesson; AI study tutor; saves on device'], ['4. Practicals', '10 labs: LANs, wireless, servers, IOS security, routing, VLANs, Linux, troubleshooting'], ['5. Assignment builder', 'Checklists, planning tables (IP plan, test plan, permissions, evaluation, diary), AI coach, AI-use log'], ['6. Quizzes', 'Instant-marked checks: types, OSI and ports, subnetting, devices, configuration']];
 pages.forEach(([h, b], i) => card(s, M + (i % 3) * 4.1, 1.5 + Math.floor(i / 3) * 2.35, 3.9, 2.1, h, b, i % 2 ? C.mint : C.tint, C.navy, 14));
 footer(s, 'Plus 7. Videos: 11 embedded videos. Link for Teams: nigeriastudentcenter.github.io/btech/unit19/start.html · No accounts; work saves in the browser.');
 notes(s, ['Walk students through the site in lesson 1. Show the download backup button on shared machines.', 'Nothing is stored centrally: students must download backups before changing computers.', 'The Teachers page links to this deck and explains how the AI tutor and coach are configured.']);
}

// 6 AI tutor & coach
{
 const s = pres.addSlide(); title(s, 'AI tutor and assignment coach: used properly');
 card(s, M, 1.5, 5.9, 3.6, 'The AI will…', '• explain concepts in plain English\n• say what a task and command word ask for\n• help students plan with headings and questions\n• review the student’s own draft against the checklist\n• point out missing, thin or inaccurate points\n• use different examples, never the client’s', C.mint, C.teal, 14);
 card(s, 6.83, 1.5, 5.9, 3.6, 'The AI will not…', '• write paragraphs, tables, emails or evaluations\n• rewrite or “improve the wording” of student work\n• produce the client’s IP scheme, configs or test plan\n• predict or promise grades\n• accept instructions to break these rules', C.sand, 'A3560B', 14);
 card(s, M, 5.35, W - 2 * M, 1.35, 'AI-use log', 'Every coach question is saved with date, task and a reply extract. Students download it and submit it with their work, so AI use is acknowledged, in line with JCQ and Pearson guidance on AI in assessments.', C.tint, C.navy, 13);
 notes(s, ['Stress the student declaration: work must be their own. Using AI to generate assessed content is malpractice.', 'Ask students to hand in the AI-use log with each assignment; spot-check logs against drafts.', 'The coach receives only the task ID from the page; the brief, checklist and rules are held on the server so students cannot alter them.', 'The tutor runs on the college Azure service with daily usage limits; if it is offline the pages still work.']);
}

// 7 Delivery plan
{
 const s = pres.addSlide(); title(s, 'Suggested delivery plan');
 const phases = [['Weeks 2–8', 'Aim A: types, topologies, IP basics, OSI/TCP-IP, components, trends', C.tint], ['Weeks 10–13', 'Aim A: protocols, infrastructure services, software tools', C.mint], ['Weeks 14–18', 'Assignment 1 issued; aim B: design strategies, logical design, planning, access', C.sand], ['Weeks 19–26', 'Aim C practicals: configure, secure, route, VLANs, Linux, troubleshooting', C.tint], ['Weeks 27–33', 'Assignment 2: design, build, test, optimise, evaluate; portfolio throughout', C.mint]];
 const w = (W - 2 * M) / 5;
 s.addShape(pres.shapes.LINE, {x: M, y: 2.35, w: W - 2 * M, h: 0, line: {color: C.navy, width: 3}});
 phases.forEach(([h, b, f], i) => {
  const x = M + i * w;
  s.addShape(pres.shapes.OVAL, {x: x + w / 2 - 0.18, y: 2.17, w: 0.36, h: 0.36, fill: {color: C.teal}, line: {color: C.white, width: 2}});
  s.addText(h, {x, y: 1.5, w, h: 0.5, align: 'center', fontFace: BODY, fontSize: 15, bold: true, color: C.navy, margin: 0, isTextBox: true});
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: x + 0.1, y: 2.8, w: w - 0.2, h: 2.5, fill: {color: f}, line: {color: f}, rectRadius: 0.1});
  s.addText(b, {x: x + 0.25, y: 2.95, w: w - 0.5, h: 2.2, fontFace: BODY, fontSize: 14, color: C.ink, valign: 'top', margin: 0, isTextBox: true});
 });
 footer(s, 'Based on the 2025–26 Unit 19 scheme of work (33 weeks). Adjust to your calendar and assignment dates.');
 notes(s, ['Assignment 1 was issued mid-December with a late-January deadline in 2025–26; Assignment 2 runs after Easter.', 'Keep one practical per week so Packet Tracer skills are secure before Assignment 2.', 'Use the Cisco NetAcad Packet Tracer course early (digital badge) as a flipped task.']);
}

function divider(label, sub) {
 const s = pres.addSlide(); s.background = {color: C.navy};
 s.addText(label, {x: M, y: 2.3, w: W - 2 * M, h: 1.2, fontFace: HEAD, fontSize: 44, bold: true, color: C.white, margin: 0, isTextBox: true});
 s.addText(sub, {x: M, y: 3.6, w: W - 2 * M, h: 1.0, fontFace: BODY, fontSize: 20, color: 'CADCFC', margin: 0, isTextBox: true});
 return s;
}

// Lesson slide builders
function lessonWide(code, t, fig, aim, flow, n) { // big figure, strip of three cards
 const s = pres.addSlide(); chip(s, code); title(s, t, {y: 0.55, size: 28});
 s.addText('Aim: ' + aim, {x: M, y: 1.3, w: W - 2 * M, h: 0.4, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 const ih = img(s, fig, M, 1.8, W - 2 * M, 3.45);
 lessonFlow(s, flow, 1.8 + ih + 0.2);
 notes(s, n); return s;
}
function lessonSplit(code, t, fig, aim, points, flow, n, fig2) { // text left, figure right
 const s = pres.addSlide(); chip(s, code); title(s, t, {y: 0.55, size: 28});
 s.addText('Aim: ' + aim, {x: M, y: 1.3, w: 5.4, h: 0.6, fontFace: BODY, fontSize: 14, italic: true, color: C.muted, margin: 0, isTextBox: true, valign: 'top'});
 bullets(s, points, M, 1.95, 5.3, 3.4, 16);
 const h1 = img(s, fig, 6.25, 1.3, 6.48, fig2 ? 2.25 : 4.0);
 if (fig2) img(s, fig2, 6.25, 1.3 + h1 + 0.12, 6.48, 4.0 - h1 - 0.12);
 lessonFlow(s, flow, 5.55);
 notes(s, n); return s;
}

divider('Learning aim A', 'How networks use communication protocols to give effective and secure access to services and resources · Assignment 1');

lessonWide('A1', 'Why do we need different networks?', 'scale_fig', 'identify network types and their characteristics',
 [['Starter', 'List every network you used today, from earbuds to the internet.'], ['Task', 'Network types and models matrix: match LAN, WLAN, WAN, SAN, cloud to seven organisations.'], ['Check', 'Exit question: intranet vs extranet, one example each.']],
 ['Teach: PAN, LAN, WLAN, MAN, WAN, SAN by scale and by who manages them. Emphasise the NEED: communicate, share data, share resources, collaborate.', 'Question: why would a listed building choose a WLAN? Why does a hospital data centre use a SAN?', 'Support: give students the types table on the Learn page (A1a). Stretch: add the cost and security implications of each choice.', 'Workbook A1a. Practical: Lab 1 Packet Tracer tour. Homework: complete the NetAcad Packet Tracer short course.', 'Videos (site page 7, lesson A1a): Types of computer networks (LAN, MAN, WAN) and Internet vs intranet vs extranet.']);

lessonSplit('A1', 'One organisation, many network types', 'company_fig', 'explain intranet, extranet, internet, cloud and wired–wireless integration',
 ['Intranet: private services for staff', 'Extranet: part of the intranet opened to trusted outsiders', 'Internet: the public network of networks', 'Cloud: computing and storage rented over the internet', 'Wired for speed and reliability; wireless for mobility; access points join them'],
 [['Practical', 'Lab 3: wired and wireless integration with WPA2.'], ['Task', 'Write a short explanation of why we need wired and wireless integration.'], ['Link', 'A.P1 website pages: need and choice of each type.']],
 ['Use the diagram to trace who can reach what. Ask: where would the suppliers’ extranet live? What happens to the branch if the WAN link fails?', 'This builds directly into Assignment 1 Task 1 (A.P1).', 'Stretch: introduce VPNs as a way to reach the intranet securely from home.']);

lessonWide('A1', 'Topologies and Ethernet standards', 'topo_fig', 'identify physical and logical topologies and the IEEE 802 family',
 [['Starter', 'What topology do we use in college? At home? What equipment does it need?'], ['Task', 'Complete the topology comparison table: routing, complexity, scalability, reliability, cost.'], ['Check', 'Quiz 1 on the site: topology questions.']],
 ['Teach: bus and ring as legacy, star and extended star as the norm, mesh for resilience, hierarchical for enterprise.', 'Physical vs logical diagrams: students need both for Assignment 2.', 'IEEE 802.3 (Ethernet) and 802.11 (Wi-Fi); 2.4 GHz range vs 5 GHz speed; the Wi-Fi Alliance.', 'Workbook A1b. Stretch: why do data-centre and internet backbones use partial mesh?']);

lessonSplit('A1', 'Network models', 'models_fig', 'describe peer-to-peer, client/server and thin client models and evaluate their suitability',
 ['Peer-to-peer: cheap, simple, hard to manage beyond ~10 PCs', 'Client/server: central logins, files, backups; costs more, scales well', 'Thin client: server does the work; cheap, secure, network-dependent', 'Evaluate on ease of use, set-up, performance and suitability for applications'],
 [['Starter', 'Thin client video clip: what is actually on the desk?'], ['Task', 'Workbook A1c: choose a model for a hairdresser, a college and a call centre.'], ['Link', 'Prepares A.D1: balanced evaluation with reasoned examples.']],
 ['A.D1 needs benefits AND drawbacks for all three models, tested against the four factors, each backed by a realistic example, leading to a justified conclusion.', 'Model the difference between describing and evaluating with one worked paragraph using a different client (not the assignment wording).', 'Support: sentence stems (because… therefore… however…). Stretch: hybrid models, e.g. client/server plus cloud SaaS.', 'Video (lesson A1c): What is a thin client? Use it before the thin-client discussion.']);

lessonSplit('A1', 'Modern trends: virtualisation, cloud, BYOD, SDN', 'hypervisor_fig', 'explain modern networking trends and their challenges',
 ['Server sprawl and virtualisation: Type 1 vs Type 2 hypervisors', 'Cloud: public, private, hybrid, edge; IaaS, PaaS, SaaS', 'BYOD: flexibility vs security and support', 'SDN and software-defined storage: central control by software'],
 [['Practical', 'Install VirtualBox and create a Linux VM (Type 2 hypervisor).'], ['Task', 'Research SDN: one benefit, one challenge, one real example.'], ['Check', 'Workbook A1d quick check: IaaS vs SaaS.']],
 ['Show the cloud responsibility chart: the further right, the less the customer manages.', 'Ask: what is the noisy neighbour problem in public cloud?', 'Link BYOD to Cyber Essentials (employer feedback on the brief) and to guest VLANs later in B1.', 'Homework: Assignment 1 trends section research.', 'Videos (lesson A1d): Cisco Internet of Everything: Circle Story (1 min starter), AWS What is cloud computing?, Cloud computing in 6 minutes, What is SDN?, Intro to SAN technologies.'], 'cloud_fig');

lessonSplit('A2', 'Network hardware', 'devices_fig', 'identify the function and characteristics of network hardware',
 ['End devices create and use data; each NIC has a MAC address', 'Switch: layer 2, learns MACs, forwards frames to one port', 'Router: layer 3, routing table, static or dynamic routes', 'Access point: SSID, 802.11 standard, WPA2/WPA3', 'Media: UTP 100 m, fibre for distance and speed, wireless for mobility'],
 [['Starter', 'How many end devices can you name in 60 seconds?'], ['Practical', 'Lab 2 and show mac address-table: watch a switch learn.'], ['Task', 'Component table rows: function + characteristics (A.P2 practice).']],
 ['Characteristics to compare: switches (ports, speed, PoE, managed, layer 3); routers (interfaces, routing protocols, VPN, firewall); APs (standard, range, users, management); media (distance, speed, noise, cost).', 'Question: why is a hub legacy? What changes when a switch is managed?', 'Stretch: switching methods (store-and-forward vs cut-through) for the Merit analysis.'], 'switch_fig');

{
 const s = pres.addSlide(); chip(s, 'A2'); title(s, 'Network software and tools', {y: 0.55, size: 28});
 s.addText('Aim: identify networking software, monitoring and troubleshooting tools, and network applications', {x: M, y: 1.3, w: W - 2 * M, h: 0.4, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 const hdr = ['Tool', 'What it tells you', 'Classroom use'].map(t => ({text: t, options: {bold: true, color: C.white, fill: {color: C.navy}}}));
 const rows = [['ping', 'can a device be reached, and how fast', 'test gateway, server, other site'], ['tracert / traceroute', 'the routers a packet passes through', 'find where a route breaks'], ['ipconfig / ip a', 'address, mask, gateway, DNS', 'did DHCP work?'], ['nslookup', 'name to IP resolution', 'is DNS working?'], ['Wireshark', 'captured and decoded packets', 'watch DHCP, see unencrypted data'], ['Event Viewer / logs', 'errors, logins, security events', 'investigate failed logins'], ['Performance Monitor', 'CPU, memory, disk, network over time', 'build a baseline']];
 s.addTable([hdr, ...rows.map(r => r.map(t => ({text: t})))], {x: M, y: 1.85, w: 7.6, colW: [2.1, 3.0, 2.5], fontFace: BODY, fontSize: 13, color: C.ink, border: {type: 'solid', pt: 1, color: C.line}, fill: {color: C.white}, margin: 0.06});
 card(s, 8.55, 1.85, 4.18, 2.2, 'Systems software', 'Network operating systems (Windows Server, Linux), Cisco IOS, firewall and security software, virtualisation and cloud management.', C.tint, C.navy, 13);
 card(s, 8.55, 4.25, 4.18, 2.2, 'Network applications', 'Email, web, VoIP and video, shared databases, document management, remote access, cloud storage.', C.mint, C.navy, 13);
 notes(s, ['Demonstrate ping, tracert, ipconfig and nslookup live, then in Packet Tracer.', 'Ethics: packet sniffers and Nmap only on networks you own or have permission to test (Computer Misuse Act). The Nmap practical should run on the isolated lab network only.', 'Workbook A2b activity: order of tools for "cannot open the intranet".']);
}

lessonWide('A3', 'OSI and TCP/IP models', 'osi_fig', 'identify the OSI layers, the TCP/IP stack and the units of data',
 [['Starter', 'Mnemonic race: seven layers in order, top to bottom and bottom to top.'], ['Task', 'OSI table test: layer, function, protocol, device, PDU.'], ['Check', 'Quiz 2 on the site.']],
 ['Teach the purpose of layering: modular design, interoperability, troubleshooting.', 'Map devices to layers: hub/cable (1), switch (2), router (3); ports at layer 4.', 'TCP vs UDP: handshake, acknowledgements, re-sending vs speed.', 'Stretch: why the session and presentation functions sit inside the TCP/IP application layer.', 'Video (lesson A3): Warriors of the Net, Ericsson (12:57). Show in full; pause at the router, switch and firewall scenes and ask which OSI layer each works at.']);

lessonSplit('A3', 'Encapsulation, ports and sockets', 'encap_fig', 'explain encapsulation, ports and sockets',
 ['Each layer adds a header going down; removes it going up', 'Port numbers deliver data to the right service', 'IP address + port = socket (e.g. 192.168.1.10:443)', 'Key ports: 80, 443, 53, 67/68, 25, 110, 143, 20-21, 22, 23, 3389'],
 [['Practical', 'Packet Tracer simulation: open each PDU and inspect the headers.'], ['Task', 'Complete the protocol and port table (HTTP to NTP).'], ['Link', 'A.M1: how data transfers within and between networks.']],
 ['Encapsulation is the core of the A.M1 “how data gets transferred” illustration: switch reads MAC (frame), router reads IP (packet), service chosen by port (segment).', 'Question: why can one server host web and email at the same time?', 'Support: envelope-in-parcel analogy.']);

lessonSplit('A4', 'Infrastructure services: DNS and DHCP', 'dns_fig', 'explain infrastructure services and their operation',
 ['DNS: names to IP addresses, hierarchy and caching', 'DHCP: Discover, Offer, Request, Acknowledge; scope and lease', 'Directory services and authentication (AAA, RADIUS)', 'Routing and remote access, NAT, VPN', 'File, print, web, mail (SMTP, IMAP/POP3) and VoIP'],
 [['Practical', 'Lab 4: DHCP, DNS, web and email servers in Packet Tracer.'], ['Task', 'Workbook A4: services for a web-design office.'], ['Check', 'Why do printers get static addresses?']],
 ['A 169.254.x.x address means DHCP failed: a great diagnostic question.', 'Ask: what would break first if DNS failed? (Everything that uses names.)', 'These services reappear in Assignment 2 Appendix A (server with DHCP, DNS and web).', 'Stretch: DHCP relay across routers; DNS record types (A, MX, CNAME).'], 'dhcp_fig');

// Assignment 1 launch
{
 const s = pres.addSlide(); chip(s, 'ASG 1'); title(s, 'Assignment 1: Investigating computer networks', {y: 0.55, size: 28});
 s.addText('Scenario: junior network technician writing technical pages for the company website. Evidence: a report.', {x: M, y: 1.3, w: W - 2 * M, h: 0.45, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 const tasks = [['A.P1 · Pass', 'Website pages: need and choice of network types and models, topologies, standards, trends (BYOD, cloud).'], ['A.P2 · Pass', 'Table: functions and characteristics of hardware, media and software components.'], ['A.M1 · Merit', 'Report analysing how components work together in LAN, WAN and wireless; protocols and data transfer with illustrations.'], ['A.D1 · Distinction', 'Balanced evaluation of peer-to-peer, client/server and thin client for different clients, with a justified conclusion.']];
 tasks.forEach(([h, b], i) => card(s, M + (i % 2) * 6.1, 1.95 + Math.floor(i / 2) * 2.0, 5.95, 1.8, h, b, [C.tint, C.tint, C.mint, C.sand][i], C.navy, 14));
 card(s, M, 6.0, W - 2 * M, 0.9, 'Tools for students', 'Assignment guide checklists · Assignment builder component table · AI coach (explain, plan, review, accuracy) · AI-use log to submit', C.white, C.teal, 13);
 notes(s, ['Issue with the official brief. Walk through the plain-English guide and the checklists together.', 'Show the Assignment builder: students paste a section of their own draft for coach feedback; the coach will not write content.', 'Require the AI-use log with submission. Internal verification: sample logs alongside scripts.']);
}

divider('Learning aims B and C', 'Design, build, test and evaluate a network for a client · Assignment 2');

lessonSplit('B1', 'Design strategies', 'lifecycle_fig', 'explain why networks need design and planning strategies',
 ['Business goals become technical requirements', 'SOHO, SMB and enterprise designs differ', 'Aims: scalability, availability, redundancy, performance, security, manageability, adaptability, affordability', 'Constraints and trade-offs: budget, time, environment', 'Flat vs hierarchical (core, distribution, access)'],
 [['Starter', 'Why do we need a network design and planning strategies? Think-pair-share.'], ['Task', 'Workbook B1a: goals, requirements and constraints for a gym.'], ['Link', 'B.P3 customer email and B.M2 justification.']],
 ['Use the dental practice example on the Learn page (a different client from the assignment).', 'Discuss trade-offs explicitly: redundancy costs money; security affects ease of use.', 'Stretch: failure domains and link aggregation (EtherChannel) in hierarchical designs.', 'Video (lesson B1a): Port of Long Beach automated container terminal, with the VectorUSA and Cisco case study link: which design aims matter most in a port that stops if the network fails?'], 'hier_fig');

lessonSplit('B1', 'Logical design: IP addressing', 'and_fig', 'plan IP addressing, subnets, private and public addresses, and IPv6',
 ['Network and host portions; the subnet mask and prefix', 'ANDing finds the network address', 'Usable hosts = 2^host bits − 2', 'Private ranges, loopback, APIPA; NAT at the edge', 'IPv6: 128-bit hex; drop leading zeros; :: once'],
 [['Starter', 'Binary to decimal warm-up (maths link).'], ['Practical', 'Lab 6: two LANs and a router; test gateways.'], ['Check', 'Quiz 3: subnet 192.168.5.130/26.']],
 ['Worked example on the Learn page: 192.168.10.0/24 into four /26 subnets.', 'Common errors: gateway outside the subnet; wrong mask on one host; giving a host the network or broadcast address.', 'Support: subnet table with blocks of 64/32/16. Stretch: VLSM for subnets of different sizes.']);

lessonSplit('B1', 'NAT, naming and VLANs', 'vlan_fig', 'use naming schemes and VLANs in a logical design',
 ['Naming scheme: site-floor-type-number (e.g. LDN-FL2-SW01)', 'VLANs: separate logical networks on one switch', 'Benefits: security, smaller broadcast domains, easier management', 'Issues: complexity, managed switches, inter-VLAN routing, misconfiguration risk', 'Voice VLAN with QoS for VoIP'],
 [['Practical', 'Lab 8: VLANs, show vlan brief, test pings.'], ['Task', 'Design a naming scheme for a two-site office.'], ['Link', 'B.P4 logical design: addressing table and naming.']],
 ['Show the NAT diagram first: why a whole office appears as one public address.', 'VLANs support Appendix A requirements such as secure Wi-Fi and VoIP; students must decide and justify.'], 'nat_fig');

{
 const s = pres.addSlide(); chip(s, 'B2'); title(s, 'Planning: components, configuration and tests', {y: 0.55, size: 28});
 s.addText('Aim: select components, plan device configuration and write a test plan before building', {x: M, y: 1.3, w: W - 2 * M, h: 0.4, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 card(s, M, 1.9, 4.0, 2.25, 'Select', 'Servers, storage, switches, APs, router/WAN, OS and applications. Record a reason for every choice.', C.tint);
 card(s, M, 4.3, 4.0, 2.25, 'Configure (plan first)', 'Names, passwords, addresses, VLANs, routes, SSIDs and security, DHCP scopes, DNS records. Prototype in Packet Tracer.', C.mint);
 const hdr = ['No.', 'What is tested', 'How', 'Expected', 'Actual', 'Pass/fail'].map(t => ({text: t, options: {bold: true, color: C.white, fill: {color: C.navy}}}));
 const rows = [['1', 'PC to gateway', 'ping 192.168.20.1', '4 replies', '', ''], ['2', 'DHCP address', 'ipconfig', '.100–.150', '', ''], ['3', 'DNS', 'browse intranet.local', 'page loads', '', ''], ['4', 'Folder permission', 'log in as other group', 'access denied', '', ''], ['5', 'Device password', 'console login', 'prompt shown', '', '']];
 s.addTable([hdr, ...rows.map(r => r.map(t => ({text: t})))], {x: 4.85, y: 1.9, w: 7.88, colW: [0.55, 1.75, 1.9, 1.4, 1.1, 1.18], fontFace: BODY, fontSize: 12, color: C.ink, border: {type: 'solid', pt: 1, color: C.line}, fill: {color: C.white}, margin: 0.06});
 s.addText('Write the expected result before testing. Record failures, the cause, the fix and the re-test.', {x: 4.85, y: 5.4, w: 7.88, h: 0.8, fontFace: BODY, fontSize: 14, color: C.teal, bold: true, margin: 0, isTextBox: true});
 notes(s, ['The Assignment builder has inventory, IP plan, naming, access and test plan tables that export to CSV for Word or Excel.', 'Example rows use the dental practice, not the assignment client.', 'Stretch: layer 2 vs layer 3 vs layer 4 switching requirements; SAN vs NAS storage decisions.']);
}

lessonSplit('B3', 'Access: users, groups and permissions', 'perm_fig', 'plan authentication, users, groups and permissions',
 ['Password policy: NCSC guidance, passphrases, MFA, block common passwords', 'Audit policy: what gets logged and reviewed', 'Permissions to groups, not individuals; least privilege', 'Linux: owner/group/others, r=4 w=2 x=1 (e.g. chmod 750)', 'Windows NTFS permissions; printer permissions'],
 [['Practical', 'Lab 9: Linux groupadd, useradd, chown, chmod, access tests.'], ['Task', 'Workbook B3: access plan for a shop (MANAGERS, STAFF).'], ['Check', 'Quiz 5: chmod numbers.']],
 ['Appendix A needs users, groups and folder permissions with different access for others: students must work out their own numbers.', 'Use the college policies pack (password, remote access, network security) as real examples of policy documents.', 'Stretch: sticky bit and setgid for shared folders.', 'Video (lesson B3): Cisco Anatomy of an Attack (4 min). Discuss which password, access and audit controls would have stopped the attacker sooner.']);

lessonSplit('C1', 'Configuration with Cisco IOS', 'ios_fig', 'configure and secure switches, routers, wireless and servers',
 ['Modes: user EXEC, privileged EXEC, global config, interface/line', 'Secure: hostname, enable secret, console and vty passwords, service password-encryption, banner', 'Router: interface addresses, no shutdown, DHCP pool, static routes', 'Switch: VLANs, access ports, shut unused ports', 'Save: copy running-config startup-config'],
 [['Practical', 'Labs 5–7: secure a switch, two LANs, two sites with static routes.'], ['Task', 'Workbook C1: commands for BRANCH-R1 in order.'], ['Evidence', 'show running-config and screenshots with captions.']],
 ['Cover the Cisco device password setup handout. Emphasise that every device in Appendix A must be password protected.', 'Version your Packet Tracer files: v1-cabled, v2-addressed, v3-services.', 'Stretch: SSH instead of Telnet; RIPv2 or OSPF instead of static routes.']);

{
 const s = pres.addSlide(); chip(s, 'C2'); title(s, 'Testing and troubleshooting', {y: 0.55, size: 28});
 s.addText('Aim: test methodically, fix faults and document the results', {x: M, y: 1.3, w: W - 2 * M, h: 0.4, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 const steps = ['Identify', 'Theory', 'Test', 'Fix', 'Verify', 'Document'];
 const w = (W - 2 * M - 0.2 * 5) / 6;
 steps.forEach((t, i) => {
  const x = M + i * (w + 0.2);
  s.addShape(pres.shapes.CHEVRON, {x, y: 1.95, w, h: 0.9, fill: {color: i % 2 ? C.teal : C.navy}, line: {color: C.white}});
  s.addText(`${i + 1} ${t}`, {x: x + 0.25, y: 1.95, w: w - 0.5, h: 0.9, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 15, bold: true, color: C.white, margin: 0, isTextBox: true});
 });
 const hdr = ['Symptom', 'Likely cause', 'Check with'].map(t => ({text: t, options: {bold: true, color: C.white, fill: {color: C.navy}}}));
 const rows = [['Red link light', 'interface shut down or wrong cable', 'show ip interface brief'], ['Local pings work, remote fail', 'wrong gateway or missing route', 'ipconfig; show ip route'], ['169.254.x.x address', 'DHCP unreachable or off', 'server Services tab; ipconfig /renew'], ['IP works, name fails', 'DNS record or server wrong', 'nslookup'], ['Laptop won’t join Wi-Fi', 'SSID or passphrase mismatch', 'AP and laptop wireless settings']];
 s.addTable([hdr, ...rows.map(r => r.map(t => ({text: t})))], {x: M, y: 3.15, w: 8.0, colW: [2.4, 2.9, 2.7], fontFace: BODY, fontSize: 13, color: C.ink, border: {type: 'solid', pt: 1, color: C.line}, fill: {color: C.white}, margin: 0.06});
 card(s, 8.95, 3.15, 3.78, 3.3, 'Optimise (C.M3)', 'Base changes on test results: voice VLAN, shut unused ports, SSH not Telnet, extra AP for weak signal, reserved printer addresses. Re-test to prove the gain.', C.mint, C.teal, 13);
 notes(s, ['Lab 10: pairs break each other’s networks with the listed faults; the completed fault table is strong C.P6 practice.', 'Start at the bottom of the OSI model: physical, then addressing, then services.', 'Change one thing at a time; never delete failed tests from the plan.']);
}

lessonSplit('C3', 'Monitoring, evaluation and self-management', 'baseline_fig', 'baseline and monitor the network, evaluate it against requirements, and evidence self-management',
 ['Baseline: normal bandwidth, latency, CPU, memory, disk', 'Monitor and review event logs regularly', 'Review: how far each requirement is met (C.P7)', 'Evaluate: strengths and weaknesses with evidence from every stage, conclusions, future work (BC.D2)', 'Portfolio: plan, diary, peer feedback, witness statement (BC.D3)'],
 [['Task', 'One row of an evaluation grid for a practice network.'], ['Tool', 'Builder evaluation grid is pre-filled with every client requirement.'], ['Habit', 'Diary entry at the end of every Assignment 2 lesson.']],
 ['BC.D3 cannot be written at the end: it needs dated evidence throughout. Check diaries weekly.', 'Model a strong diary entry (see the Learn page C4 example).', 'Distinction evaluations synthesise across design, build, test and optimisation; weaker ones only restate test results.']);

// Assignment 2 launch
{
 const s = pres.addSlide(); chip(s, 'ASG 2'); title(s, 'Assignment 2: Design, build, test and evaluate', {y: 0.55, size: 28});
 s.addText('Scenario: junior network engineer; branch office of a web-design customer, with one off-site office.', {x: M, y: 1.3, w: W - 2 * M, h: 0.45, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 card(s, M, 1.95, 6.0, 4.5, 'Client requirements (Appendix A)', '• Server: DHCP, DNS, web\n• 10+ workstations; wired plus secure Wi-Fi\n• Wireless laptops at both sites\n• Internet and router link between sites\n• Users, groups and folder permissions\n• VoIP, antivirus, e-commerce facilities\n• All devices password protected\n• Scalable, secure, low cost\n• Full documentation with test plans and results', C.tint, C.navy, 14);
 const ev = [['B.P3', 'customer email'], ['B.P4 · B.M2', 'design + justification'], ['C.P5', 'build and configure'], ['C.P6 · C.M3', 'test and optimise'], ['C.P7 · BC.D2', 'review and evaluate'], ['BC.D3', 'portfolio throughout']];
 ev.forEach(([c, t], i) => {
  const y = 1.95 + i * 0.75;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 6.85, y, w: 1.9, h: 0.6, fill: {color: i === 5 ? C.amber : C.teal}, line: {color: C.white}, rectRadius: 0.08});
  s.addText(c, {x: 6.85, y, w: 1.9, h: 0.6, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 13, bold: true, color: C.white, margin: 0, isTextBox: true});
  s.addText(t, {x: 8.9, y, w: 3.83, h: 0.6, valign: 'middle', fontFace: BODY, fontSize: 15, color: C.ink, margin: 0, isTextBox: true});
 });
 notes(s, ['Issue the official brief with Appendix B (office layout) and Appendix C (skills, knowledge and behaviours).', 'Students plan in the Assignment builder: inventory, IP plan, naming, permissions, test plan, evaluation grid, targets, diary and feedback log.', 'Build in Packet Tracer; Linux VM for users, groups and permissions. Witness statements for professional behaviour and communication.', 'Remind students: the AI coach reviews their own drafts but will not design the network for them; submit the AI-use log.']);
}

// Practicals overview
{
 const s = pres.addSlide(); title(s, 'Ten labs on the student site');
 const labs = ['Packet Tracer tour', 'Build and test a LAN', 'Wired + wireless', 'DHCP, DNS, web, email', 'Secure a switch (IOS)', 'Two LANs and a router', 'Two sites, static routes', 'VLANs', 'Linux users and permissions', 'Troubleshooting challenge'];
 labs.forEach((t, i) => {
  const col = i % 5, row = Math.floor(i / 5), w = (W - 2 * M - 0.25 * 4) / 5, x = M + col * (w + 0.25), y = 1.6 + row * 2.45;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y, w, h: 2.2, fill: {color: row ? C.mint : C.tint}, line: {color: row ? C.mint : C.tint}, rectRadius: 0.12});
  s.addText(String(i + 1), {x: x + 0.2, y: y + 0.15, w: 1, h: 0.8, fontFace: HEAD, fontSize: 40, bold: true, color: C.teal, margin: 0, isTextBox: true});
  s.addText(t, {x: x + 0.2, y: y + 1.0, w: w - 0.4, h: 1.0, fontFace: BODY, fontSize: 16, bold: true, color: C.ink, margin: 0, isTextBox: true, valign: 'top'});
 });
 footer(s, 'Each lab lists steps, commands, how to check it works and the evidence to capture. Teacher .pkt files (switch working, Two LANs, Three router design, dns) can extend the labs via Teams.');
 notes(s, ['Labs map to lessons: 1 A1a · 2 A1b/A2a · 3 A1a · 4 A4 · 5 C1 · 6 B1b/C1 · 7 B1b/C1 · 8 B1b · 9 B3 · 10 C2.', 'Cisco NetAcad .pka activities remain on Teams; they are Cisco content and are not published on the public site.']);
}

// Closing
{
 const s = pres.addSlide(); s.background = {color: C.navy};
 s.addText('Ready to deliver', {x: M, y: 1.2, w: 7, h: 1.0, fontFace: HEAD, fontSize: 42, bold: true, color: C.white, margin: 0, isTextBox: true});
 bullets(s, ['Share the start page link in Teams', 'Lesson 1: tour the site and the Assignment guide', 'Enrol students on NetAcad Packet Tracer', 'Agree AI rules; collect AI-use logs with each assignment', 'Use the quizzes as starters and exit checks'], M, 2.4, 6.6, 3.5, 18, C.white);
 s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 7.4, y: 2.0, w: 5.33, h: 2.65, fill: {color: C.white}, line: {color: C.white}, rectRadius: 0.15});
 img(s, 'hier_fig', 7.55, 2.1, 5.03, 2.45);
 notes(s, ['Site: nigeriastudentcenter.github.io/btech/unit19/start.html', 'The AI tutor and coach depend on the college Azure subscription being active; the rest of the site works without it.']);
}

pres.writeFile({fileName: path.join(__dirname, 'Unit19-Computer-Networking-Teacher-Deck.pptx')}).then(f => console.log('wrote', f));
