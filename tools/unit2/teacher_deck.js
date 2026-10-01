// Unit 2 Fundamentals of Computer Systems: teacher delivery deck (original content).
// Figures are PNG exports of the Learn page diagrams: set FIGS to their folder (with dims.json).
const pptxgen = require('pptxgenjs');
const path = require('path');
const FIGS = process.env.FIGS || path.join(__dirname, 'figs');
const DIMS = require(path.join(FIGS, 'dims.json'));
const FIG = n => path.join(FIGS, n + '.png');

const C = {navy: '0E3B43', teal: '1F8A70', amber: 'F2A541', ink: '17334B', muted: '4F6577', tint: 'EAF2F9', mint: 'E6F4EE', white: 'FFFFFF', line: 'C9D7E3', sand: 'FDF1E7'};
const HEAD = 'Cambria', BODY = 'Calibri';
const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.333 x 7.5
pres.author = 'Unit 2 course team';
pres.title = 'Unit 2 Fundamentals of Computer Systems: teacher delivery deck';
const W = 13.333, H = 7.5, M = 0.6;
const SITE = 'nigeriastudentcenter.github.io/btech/start.html';

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
 s.addText('Unit 2', {x: M, y: 1.2, w: 6, h: 0.6, fontFace: BODY, fontSize: 20, bold: true, color: C.amber, margin: 0, isTextBox: true});
 s.addText('Fundamentals of Computer Systems', {x: M, y: 1.75, w: 6.4, h: 1.6, fontFace: HEAD, fontSize: 40, bold: true, color: C.white, margin: 0, isTextBox: true, valign: 'top'});
 s.addText('Teacher delivery deck · BTEC Level 3 Nationals in Computing', {x: M, y: 3.5, w: 6.2, h: 0.8, fontFace: BODY, fontSize: 18, color: 'CDEBE3', margin: 0, isTextBox: true, valign: 'top'});
 s.addText('Hardware · Software · Architecture · Data · Transmission · Logic', {x: M, y: 4.4, w: 6.2, h: 0.5, fontFace: BODY, fontSize: 16, italic: true, color: C.white, margin: 0, isTextBox: true});
 const th = fitH('motherboard_identification_diagram', 4.2);
 s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 7.6, y: 3.6 - Math.min(th, 5.6) / 2 - 0.15, w: 4.6, h: Math.min(th, 5.6) + 0.3, fill: {color: C.white}, line: {color: C.white}, rectRadius: 0.15});
 img(s, 'motherboard_identification_diagram', 7.8, 3.6 - Math.min(th, 5.6) / 2, 4.2, 5.6);
 notes(s, ['Purpose: this deck supports delivery of Unit 2 alongside the student pack (' + SITE + ').', 'Lesson slides follow the college routine: starter, aim, teach, practical, task, check, flipped homework.', 'Each slide points to the matching Learn section, diagram task, video and revision test.']);
}

// 2 How each lesson runs
{
 const s = pres.addSlide(); title(s, 'How each lesson runs');
 const steps = [['Starter', 'Millionaire, matching game or recap quiz'], ['Aim', 'share the aim and spec point'], ['Teach', 'diagram-led explanation'], ['Practical', 'diagram task, hands-on or worked example'], ['Task', 'workbook activity with the AI tutor'], ['Check', 'exam-style question'], ['Homework', 'flipped: preview the next deck']];
 const w = (W - 2 * M - 0.15 * 6) / 7;
 steps.forEach(([h, b], i) => {
  const x = M + i * (w + 0.15);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y: 1.7, w, h: 2.2, fill: {color: i % 2 ? C.tint : C.mint}, line: {color: C.line}, rectRadius: 0.1});
  s.addShape(pres.shapes.OVAL, {x: x + w / 2 - 0.35, y: 1.9, w: 0.7, h: 0.7, fill: {color: C.navy}, line: {color: C.navy}});
  s.addText(String(i + 1), {x: x + w / 2 - 0.35, y: 1.9, w: 0.7, h: 0.7, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 18, bold: true, color: C.white, margin: 0, isTextBox: true});
  s.addText([{text: h, options: {bold: true, fontSize: 15, color: C.navy, breakLine: true}}, {text: b, options: {fontSize: 12, color: C.ink}}], {x: x + 0.1, y: 2.75, w: w - 0.2, h: 1.35, align: 'center', valign: 'top', fontFace: BODY, margin: 0, isTextBox: true});
 });
 card(s, M, 4.3, 6.0, 1.5, 'Keep your starters', 'The Millionaire, Hollywood Squares and matching-game starters, quiz QR codes and cheat sheets stay on Teams and work alongside the site.');
 card(s, 6.9, 4.3, 5.83, 1.5, 'End with exam practice', 'Finish each topic with an exam-style question from the Revision tests or the Past Exam Papers page, where the tutor gives hints without writing answers.', C.mint);
 notes(s, ['The revision and past-paper pages mirror the external exam, so use them weekly rather than only at the end.']);
}

// 3 At a glance
{
 const s = pres.addSlide(); title(s, 'Unit 2 at a glance');
 const stats = [['90', 'guided learning hours'], ['1', 'external written exam'], ['6', 'topic areas: A–F'], ['16', 'Learn sections'], ['9', 'diagram tasks']];
 const w = (W - 2 * M - 0.25 * 4) / 5;
 stats.forEach(([n, l], i) => {
  const x = M + i * (w + 0.25);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y: 1.6, w, h: 2.1, fill: {color: i === 1 ? C.navy : C.tint}, line: {color: i === 1 ? C.navy : C.tint}, rectRadius: 0.12});
  s.addText(n, {x, y: 1.75, w, h: 1.1, align: 'center', fontFace: HEAD, fontSize: 60, bold: true, color: i === 1 ? C.white : C.teal, margin: 0, isTextBox: true});
  s.addText(l, {x: x + 0.15, y: 2.85, w: w - 0.3, h: 0.7, align: 'center', fontFace: BODY, fontSize: 14, color: i === 1 ? C.white : C.ink, margin: 0, isTextBox: true});
 });
 const areas = [['A', 'Hardware and software'], ['B', 'Computer architecture'], ['C', 'Data representation'], ['D', 'Data organisation'], ['E', 'Data transmission'], ['F', 'Logic and data flow']];
 const w2 = (W - 2 * M - 0.2 * 5) / 6;
 areas.forEach(([a, t], i) => card(s, M + i * (w2 + 0.2), 4.1, w2, 1.7, `Topic ${a}`, t, [C.tint, C.mint, C.sand][i % 3], C.navy, 13));
 footer(s, 'Externally assessed. Check the current exam length, marks and dates with Pearson; examiner reports since 2017 are in the unit folder on Teams.');
 notes(s, ['Use the examiner reports to pick out recurring weaknesses: generic answers not applied to the scenario, confusing similar terms (RAM/ROM, serial/parallel), and incomplete working in number questions.']);
}

// 4 Exam technique
{
 const s = pres.addSlide(); title(s, 'Exam technique from the examiner reports');
 table(s, ['Command word', 'What students must do'], [
  ['State / identify / give', 'a short, precise fact'],
  ['Describe', 'features or steps, one mark per accurate point'],
  ['Explain', 'a point plus why/how, linked to the scenario'],
  ['Calculate / convert', 'show every step of working'],
  ['Discuss / evaluate', 'both sides, applied to the scenario, with a supported judgement']], {x: M, y: 1.45, w: 7.4, colW: [2.3, 5.1]});
 card(s, 8.3, 1.45, 4.43, 2.4, 'Recurring weaknesses', '• answers not applied to the scenario\n• mixing up similar terms\n• missing working in conversions\n• lists instead of developed points', C.sand, 'A3560B', 13);
 card(s, 8.3, 4.05, 4.43, 2.3, 'In the pack', 'Revision tests 1–4 (guided to long answers) and five past papers with tutor help modes: start, check and plan.', C.mint, C.teal, 13);
 notes(s, ['Model one developed point per lesson: point, explain, apply to the scenario.']);
}

// 5 Student pack
{
 const s = pres.addSlide(); title(s, 'The student pack');
 const pages = [['1. Brief', 'the practice brief and success criteria'], ['2. Learn', '16 sections, ‘Go deeper’ diagrams, ‘From your lessons’ blocks and videos'], ['3. Workbook + tutor', 'an activity per section with the AI tutor'], ['4. Revision', 'four tests: guided, independent, deeper, long answers'], ['5. Past Exam Papers', 'five Pearson papers with tutor help'], ['6. Diagram tasks', 'your labelling worksheets as drop-down tasks'], ['7. Videos', '57 videos including the MrBrownCS revision series'], ['Teachers', 'this deck, the topic map, tutor notes']];
 pages.forEach(([h, b], i) => card(s, M + (i % 4) * 3.07, 1.5 + Math.floor(i / 4) * 2.4, 2.9, 2.15, h, b, i % 2 ? C.mint : C.tint, C.navy, 13));
 footer(s, 'Link for Teams: ' + SITE + ' · No accounts; work saves in the browser.');
 notes(s, ['Tour the pack in the first lesson. Show the backup download on shared PCs.']);
}

// 6 AI tutor
{
 const s = pres.addSlide(); title(s, 'The AI study tutor');
 card(s, M, 1.5, 5.9, 3.4, 'Students can ask it to…', '• explain a topic another way\n• diagnose a misunderstanding with one question\n• give one hint at a time\n• set new practice questions\n• help start, check or plan a past-paper answer', C.mint, C.teal, 14);
 card(s, 6.83, 1.5, 5.9, 3.4, 'It is set up to…', '• not give answers to the workbook’s own activities\n• use different numbers from the activity\n• never invent official mark schemes\n• reply in plain English\n• store nothing on the server; no names', C.sand, 'A3560B', 14);
 card(s, M, 5.15, W - 2 * M, 1.35, 'Live now', 'The tutor runs on the college Azure AI service with shared usage limits. If it is ever offline, every page still works.', C.tint, C.navy, 13);
 notes(s, ['Encourage “Hint” mode during lessons and “Practice” mode for homework.']);
}

// 7 Delivery plan
{
 const s = pres.addSlide(); title(s, 'Delivery plan by topic');
 const phases = [['A1–A3', 'hardware, software, data processing'], ['B1–B3', 'architecture, CPU, registers, interrupts'], ['C1–C3', 'numbers, text, images'], ['D1–D2', 'data structures, matrices'], ['E1–E3', 'transmission, encryption, errors'], ['F1–F2', 'logic, flowcharts, system diagrams']];
 const w = (W - 2 * M) / 6;
 s.addShape(pres.shapes.LINE, {x: M, y: 2.35, w: W - 2 * M, h: 0, line: {color: C.navy, width: 3}});
 phases.forEach(([h, b], i) => {
  const x = M + i * w, f = [C.tint, C.mint, C.sand][i % 3];
  s.addShape(pres.shapes.OVAL, {x: x + w / 2 - 0.18, y: 2.17, w: 0.36, h: 0.36, fill: {color: C.teal}, line: {color: C.white, width: 2}});
  s.addText(h, {x, y: 1.5, w, h: 0.5, align: 'center', fontFace: BODY, fontSize: 15, bold: true, color: C.navy, margin: 0, isTextBox: true});
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: x + 0.08, y: 2.8, w: w - 0.16, h: 2.3, fill: {color: f}, line: {color: f}, rectRadius: 0.1});
  s.addText(b, {x: x + 0.22, y: 2.95, w: w - 0.44, h: 2.0, fontFace: BODY, fontSize: 14, color: C.ink, valign: 'top', margin: 0, isTextBox: true});
 });
 footer(s, 'Follow your scheme of work dates; leave the final weeks for revision tests, past papers and the sample assessment material.');
 notes(s, ['The Unit 2 scheme of work and outline are in the unit management folder on Teams.']);
}

divider('A · Hardware and software', 'Computer types, components, connectors and ports, servers, storage, operating systems and data processing');

lessonSplit('A1', 'Inside a computer system', 'labelled_top_down_view_of_a_desktop_moth', 'identify internal components and explain their purpose, features and uses',
 ['Motherboard, CPU, RAM, ROM, storage, PSU, GPU', 'Purpose + feature + use for each component', 'Types of computer and mobile devices', 'Factors affecting the choice of hardware'],
 [['Practical', 'PC disassembly; Diagram tasks 1, 4 and 5.'], ['Task', 'Workbook A1; PC component selection task.'], ['Check', 'Exam question on choosing hardware.']],
 ['Use the Motherboard ID task (now Diagram task 1 on the site) after the disassembly practical.', 'Videos (A1): Main memory; Secondary storage; Embedded systems.'], 'motherboard_identification_diagram');

lessonSplit('A1', 'Connectors, ports and servers', 'seven_computer_connectors_to_identify', 'identify connectors and ports and explain the functions of servers',
 ['ATX 24/20-pin, EPS 4/8-pin, PCIe 6/8-pin', 'SATA, Molex, Berg', 'USB-A/C, HDMI, DisplayPort, VGA, DVI, RJ45', 'File, print, web, mail, database, authentication servers'],
 [['Practical', 'Diagram tasks 2 and 3.'], ['Task', '‘From your lessons · A1’ tables.'], ['Check', 'Name the server for each scenario.']],
 ['The connectors and ports tasks redraw your Word worksheets as drop-down tasks with instant marking.', 'Video (A1): Network hardware.'], 'ten_ports_to_identify');

lessonSplit('A1', 'Storage, RAID, NAS and SAN', 'how_raid_0_1_and_5_place_data_across_dri', 'compare storage and explain RAID, NAS and SAN',
 ['Memory and storage hierarchy', 'HDD vs SSD', 'RAID 0, 1, 5 (and 10)', 'NAS vs SAN; cluster storage'],
 [['Practical', 'Diagram task 9: RAID levels.'], ['Task', 'Workbook A1 storage activity.'], ['Check', 'RAID choice for a scenario.']],
 ['Use the NAS and RAID notes from Teams.', 'Video (A1): PowerCert, What is RAID 0, 1, 5 and 10?']);

lessonSplit('A2', 'Operating systems and the kernel', 'user_shell_kernel_and_hardware', 'explain the role of the OS and kernel, interfaces, utilities and open source',
 ['Kernel: execution, interrupts, memory, scheduling, devices', 'OS networking and security: home vs organisation', 'GUI, CLI, menu, voice: choosing an interface', 'Utilities, applications, open source, disk cache'],
 [['Starter', 'Kernel crossword (link on Teams).'], ['Task', 'Workbook A2.'], ['Check', 'Open source vs proprietary exam question.']],
 ['Decks 1–10 in Presentations Software map to Learn A2 and its ‘From your lessons’ block.', 'Videos (A2): Operating System; What is a kernel?; Utility software; Open source explained.'], 'timeline_of_multitasking_with_time_slice');

lessonSplit('A3', 'Data processing', 'the_stages_of_data_processing_from_colle', 'explain how data is collected, processed, shared and backed up',
 ['Collection methods and validation', 'Processing: sort, search, aggregate, calculate', 'Data across multiple systems', 'Backups: full, incremental, differential'],
 [['Task', 'Workbook A3.'], ['Practical', 'Data processing homework (Teams).'], ['Check', 'Revision test question on processing.']],
 ['Videos (A3): Databases; Client–server and peer-to-peer networks.'], 'full_incremental_and_differential_backup');

divider('B · Computer architecture', 'Von Neumann and Harvard, the fetch–decode–execute cycle, pipelining, registers and interrupts');

lessonSplit('B1', 'Approaches to architecture', 'von_neumann_and_harvard_architectures_co', 'compare Von Neumann, Harvard, clusters and NUMA',
 ['Stored-program concept', 'Separate instruction and data memories', 'Clusters and parallel processing', 'Uniform vs non-uniform memory access'],
 [['Task', 'Workbook B1.'], ['Check', 'Revision test 3 (deeper) B1 set.'], ['Homework', 'Preview B2 deck.']],
 ['Videos (B1): CPU and Von Neumann; Harvard vs Von Neumann; contemporary CPUs.'], 'a_computer_cluster_sharing_one_big_job');

lessonSplit('B2', 'Microarchitecture: FDE and pipelining', 'the_fetch_decode_execute_cycle', 'explain the fetch–decode–execute cycle, pipelining, cores and cache',
 ['Fetch, decode, execute', 'Pipelining overlaps stages', 'Cores, threads and cache', 'Why 4 cores ≠ 4× faster'],
 [['Starter', 'Act out the FDE cycle with students as registers.'], ['Task', 'Workbook B2.'], ['Check', 'Exam question on CPU performance.']],
 ['Videos (B2): Purpose of the CPU; Factors affecting CPU performance; Computerphile CPU pipeline (stretch).'], 'instructions_overlapping_in_a_three_stag');

lessonSplit('B3', 'Registers, buses and interrupts', 'registers_inside_the_cpu_and_the_buses_t', 'trace registers through a fetch and explain interrupts',
 ['PC, MAR, MDR, CIR, ACC', 'Address, data and control buses', 'Interrupt handling and priorities', 'Saving and restoring registers'],
 [['Practical', 'Diagram task 7: Von Neumann computer.'], ['Task', 'Workbook B3 register trace.'], ['Check', 'Revision test question on registers.']],
 ['Videos (B3): Special-purpose registers; Address, data and control buses; how interrupts work (stretch).'], 'von_neumann_computer_to_label');

divider('C and D · Data', 'Number systems, text, images, data structures and matrices');

lessonSplit('C1', 'Number systems and arithmetic', 'converting_a_byte_between_binary_hexadec', 'convert between bases, use BCD and do binary arithmetic',
 ['Binary, octal, decimal, hexadecimal', 'Recognising a base from its digits', 'BCD', 'Addition, subtraction, shifts'],
 [['Starter', 'Cisco Binary Game / number systems quiz.'], ['Practical', 'Diagram task 6: which number base?'], ['Check', 'Numbers competence test.']],
 ['Use the numbers booklet and binary mathematics end test on Teams.', 'Videos (C1): Introduction to binary; conversions; addition; hex and binary; shifts.'], 'adding_two_binary_bytes');

lessonSplit('C1', 'Negative numbers and floating point', 'eight_bit_two_x27_s_complement_place_val', 'represent negative numbers and real numbers in binary',
 ['Sign and magnitude', 'Two’s complement and range', 'Mantissa and exponent', 'Precision vs range'],
 [['Task', 'Signed binary worksheet (Teams).'], ['Check', 'Revision test 3 C1 set.'], ['Homework', 'Floating point deck.']],
 ['Videos (C1): Signed binary; floating point (stretch); BCD.'], 'a_floating_point_number_made_of_a_mantis');

lessonSplit('C2–C3', 'Text and images', 'unicode_characters_and_how_many_utf_8_by', 'explain ASCII, Unicode, bitmap images and compression',
 ['ASCII and extended ASCII', 'Unicode and UTF-8', 'Pixels, resolution, colour depth', 'File size; RLE compression'],
 [['Task', 'Workbook C2 and C3.'], ['Check', 'Image file size calculation.'], ['Homework', 'Image representation deck.']],
 ['Videos (C2, C3): Text in binary; images in binary; sound; lossy and lossless compression.'], 'run_length_encoding_of_one_row_of_pixels');

lessonSplit('D1–D2', 'Data structures and matrices', 'a_stack_and_a_queue_side_by_side', 'use stacks, queues, arrays, lists and matrices',
 ['Stack (LIFO), queue (FIFO)', 'Arrays and linked lists', 'Row-major storage', 'Matrix addition, multiplication, transformations'],
 [['Task', 'Workbook D1 and D2; matrices worksheet.'], ['Check', 'Indices and matrices questions.'], ['Homework', 'D revision questions.']],
 ['Videos (D1, D2): Data structures; stacks and queues; how to multiply matrices.'], 'multiplying_two_matrices_row_by_column');

divider('E and F · Transmission and logic', 'Channels, encryption, VoIP, error detection and correction, logic gates and data flow');

lessonSplit('E1', 'Transmitting data and encryption', 'serial_and_parallel_transmission_of_one_', 'explain transmission methods, protocols, encryption and VoIP',
 ['Simplex, half and full duplex', 'Serial vs parallel; synchronous vs asynchronous', 'Caesar, Vigenère, public key', 'VoIP: codecs, packets, jitter'],
 [['Practical', 'Vigenère cipher worksheet (Teams).'], ['Task', 'Workbook E1.'], ['Check', 'E revision questions.']],
 ['Videos (E1): Serial and parallel; synchronous and asynchronous; encryption; Vigenère.'], 'vigen_re_cipher_worked_example');

lessonSplit('E2–E3', 'Detecting and correcting errors', 'arq_asks_again_while_fec_sends_correctio', 'explain parity, checksums, CRC, ARQ and FEC',
 ['Causes of errors', 'Parity and checksums', 'CRC', 'ARQ vs FEC: when to use each'],
 [['Task', 'Workbook E2 and E3.'], ['Check', 'Error correction exam question.'], ['Homework', 'Error correction deck.']],
 ['Videos (E2, E3): Check digits and parity; Computerphile CRC and error correction; Hamming codes (stretch).'], 'even_parity_counts_the_number_of_ones');

lessonSplit('F1', 'Logic gates and Boolean logic', 'the_six_logic_gates_with_their_symbols_n', 'use gates, truth tables, expressions and adders',
 ['AND, OR, NOT, NAND, NOR, XOR', 'Truth tables and expressions', 'Half and full adders', 'Universal gates; three-state logic'],
 [['Practical', 'Diagram task 8: logic gate symbols.'], ['Task', 'Logic questions (Teams); Workbook F1.'], ['Check', 'Dog day-care truth table question.']],
 ['Use the logic booklet with the site’s gate gallery.', 'Videos (F1): Logic gates; half and full adder; Boolean algebra (stretch).'], 'six_logic_gate_symbols_to_identify');

lessonSplit('F2', 'Flowcharts and system diagrams', 'flowchart_for_topping_up_a_bus_pass_with', 'read and draw flowcharts and system diagrams',
 ['Flowchart symbols', 'Tracing with normal and edge cases', 'System diagrams: inputs, processes, outputs, storage', 'Explaining a diagram in words'],
 [['Task', 'Workbook F2.'], ['Check', 'Reward-system flowchart question.'], ['Homework', 'Revision test 2.']],
 ['Videos (F2): Flowcharts; Data flow diagrams.'], 'system_diagram_of_a_school_canteen_payme');

// Diagram tasks overview
{
 const s = pres.addSlide(); title(s, 'Nine diagram tasks on the site');
 const labs = ['Motherboard ID', 'Power connectors', 'Ports', 'Mobile devices', 'Internal components', 'Which number base?', 'Von Neumann computer', 'Logic gate symbols', 'RAID levels'];
 labs.forEach((t, i) => {
  const col = i % 5, row = Math.floor(i / 5), w = (W - 2 * M - 0.25 * 4) / 5, x = M + col * (w + 0.25), y = 1.6 + row * 2.45;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y, w, h: 2.2, fill: {color: row ? C.mint : C.tint}, line: {color: row ? C.mint : C.tint}, rectRadius: 0.12});
  s.addText(String(i + 1), {x: x + 0.2, y: y + 0.15, w: 1, h: 0.8, fontFace: HEAD, fontSize: 36, bold: true, color: C.teal, margin: 0, isTextBox: true});
  s.addText(t, {x: x + 0.2, y: y + 1.0, w: w - 0.4, h: 1.05, fontFace: BODY, fontSize: 15, bold: true, color: C.ink, margin: 0, isTextBox: true, valign: 'top'});
 });
 footer(s, 'Your Word labelling worksheets, redrawn as original diagrams with drop-down answers, instant marking and links to the lesson and tutor.');
 notes(s, ['Tasks 1–6 come from the Hardware and Number Systems worksheets; 7–9 are new, from the architecture, logic and RAID lessons.', 'Use them as starters, plenaries or homework; choices save on the student’s device.']);
}

// Revision
{
 const s = pres.addSlide(); title(s, 'Revision and the exam');
 const steps = ['Learn section', 'Diagram task', 'Workbook + tutor', 'Revision tests', 'Past papers', 'Examiner tips'];
 const w = (W - 2 * M - 0.2 * 5) / 6;
 steps.forEach((t, i) => {
  const x = M + i * (w + 0.2);
  s.addShape(pres.shapes.CHEVRON, {x, y: 1.6, w, h: 0.9, fill: {color: i % 2 ? C.teal : C.navy}, line: {color: C.white}});
  s.addText(t, {x: x + 0.35, y: 1.6, w: w - 0.6, h: 0.9, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 13, bold: true, color: C.white, margin: 0, isTextBox: true});
 });
 card(s, M, 2.9, 3.9, 2.3, 'Four revision tests', 'Guided, independent, deeper understanding and long 6–12 mark answers with level marking.', C.tint, C.navy, 14);
 card(s, M + 4.1, 2.9, 3.9, 2.3, 'Five past papers', 'Real Pearson papers with tutor modes: start, check and plan. The official mark schemes are linked.', C.mint, C.teal, 14);
 card(s, M + 8.2, 2.9, 3.93, 2.3, 'Exam questions by topic', 'The A–F question banks and answers on Teams pair with each Learn section.', C.sand, C.navy, 14);
 notes(s, ['Set one revision test and one past-paper question per week in the final half term.']);
}

// Closing
{
 const s = pres.addSlide(); s.background = {color: C.navy};
 s.addText('Ready to deliver', {x: M, y: 1.2, w: 7, h: 1.0, fontFace: HEAD, fontSize: 42, bold: true, color: C.white, margin: 0, isTextBox: true});
 bullets(s, ['Share the start page link in Teams', 'Lesson 1: tour the pack and the tutor', 'Use a diagram task in every hardware lesson', 'Set workbook activities as homework', 'Revision tests and past papers every week'], M, 2.4, 6.6, 3.5, 18, C.white);
 const ch = fitH('the_six_logic_gates_with_their_symbols_n', 5.03);
 s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 7.4, y: 2.0, w: 5.33, h: ch + 0.3, fill: {color: C.white}, line: {color: C.white}, rectRadius: 0.15});
 img(s, 'the_six_logic_gates_with_their_symbols_n', 7.55, 2.15, 5.03, 3.2);
 notes(s, ['Site: ' + SITE, 'The AI tutor is live on the college Azure subscription.']);
}

pres.writeFile({fileName: path.join(process.env.OUT || __dirname, 'Unit2-Fundamentals-Teacher-Deck.pptx')}).then(f => console.log('wrote', f));
