// Unit 7 Digital environments: teacher delivery deck (original content).
// Figures are PNG exports of the Learn page diagrams: set FIGS to their folder (with dims.json).
const pptxgen = require('pptxgenjs');
const path = require('path');
const FIGS = process.env.FIGS || path.join(__dirname, 'figs');
const DIMS = require(path.join(FIGS, 'dims.json'));
const FIG = n => path.join(FIGS, n + '.png');

const C = {navy: '14304A', teal: '2A7F62', amber: 'D9772B', ink: '17334B', muted: '4F6577', tint: 'EAF2F9', mint: 'E6F4EE', white: 'FFFFFF', line: 'C9D7E3', sand: 'FDF1E7'};
const HEAD = 'Cambria', BODY = 'Calibri';
const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.333 x 7.5
pres.author = 'Unit 7 course team';
pres.title = 'Unit 7 Digital environments: teacher delivery deck';
const W = 13.333, H = 7.5, M = 0.6;
const SITE = 'nigeriastudentcenter.github.io/btech/unit7/start.html';

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
 s.addText('Content area 7', {x: M, y: 1.2, w: 6, h: 0.6, fontFace: BODY, fontSize: 20, bold: true, color: C.amber, margin: 0, isTextBox: true});
 s.addText('Digital environments', {x: M, y: 1.75, w: 6.4, h: 1.5, fontFace: HEAD, fontSize: 48, bold: true, color: C.white, margin: 0, isTextBox: true, valign: 'top'});
 s.addText('Teacher delivery deck · T Level Digital Production, Design and Development (core)', {x: M, y: 3.65, w: 6.2, h: 0.8, fontFace: BODY, fontSize: 18, color: 'CADCFC', margin: 0, isTextBox: true, valign: 'top'});
 s.addText('Hardware · Software · Networks · Virtual · Cloud · Resilience', {x: M, y: 4.6, w: 6.2, h: 0.5, fontFace: BODY, fontSize: 16, italic: true, color: C.white, margin: 0, isTextBox: true});
 const th = fitH('four_kinds_of_physical_computer', 5.6);
 s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 6.9, y: 2.9 - th / 2, w: 5.9, h: th + 0.3, fill: {color: C.white}, line: {color: C.white}, rectRadius: 0.15});
 img(s, 'four_kinds_of_physical_computer', 7.05, 3.05 - th / 2, 5.6, 3.7);
 notes(s, ['Purpose: this deck supports delivery of content area 7 alongside the student course site (' + SITE + ').', 'Every lesson slide follows the college routine: starter, aim, teach, practical, task, check, flipped homework.', 'Speaker notes give teaching points, questions, differentiation, and the matching workbook section, practical and quiz.']);
}

// 2 How each lesson runs
{
 const s = pres.addSlide(); title(s, 'How each lesson runs');
 const steps = [['Starter', '5 min hook or recap quiz'], ['Aim', 'share the aim and the spec point'], ['Teach', 'diagram-led explanation with questioning'], ['Practical', 'hands-on task or Packet Tracer'], ['Task', 'workbook activity on the site'], ['Check', 'quiz or exam-style exit question'], ['Homework', 'flipped: preview the next lesson']];
 const w = (W - 2 * M - 0.15 * 6) / 7;
 steps.forEach(([h, b], i) => {
  const x = M + i * (w + 0.15);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y: 1.7, w, h: 2.2, fill: {color: i % 2 ? C.tint : C.mint}, line: {color: C.line}, rectRadius: 0.1});
  s.addShape(pres.shapes.OVAL, {x: x + w / 2 - 0.35, y: 1.9, w: 0.7, h: 0.7, fill: {color: C.navy}, line: {color: C.navy}});
  s.addText(String(i + 1), {x: x + w / 2 - 0.35, y: 1.9, w: 0.7, h: 0.7, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 18, bold: true, color: C.white, margin: 0, isTextBox: true});
  s.addText([{text: h, options: {bold: true, fontSize: 15, color: C.navy, breakLine: true}}, {text: b, options: {fontSize: 12, color: C.ink}}], {x: x + 0.1, y: 2.75, w: w - 0.2, h: 1.35, align: 'center', valign: 'top', fontFace: BODY, margin: 0, isTextBox: true});
 });
 card(s, M, 4.3, 6.0, 1.5, 'On the student site', 'Each lesson has a Learn page section with diagrams and exam tips, a workbook activity with the AI tutor, a video, a practical where relevant, and a quiz.');
 card(s, 6.9, 4.3, 5.83, 1.5, 'In the speaker notes', 'Teaching points, questions to ask, stretch and support, the matching workbook section, practical and quiz, and the flipped homework.', C.mint);
 notes(s, ['Keep the existing starters from Teams (Millionaire, Hollywood Squares, catchphrase, IP quiz).', 'Keep using the Microsoft Forms end-of-lesson checks from the detailed SOW; the site quizzes work as extra starters or homework.']);
}

// 3 At a glance
{
 const s = pres.addSlide(); title(s, 'Content area 7 at a glance');
 const stats = [['6', 'topic areas: 7.1–7.6'], ['26', 'specification points'], ['18', 'lessons on the student site'], ['12', 'practical tasks'], ['1', 'written core exam']];
 const w = (W - 2 * M - 0.25 * 4) / 5;
 stats.forEach(([n, l], i) => {
  const x = M + i * (w + 0.25);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y: 1.6, w, h: 2.1, fill: {color: i === 4 ? C.navy : C.tint}, line: {color: i === 4 ? C.navy : C.tint}, rectRadius: 0.12});
  s.addText(n, {x, y: 1.75, w, h: 1.1, align: 'center', fontFace: HEAD, fontSize: 60, bold: true, color: i === 4 ? C.white : C.teal, margin: 0, isTextBox: true});
  s.addText(l, {x: x + 0.15, y: 2.85, w: w - 0.3, h: 0.7, align: 'center', fontFace: BODY, fontSize: 14, color: i === 4 ? C.white : C.ink, margin: 0, isTextBox: true});
 });
 const areas = [['7.1 Hardware', 'physical systems, devices'], ['7.2 Software', 'OS, utilities, dev tools, apps'], ['7.3 Networks', 'types to protocols, 11 points'], ['7.4 Virtual', 'VMs and hypervisors'], ['7.5 Cloud', 'types, benefits, IaaS/PaaS/SaaS'], ['7.6 Resilience', 'benefits and methods']];
 const w2 = (W - 2 * M - 0.2 * 5) / 6;
 areas.forEach(([h, b], i) => card(s, M + i * (w2 + 0.2), 4.1, w2, 1.9, h, b, [C.tint, C.mint, C.sand][i % 3], C.navy, 13));
 footer(s, 'Number systems (binary, denary, hexadecimal, units) are taught first as a foundation for addressing, storage and data representation.');
 notes(s, ['Content area 7 is part of the T Level core, assessed by written examination together with other core content areas. Check the current specification and exam timetable with your awarding organisation.', '7.3 Networks is the largest block (11 of 26 points) and takes roughly half the teaching weeks.']);
}

// 4 Assessment and command words
{
 const s = pres.addSlide(); title(s, 'How it is assessed: exam technique');
 table(s, ['Command word', 'What students must do', 'Typical marks'], [
  ['State / identify', 'short fact or name, no explanation', '1'],
  ['Describe', 'features or steps; one mark per accurate point', '2–4'],
  ['Explain', 'point + why/how (“because”, “so that”), applied to the scenario', '2–6'],
  ['Discuss', 'different sides: how it works, benefits, drawbacks, depends on', '6–9'],
  ['Evaluate / justify', 'weigh strengths against weaknesses; supported judgement', '9–12']], {x: M, y: 1.45, w: 7.6, colW: [1.9, 4.6, 1.1]});
 card(s, 8.5, 1.45, 4.23, 2.35, 'Level-marked answers', 'Long answers are judged as a whole. Reward developed points linked to the scenario, not lists. About 1 minute per mark.', C.mint, C.teal, 13);
 card(s, 8.5, 4.0, 4.23, 2.35, 'On the site', 'Exam practice has two scenario papers (short and extended) with self-marking checklists and level descriptors. Every question links to its lesson and the AI tutor.', C.sand, C.navy, 13);
 notes(s, ['Model the PEEL-style developed point: point, explain, example/apply, link back.', 'Use the awarding organisation’s sample assessment materials and past papers for timed mocks; the site’s exam practice is original, not official.', 'Most common weakness: generic answers that ignore the scenario. Insist on naming the business in every point.']);
}

// 5 Student site
{
 const s = pres.addSlide(); title(s, 'The student course site');
 const pages = [['1. Course guide', 'How the exam works and a red/amber/green checklist of all 26 spec points'], ['2. Learn', '18 lessons with original diagrams, key terms, exam tips and questions'], ['3. Workbook + tutor', 'An activity and quick check per lesson; AI study tutor; saves on device'], ['4. Practicals', '12 tasks: motherboard, command line, Packet Tracer, VMs, resilience plan'], ['5. Exam practice', 'Scenario papers with command-word guide and level marking'], ['6. Quizzes', 'Five instant-marked quizzes, one per topic block']];
 pages.forEach(([h, b], i) => card(s, M + (i % 3) * 4.1, 1.5 + Math.floor(i / 3) * 2.35, 3.9, 2.1, h, b, i % 2 ? C.mint : C.tint, C.navy, 14));
 footer(s, 'Plus 7. Videos: 30 embedded videos (MrBrownCS series, TED, Cisco). Link for Teams: ' + SITE + ' · No accounts; work saves in the browser.');
 notes(s, ['Tour the site in the first lesson. Show the download backup button on shared machines.', 'Ask students to complete the RAG checklist in the Course guide after each topic and screenshot it before one-to-ones.']);
}

// 6 AI tutor
{
 const s = pres.addSlide(); title(s, 'The AI study tutor: used well');
 card(s, M, 1.5, 5.9, 3.6, 'Encourage students to…', '• ask for a concept explained another way\n• ask it to quiz them on a lesson\n• get one hint when stuck, then try again\n• check a practice answer and ask what is missing\n• use Practice mode for new questions', C.mint, C.teal, 14);
 card(s, 6.83, 1.5, 5.9, 3.6, 'It is set up to…', '• stay on the lesson they chose\n• give hints, not the workbook answers\n• use different numbers from the activity\n• reply in plain English for 16–18 year olds\n• ignore attempts to change its rules', C.sand, 'A3560B', 14);
 card(s, M, 5.35, W - 2 * M, 1.35, 'Exam-assessed, so no assignment coach', 'There is no coursework in this content area, so students can use the tutor freely for revision. No names or accounts; nothing is stored on the server.', C.tint, C.navy, 13);
 notes(s, ['The page sends only the lesson ID; the notes and rules are held on the server.', 'The tutor runs on the college Azure service with usage limits. If it is offline, every other page still works.']);
}

// 7 Delivery plan
{
 const s = pres.addSlide(); title(s, 'Delivery plan (2025–26 SOW)');
 const phases = [['Weeks 2–7', 'Number systems; 7.1 hardware; PC practical; IoT; Raspberry Pi', C.tint], ['Weeks 8–10', '7.2 software: OS, utilities, dev tools, applications', C.mint], ['Weeks 11–24', '7.3 networks: types to protocols, bandwidth and latency; practicals', C.sand], ['Weeks 25–31', '7.4 virtual, 7.5 cloud, 7.6 resilience', C.tint], ['Weeks 32–33', 'Revision and exam practice', C.mint]];
 const w = (W - 2 * M) / 5;
 s.addShape(pres.shapes.LINE, {x: M, y: 2.35, w: W - 2 * M, h: 0, line: {color: C.navy, width: 3}});
 phases.forEach(([h, b, f], i) => {
  const x = M + i * w;
  s.addShape(pres.shapes.OVAL, {x: x + w / 2 - 0.18, y: 2.17, w: 0.36, h: 0.36, fill: {color: C.teal}, line: {color: C.white, width: 2}});
  s.addText(h, {x, y: 1.5, w, h: 0.5, align: 'center', fontFace: BODY, fontSize: 15, bold: true, color: C.navy, margin: 0, isTextBox: true});
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: x + 0.1, y: 2.8, w: w - 0.2, h: 2.5, fill: {color: f}, line: {color: f}, rectRadius: 0.1});
  s.addText(b, {x: x + 0.25, y: 2.95, w: w - 0.5, h: 2.2, fontFace: BODY, fontSize: 14, color: C.ink, valign: 'top', margin: 0, isTextBox: true});
 });
 footer(s, 'Based on the 2025–26 Digital environments scheme of work (35 weeks). The Teachers page on the site maps each week to its lesson, practical and quiz.');
 notes(s, ['Networks take about 14 weeks: keep one hands-on session every week or two so the theory stays concrete.', 'Cisco Academy weeks (IoT, week 4; week 14) can use the NetAcad courses as flipped or catch-up work.']);
}

divider('Number systems and 7.1 Hardware', 'Binary, denary and hex · physical computer systems · hardware devices');

lessonSplit('NS', 'Number systems', 'the_same_number_in_four_number_bases', 'convert between binary, denary and hexadecimal, add binary and use units of data',
 ['Place values: 128 64 32 16 8 4 2 1', 'Hex: one digit = 4 bits (a nibble)', 'Binary addition and overflow', 'Units: bit, nibble, byte; kB vs KiB (1000 vs 1024)', 'Why it matters: addresses, colours, storage sizes'],
 [['Starter', 'Hold up cards 128…1: make your age in binary.'], ['Task', 'Workbook NS and Practical 4 (numbers booklet).'], ['Check', 'Quiz 1: conversions, units, two’s complement.']],
 ['Teach the column method first, then repeated division by 2 for denary to binary.', 'Question: why does a 1 TB drive show about 931 GiB in Windows?', 'Support: printed place-value grid. Stretch: two’s complement and binary shifts.', 'Videos (lesson NS): MrBrownCS Introduction to Binary, Binary–Decimal Conversions, Binary Addition, Signed Binary.'], 'adding_two_binary_bytes');

lessonSplit('7.1.1', 'Types of physical computer system', 'four_kinds_of_physical_computer', 'describe the features and uses of personal computers, servers, mainframes, supercomputers and embedded systems',
 ['Personal: desktop, laptop, tablet, phone', 'Servers: services for clients; redundant parts', 'Mainframes: huge transaction volumes, reliability', 'Supercomputers: parallel science and simulation', 'Embedded: dedicated, low power, real-time; IoT'],
 [['Starter', 'Count the computers you used before college today.'], ['Practical', 'Practical 1: PC disassemble and reassemble.'], ['Task', 'Workbook H1: match systems to organisations.']],
 ['Emphasise features AND use: the exam asks why a system suits a scenario.', 'Question: why do embedded devices often go unpatched? (link to 7.6 resilience).', 'Stretch: quantum computers as an emerging type.', 'Videos (lesson H1): Embedded systems (MrBrownCS), Cisco Internet of Everything, Avi Rubin TED talk on hacking devices.'], 'inside_an_embedded_system_a_smart_thermo');

lessonSplit('7.1.2', 'Hardware devices: memory and storage', 'the_memory_and_storage_hierarchy', 'explain the features and use of memory, storage, motherboards and interfaces',
 ['Input, output and sensors', 'RAM (volatile) vs ROM (firmware)', 'Cache: small, fast, close to the CPU', 'Storage: magnetic, solid state, optical', 'Motherboard: socket, slots, chipset, buses; PCIe, USB, NIC'],
 [['Starter', 'Which is faster: RAM or SSD? Why do we need both?'], ['Practical', 'Practical 2: Motherboard ID and connectors.'], ['Homework', 'Practical 3: hardware spider diagram.']],
 ['Use the hierarchy: speed and cost per GB fall as capacity rises.', 'Question: a school laptop has 4 GB RAM and slows with many tabs. Why?', 'Support: labelled motherboard handout. Stretch: NVMe vs SATA SSD.', 'Videos (lesson H2): Main memory; Secondary storage; Buses; Registers.'], 'labelled_top_down_view_of_a_desktop_moth');

lessonSplit('7.1.2', 'Processors, GPUs and cooling', 'inside_a_four_core_processor_chip', 'explain processor features and why cooling is needed',
 ['Cores, clock speed and cache set performance', 'Mobile processors: low power, less heat', 'GPU: thousands of cores for parallel graphics and AI', 'Air cooling: heatsink and fan', 'Liquid cooling: quieter, handles more heat, costs more'],
 [['Starter', 'Why doesn’t an 8-core CPU run a game twice as fast as a 4-core?'], ['Task', 'Spec a PC for a video editor and justify each part.'], ['Check', 'Quiz 2: hardware.']],
 ['Link features to effect: more cores help only when software is multi-threaded.', 'Thermal throttling: why laptops slow down when hot.', 'Raspberry Pi practical (week 7) is a good embedded-system bridge.', 'Video (lesson H2): Factors affecting CPU performance (MrBrownCS).'], 'air_cooling_and_liquid_cooling');

divider('7.2 Software', 'Operating systems · utilities · code development tools · applications');

lessonSplit('7.2.1', 'Operating systems', 'layers_of_software_between_the_user_and_', 'explain the features and uses of different types of operating system',
 ['Functions: memory, processes, files, devices, security, UI', 'Single-user single-task and multi-tasking', 'Multi-user and network operating systems', 'Real-time: guaranteed response (airbags, robots)', 'Batch vs real-time processing'],
 [['Starter', 'What does Task Manager show? Open it and explain one column.'], ['Task', 'Workbook SW1: match OS types to devices.'], ['Check', 'Exit: two functions of an OS.']],
 ['Show time slicing to explain multitasking on one core.', 'Question: why must a pacemaker use a real-time OS?', 'Stretch: kernel vs user mode; device drivers.', 'Video (lesson SW1): Operating System (MrBrownCS).'], 'timeline_of_multitasking_with_time_slice');

lessonSplit('7.2.2', 'Utilities', 'full_incremental_and_differential_backup', 'explain the purpose of common utilities',
 ['Antivirus and firewall', 'Backup: full, incremental, differential', 'Compression: lossy vs lossless', 'Disk defragmenter (not for SSDs) and disk clean-up', 'Encryption and file management tools'],
 [['Starter', 'You deleted your coursework. Which utility would have saved you?'], ['Task', 'Workbook SW2: choose a backup type for a café.'], ['Check', 'Quiz 3: utilities.']],
 ['Walk through restoring from each backup type: full + last incremental chain vs full + one differential.', 'Question: why not defragment an SSD?', 'Links to 7.6 resilience (backup and recovery procedures).', 'Videos (lesson SW2): Utility software; Lossy and lossless compression.'], 'hard_disc_drive_compared_with_solid_stat');

lessonSplit('7.2.3', 'Code development tools', 'parts_of_an_integrated_development_envir', 'explain the features and uses of IDEs, translators and version control',
 ['IDE: editor, highlighting, auto-complete, debugger', 'Breakpoints and stepping find logic errors', 'Compiler vs interpreter; assembler', 'Version control (Git): history, branches, roll back', 'Libraries, frameworks and APIs'],
 [['Starter', 'Spot the syntax error on the board in 30 seconds.'], ['Practical', 'Set a breakpoint in a short Python program.'], ['Task', 'Workbook SW3: compiler or interpreter?']],
 ['Demonstrate in VS Code or Thonny: highlight, error squiggle, breakpoint.', 'Question: why would a games studio ship compiled code?', 'API extension: the Postman slides on Teams show how apps call cloud services.'], 'compiler_compared_with_interpreter');

{
 const s = pres.addSlide(); chip(s, '7.2.4'); title(s, 'Application software', {y: 0.55, size: 28});
 s.addText('Aim: explain the features and uses of common application software for organisations', {x: M, y: 1.3, w: W - 2 * M, h: 0.4, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 table(s, ['Application', 'Used for', 'Example organisation'], [
  ['Productivity (word processor, spreadsheet, presentation)', 'documents, budgets, reports', 'any office'],
  ['Database / DBMS', 'store and query structured data', 'a library catalogue'],
  ['CRM', 'customer records, sales, follow-ups', 'a car dealer'],
  ['Collaboration and communication', 'chat, video calls, shared files', 'a remote team'],
  ['Graphics, video and design', 'images, video editing, CAD', 'a marketing agency'],
  ['Web browser and web apps', 'online services and SaaS', 'every user']], {x: M, y: 1.85, w: 8.0, colW: [3.2, 2.7, 2.1]});
 card(s, 8.95, 1.85, 3.78, 2.2, 'Exam angle', 'Pick software for a scenario and justify it by the organisation’s needs, cost, licensing and compatibility.', C.mint, C.teal, 13);
 card(s, 8.95, 4.25, 3.78, 2.2, 'Task', 'Workbook SW4: choose three applications for a small charity and justify each. Check: Quiz 3.', C.sand, C.navy, 13);
 notes(s, ['Discuss licensing models: perpetual, subscription, open source, freeware.', 'Stretch: off-the-shelf vs bespoke software.']);
}

divider('7.3 Networks', 'Why network · types · connectivity · topologies · models · components · OSI and TCP/IP · packets · protocols · bandwidth and latency');

lessonSplit('7.3.1–2', 'Why network, and network types', 'networks_from_personal_to_worldwide', 'explain the benefits and drawbacks of networks and the features of PAN, LAN, WLAN, MAN, WAN, VPN',
 ['Benefits: share resources, data, communication, central management', 'Drawbacks: cost, security risk, single points of failure, needs skills', 'Types by scale: PAN, LAN, WLAN, MAN, WAN', 'VPN: an encrypted tunnel across the internet'],
 [['Starter', 'List every network you used today, from earbuds to the internet.'], ['Task', 'Workbook N1: pick network types for five organisations.'], ['Check', 'Quiz 4a.']],
 ['Question: why would a council use a MAN rather than leased WAN links?', 'Support: types table on the Learn page. Stretch: SAN and the difference from NAS.', 'Video (lesson N1): Network types and performance.'], 'a_vpn_tunnel_across_the_internet');

lessonSplit('7.3.3', 'Connectivity methods', 'copper_fibre_and_wireless_compared', 'compare wired and wireless connectivity methods',
 ['Copper twisted pair: cheap, 100 m, interference', 'Fibre: fast, long distance, immune to EMI, costly', 'Wi-Fi: mobility; range, interference, security', 'Bluetooth, NFC, cellular 4G/5G, satellite', 'Choose by speed, distance, cost, security, mobility'],
 [['Starter', 'Why is the college backbone fibre but your desk copper?'], ['Practical', 'Packet Tracer: wired and wireless with WPA2 (Learn page N2).'], ['Task', 'Workbook N2.']],
 ['Use real examples: rural broadband by 4G/satellite; undersea fibre.', 'Question: when would you choose wired over Wi-Fi in an office?', 'Video (lesson N2): The Ethernet and Wi-Fi protocols.']);

lessonSplit('7.3.4–5', 'Topologies and network models', 'six_physical_network_topologies', 'compare topologies and the peer-to-peer, client–server and thin client models',
 ['Bus, ring, star, extended star, mesh, hybrid', 'Star: faults isolated; switch is a single point of failure', 'Mesh: many paths, resilient, costly', 'Peer-to-peer vs client–server vs thin client'],
 [['Starter', 'Which topology does the classroom use? Draw it.'], ['Practical', 'Practical 6: build and test a LAN.'], ['Task', 'Workbook N3: choose a model for a hairdresser and a college.']],
 ['Exam angle: benefits and drawbacks for a named organisation.', 'Question: why does a thin client model suit a call centre?', 'Stretch: logical vs physical topology.'], 'peer_to_peer_client_server_and_thin_clie');

lessonSplit('7.3.6', 'Network components and the backbone', 'from_a_home_network_to_the_internet_back', 'explain the roles of servers, clients, switches, routers, the internet connection and backbone',
 ['Server vs client; common server types', 'Switch: LAN, MAC addresses', 'Router: between networks, IP addresses', 'Internet connection to an ISP', 'Backbone: tier 1 networks, IXPs, undersea cables'],
 [['Practical', 'Practical 7: home network to the internet via cable and DSL.'], ['Task', 'Workbook N4.'], ['Check', 'Exit: switch vs router in two sentences.']],
 ['Use the teacher’s cloud-with-cable-and-modem.pkt file for the practical.', 'Question: what happens to your traffic between your router and a US website?', 'Starter idea: the submarine cable map.'], 'how_a_switch_learns_mac_addresses');

lessonSplit('7.3.7–8', 'The OSI and TCP/IP models', 'the_osi_model_beside_the_tcp_ip_model', 'describe the layers, functions and related protocols of the OSI and TCP/IP models',
 ['OSI: 7 layers; mnemonic', 'TCP/IP: application, transport, internet, network access', 'Encapsulation adds a header at each layer', 'Devices by layer: switch 2, router 3', 'Why layers: standards, interoperability, troubleshooting'],
 [['Starter', 'Mnemonic race: seven layers both ways.'], ['Task', 'Workbook N5: place protocols in layers.'], ['Check', 'Quiz 4b.']],
 ['Build the envelope-in-a-parcel analogy for encapsulation.', 'Question: at which layer does a web browser work? A cable?', 'Video (lesson N5): Network protocols and the 4-layer model.'], 'encapsulation_as_data_moves_down_the_lay');

lessonSplit('7.3.9', 'Data packets', 'the_structure_of_a_data_packet', 'describe packet structure, packet switching, packet loss and CRC',
 ['Header: source/destination IP, sequence number, TTL', 'Payload: the data; trailer: CRC', 'Packet switching: independent routes, reassembly', 'Loss: congestion, faults, interference, TTL expiry', 'CRC detects corruption; TCP re-sends'],
 [['Starter', 'Tear a message into numbered strips, pass by different routes.'], ['Practical', 'Packet Tracer simulation: open a PDU.'], ['Task', 'Workbook N6.']],
 ['The packet-strip starter makes sequence numbers and loss memorable.', 'Question: why can packets arrive out of order?', 'Video (lesson N6): Check digits and parity bits.'], 'packets_taking_different_routes_across_a');

{
 const s = pres.addSlide(); chip(s, '7.3.10'); title(s, 'Network protocols', {y: 0.55, size: 28});
 s.addText('Aim: explain the role of common network, routing and application protocols', {x: M, y: 1.3, w: W - 2 * M, h: 0.4, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 table(s, ['Protocol', 'Role', 'Port'], [
  ['TCP / UDP', 'reliable, ordered delivery / fast, no re-sending', '–'],
  ['IP', 'addressing and routing packets', '–'],
  ['HTTP / HTTPS', 'web pages / encrypted with TLS', '80 / 443'],
  ['FTP / SFTP', 'file transfer / secure file transfer', '21 / 22'],
  ['SMTP · POP · IMAP', 'send mail · download mail · sync mail', '25 · 110 · 143'],
  ['DHCP · DNS', 'automatic addresses · names to IP addresses', '67/68 · 53'],
  ['RIP · OSPF', 'routing protocols: share routes between routers', '–']], {x: M, y: 1.85, w: 7.4, colW: [1.9, 4.2, 1.3], fontSize: 12});
 img(s, 'how_dns_finds_the_ip_address_for_a_name', 8.3, 1.85, 4.43, 2.2);
 card(s, 8.3, 4.35, 4.43, 2.2, 'Practicals', 'Practical 5: command-line tools (ipconfig, ping, arp, netstat, tracert). Practical 8: routing with RIP.', C.mint, C.teal, 13);
 notes(s, ['Run the command-line practical live first: students record their own IP, gateway, DHCP and DNS servers.', 'Question: which email protocol suits someone with a phone and a laptop? (IMAP)', 'Videos (lesson N7): TCP, IP, HTTP/S and FTP; Email protocols.']);
}

lessonSplit('7.3.11', 'Bandwidth and latency', 'bandwidth_and_latency_as_a_pipe', 'explain bandwidth and latency and their effect on performance',
 ['Bandwidth: maximum data rate (Mbps)', 'Latency: delay (ms); jitter: variation', 'Throughput: what you actually get', 'Real-time services need low latency', 'Time = size ÷ speed (same units)'],
 [['Starter', 'Why does an online game lag with fast broadband?'], ['Task', 'Workbook N8: download-time calculations.'], ['Check', 'Quiz 4c.']],
 ['Worked example: 400 Mb at 50 Mbps = 8 s; watch bits vs bytes.', 'Use tracert and ping times from Practical 5 to show latency.', 'Stretch: QoS prioritising voice and video.']);

divider('7.4 Virtual · 7.5 Cloud · 7.6 Resilience', 'Virtual machines and hypervisors · cloud types and delivery models · keeping digital environments working');

lessonSplit('7.4', 'Virtual environments', 'type_1_and_type_2_hypervisors', 'explain VMs, hypervisors, key features, benefits and drawbacks',
 ['VM clients and servers; virtual switches and routers', 'Type 1 (bare metal) vs type 2 (hosted)', 'Features: security, managed execution, sharing, aggregation, emulation, isolation, portability', 'Benefits vs drawbacks (host load, slower, misleading performance)'],
 [['Practical', 'Practical 9: create a VM and restore a snapshot.'], ['Task', 'Workbook V1.'], ['Check', 'Quiz 5a.']],
 ['The spec lists seven key features by name: students should learn them all.', 'Question: why do schools virtualise their test servers?', 'Exam practice 2 has a 9-mark virtualisation question.'], 'virtual_clients_switch_and_router_inside');

lessonWide('7.5', 'Cloud environments', 'who_manages_what_in_iaas_paas_and_saas', 'compare private and public clouds, explain the benefits, and the IaaS, PaaS, SaaS responsibility split',
 [['Starter', 'Which cloud services have you used today?'], ['Practical', 'Practical 10: responsibility card sort; API demo with Postman.'], ['Check', 'Quiz 5b and Exam practice 2, question 2.']],
 ['Teach the split exactly as the specification: IaaS client manages application software, system software, runtime, data and user accounts; PaaS client manages application software, data and user accounts; SaaS client manages user accounts and data.', 'Benefits: portability, elasticity, fewer storage limits, cost effectiveness.', 'Question: which model for a developer who does not want to patch servers? (PaaS)']);

lessonSplit('7.6', 'Resilient digital environments', 'hot_warm_and_cold_standby_sites', 'explain the benefits of resilience and the methods used to improve it',
 ['Benefits: security, reputation, reduced downtime', 'Updates, patches and hardware replacement; secure disposal', 'Redundancy (RAID, dual power, links); device hardening', 'Backups onsite, offsite, cloud; tested recovery', 'Hot, warm and cold sites; SOPs and staff training'],
 [['Practical', 'Practical 11: a resilience plan for a small business.'], ['Task', 'Workbook R1.'], ['Check', 'Quiz 5c.']],
 ['Evaluate by cost vs risk: a hospital needs a hot site; a café may rely on cloud backups.', 'Videos (lesson R1): Cisco Anatomy of an IoT Attack; Anatomy of an Attack; Port of Long Beach automated terminal.'], 'how_raid_0_1_and_5_place_data_across_dri');

// Practicals overview
{
 const s = pres.addSlide(); title(s, 'Twelve practicals on the student site');
 const labs = ['PC disassemble and reassemble', 'Motherboard ID and connectors', 'Hardware spider diagram', 'Number systems practice', 'Command-line network tools', 'Build and test a LAN', 'Home network to the internet', 'Routing with RIP', 'Create a virtual machine', 'Cloud responsibilities and APIs', 'Resilience plan', 'Cisco Intro to IoT badge'];
 labs.forEach((t, i) => {
  const col = i % 6, row = Math.floor(i / 6), w = (W - 2 * M - 0.2 * 5) / 6, x = M + col * (w + 0.2), y = 1.6 + row * 2.45;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y, w, h: 2.2, fill: {color: row ? C.mint : C.tint}, line: {color: row ? C.mint : C.tint}, rectRadius: 0.12});
  s.addText(String(i + 1), {x: x + 0.2, y: y + 0.15, w: 1, h: 0.8, fontFace: HEAD, fontSize: 36, bold: true, color: C.teal, margin: 0, isTextBox: true});
  s.addText(t, {x: x + 0.2, y: y + 1.0, w: w - 0.4, h: 1.05, fontFace: BODY, fontSize: 15, bold: true, color: C.ink, margin: 0, isTextBox: true, valign: 'top'});
 });
 footer(s, 'Each practical lists steps, how to check it works and what to keep for revision. Teacher .pkt files and task sheets stay on Teams.');
 notes(s, ['Map: 1–3 lesson H1/H2 · 4 NS · 5 N7 · 6–7 N4 · 8 N7 · 9 V1 · 10 C1 · 11 R1 · 12 H1.', 'Anti-static precautions and unplugging are essential for Practical 1.', 'Only run network commands on the college lab network.']);
}

// Exam technique and revision
{
 const s = pres.addSlide(); title(s, 'Revision and exam technique');
 const steps = ['RAG the spec', 'Re-learn reds', 'Quiz', 'Exam practice', 'Mark with levels', 'Re-do'];
 const w = (W - 2 * M - 0.2 * 5) / 6;
 steps.forEach((t, i) => {
  const x = M + i * (w + 0.2);
  s.addShape(pres.shapes.CHEVRON, {x, y: 1.6, w, h: 0.9, fill: {color: i % 2 ? C.teal : C.navy}, line: {color: C.white}});
  s.addText(t, {x: x + 0.35, y: 1.6, w: w - 0.6, h: 0.9, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 13, bold: true, color: C.white, margin: 0, isTextBox: true});
 });
 card(s, M, 2.9, 3.9, 2.3, 'Developed points', 'Point → because → so for this business → link to the question. One developed point beats three listed ones.', C.tint, C.navy, 14);
 card(s, M + 4.1, 2.9, 3.9, 2.3, 'Weak → strong', '“Cloud is cheaper.”\n→ “The shop avoids buying servers and pays only for what it uses, so its costs fall in quiet months.”', C.mint, C.teal, 14);
 card(s, M + 8.2, 2.9, 3.93, 2.3, 'Timing', 'About 1 minute per mark. Plan long answers for 2–3 minutes: for, against, judgement.', C.sand, C.navy, 14);
 notes(s, ['Weeks 32–33: use the Course guide RAG checklist to target revision; students re-take quizzes until green.', 'Exam practice 1 and 2 on the site, then an official sample paper under timed conditions.']);
}

// Closing
{
 const s = pres.addSlide(); s.background = {color: C.navy};
 s.addText('Ready to deliver', {x: M, y: 1.2, w: 7, h: 1.0, fontFace: HEAD, fontSize: 42, bold: true, color: C.white, margin: 0, isTextBox: true});
 bullets(s, ['Share the start page link in Teams', 'Lesson 1: tour the site and the RAG checklist', 'One practical every week or two', 'Quizzes as starters and exit checks', 'Exam practice from spring term'], M, 2.4, 6.6, 3.5, 18, C.white);
 const ch = fitH('tcp_ip_layers_with_example_protocols', 5.03);
 s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 7.4, y: 2.4, w: 5.33, h: ch + 0.3, fill: {color: C.white}, line: {color: C.white}, rectRadius: 0.15});
 img(s, 'tcp_ip_layers_with_example_protocols', 7.55, 2.55, 5.03, 2.45);
 notes(s, ['Site: ' + SITE, 'The AI tutor depends on the college Azure subscription being active; the rest of the site works without it.']);
}

pres.writeFile({fileName: path.join(process.env.OUT || __dirname, 'Unit7-Digital-Environments-Teacher-Deck.pptx')}).then(f => console.log('wrote', f));
