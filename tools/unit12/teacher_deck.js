// Unit 12 Software Development: teacher delivery deck (original content).
// Figures are PNG exports of the Learn page diagrams: set FIGS to their folder (with dims.json).
const pptxgen = require('pptxgenjs');
const path = require('path');
const FIGS = process.env.FIGS || path.join(__dirname, 'figs');
const DIMS = require(path.join(FIGS, 'dims.json'));
const FIG = n => path.join(FIGS, n + '.png');

const C = {navy: '2B1B4A', teal: '6A3FA0', amber: 'F2A541', ink: '17334B', muted: '4F6577', tint: 'EAF2F9', mint: 'E6F4EE', white: 'FFFFFF', line: 'C9D7E3', sand: 'FDF1E7'};
const HEAD = 'Cambria', BODY = 'Calibri';
const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE'; // 13.333 x 7.5
pres.author = 'Unit 12 course team';
pres.title = 'Unit 12 Software Development: teacher delivery deck';
const W = 13.333, H = 7.5, M = 0.6;
const SITE = 'nigeriastudentcenter.github.io/btech/unit12/start.html';

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
 s.addText('Unit 12', {x: M, y: 1.2, w: 6, h: 0.6, fontFace: BODY, fontSize: 20, bold: true, color: C.amber, margin: 0, isTextBox: true});
 s.addText('Software Development', {x: M, y: 1.75, w: 6.4, h: 1.5, fontFace: HEAD, fontSize: 46, bold: true, color: C.white, margin: 0, isTextBox: true, valign: 'top'});
 s.addText('Teacher delivery deck · BTEC First in Information and Creative Technology', {x: M, y: 3.4, w: 6.2, h: 0.8, fontFace: BODY, fontSize: 18, color: 'D9CCF2', margin: 0, isTextBox: true, valign: 'top'});
 s.addText('Understand it · Design it · Build it · Test it · Review it', {x: M, y: 4.4, w: 6.2, h: 0.5, fontFace: BODY, fontSize: 16, italic: true, color: C.white, margin: 0, isTextBox: true});
 const th = fitH('the_software_development_life_cycle', 5.6);
 s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 6.9, y: 3.4 - th / 2, w: 5.9, h: th + 0.3, fill: {color: C.white}, line: {color: C.white}, rectRadius: 0.15});
 img(s, 'the_software_development_life_cycle', 7.05, 3.55 - th / 2, 5.6, 4.6);
 notes(s, ['Purpose: this deck supports delivery of Unit 12 alongside the student course site (' + SITE + ').', 'Lesson slides follow the college routine: starter, aim, teach, practical, task, check, flipped homework.', 'The scheme of work has 20 three-hour lessons and three assignments; the speaker notes link each slide to the workbook section, practical and quiz.']);
}

// 2 How each lesson runs
{
 const s = pres.addSlide(); title(s, 'How each lesson runs');
 const steps = [['Starter', 'predict-the-output or recap quiz'], ['Aim', 'share the aim and the criteria it builds'], ['Teach', 'live-code or diagram-led explanation'], ['Practical', 'build it in Visual Studio'], ['Task', 'workbook activity on the site'], ['Check', 'quiz or exit question'], ['Homework', 'flipped: preview the next lesson']];
 const w = (W - 2 * M - 0.15 * 6) / 7;
 steps.forEach(([h, b], i) => {
  const x = M + i * (w + 0.15);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y: 1.7, w, h: 2.2, fill: {color: i % 2 ? C.tint : C.sand}, line: {color: C.line}, rectRadius: 0.1});
  s.addShape(pres.shapes.OVAL, {x: x + w / 2 - 0.35, y: 1.9, w: 0.7, h: 0.7, fill: {color: C.navy}, line: {color: C.navy}});
  s.addText(String(i + 1), {x: x + w / 2 - 0.35, y: 1.9, w: 0.7, h: 0.7, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 18, bold: true, color: C.white, margin: 0, isTextBox: true});
  s.addText([{text: h, options: {bold: true, fontSize: 15, color: C.navy, breakLine: true}}, {text: b, options: {fontSize: 12, color: C.ink}}], {x: x + 0.1, y: 2.75, w: w - 0.2, h: 1.35, align: 'center', valign: 'top', fontFace: BODY, margin: 0, isTextBox: true});
 });
 card(s, M, 4.3, 6.0, 1.5, 'Live coding works best', 'Type the example in front of the class, make a deliberate mistake, and let students spot it. Then they build their own version in the practical.');
 card(s, 6.9, 4.3, 5.83, 1.5, 'Three-hour lessons', 'Roughly: 20 min teach, 90 min practical, 40 min workbook and quiz, with breaks. Practicals are on the site so students can catch up.', C.sand);
 notes(s, ['Students who miss a lesson can follow the Learn page and practical at home; console versions run at dotnetfiddle.net.']);
}

// 3 At a glance
{
 const s = pres.addSlide(); title(s, 'Unit 12 at a glance');
 const stats = [['60', 'guided learning hours'], ['3', 'assignments'], ['4', 'learning aims: A–D'], ['18', 'lessons on the site'], ['10', 'programming practicals']];
 const w = (W - 2 * M - 0.25 * 4) / 5;
 stats.forEach(([n, l], i) => {
  const x = M + i * (w + 0.25);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y: 1.6, w, h: 2.1, fill: {color: i === 0 ? C.navy : C.tint}, line: {color: i === 0 ? C.navy : C.tint}, rectRadius: 0.12});
  s.addText(n, {x, y: 1.75, w, h: 1.1, align: 'center', fontFace: HEAD, fontSize: 60, bold: true, color: i === 0 ? C.white : C.teal, margin: 0, isTextBox: true});
  s.addText(l, {x: x + 0.15, y: 2.85, w: w - 0.3, h: 0.7, align: 'center', fontFace: BODY, fontSize: 14, color: i === 0 ? C.white : C.ink, margin: 0, isTextBox: true});
 });
 const aims = [['A', 'Understand the characteristics and uses of a software program'], ['B', 'Design a software program'], ['C', 'Develop and test a software program'], ['D', 'Review the finished software program']];
 const w2 = (W - 2 * M - 0.25 * 3) / 4;
 aims.forEach(([a, t], i) => card(s, M + i * (w2 + 0.25), 4.1, w2, 1.9, `Learning aim ${a}`, t, [C.tint, C.sand, C.mint, C.tint][i], C.navy, 13));
 footer(s, 'Level 1 and Level 2 · internally assessed · mandatory in the Computer Science pathway · links to Unit 2 Technology Systems and Unit 8 Mobile Apps Development.');
 notes(s, ['Unit 12 builds on Unit 2 (software types) and complements Unit 8 (mobile apps).', 'Maths opportunities are flagged on 1C.4, 2C.P4, 2C.M3, 2C.D3 (calculations in programs).']);
}

// 4 Assessment map
{
 const s = pres.addSlide(); title(s, 'Assessment map');
 table(s, ['Assignment', 'Level 1 / Pass', 'Merit', 'Distinction'], [
  ['1 · Characteristics of programs (aim A)', '1A.1 / 2A.P1 Identify / explain the purpose and characteristics of two programs', '2A.M1 Comment on quality, suggest improvements, flowchart', '2A.D1 Discuss strengths and weaknesses'],
  ['2 · Design, develop, test (aims B, C)', '1B.2 / 2B.P2 Purpose and user requirements\n1B.3 / 2B.P3 Design: problem definition, solution, predefined functions, test plan\n1C.4 / 2C.P4 Develop: UI, constructs, commentary\n1C.5 / 2C.P5 Test and repair', '2B.M2 Detailed design with alternatives and test data\n2C.M3 Functional program meets the brief\n2C.M4 Feedback used to improve', '2B.D2 Justify design decisions\n2C.D3 Refine for code quality and user feedback'],
  ['3 · Review (aim D)', '1D.6 / 2D.P6 How the program suits requirements and purpose', '2D.M5 Review the extent requirements are met, with feedback and constraints', '2D.D4 Evaluate against designs and code quality; justify changes; recommend']], {x: M, y: 1.45, w: W - 2 * M, colW: [2.4, 4.5, 2.8, 2.43], fontSize: 11});
 footer(s, 'The Assignment guide on the site restates every criterion in plain English with a success checklist; the same data drives the builder and the AI coach.');
 notes(s, ['The scheme of work schedules Assignment 1 in lesson 5, Assignment 2 in lessons 17–18 and Assignment 3 in lesson 20. Use centre-devised briefs or Pearson’s authorised assignment briefs.', 'Choose an Assignment 2 client different from the leisure-centre example used in the lessons.']);
}

// 5 Student site
{
 const s = pres.addSlide(); title(s, 'The student course site');
 const pages = [['1. Assignment guide', 'Three assignments in plain English; Level 1 to Distinction explained; checklists'], ['2. Learn', '18 lessons with original diagrams, flowcharts and Visual Basic examples'], ['3. Workbook + tutor', 'Activity and quick check per lesson; AI study tutor; saves on device'], ['4. Practicals', '10 labs: forms, calculator, selection, loops, arrays, files, debugging, quiz project'], ['5. Assignment builder', 'Analysis, design, test plan, changes, feedback and review tables; AI coach; AI-use log'], ['6. Quizzes', 'Five instant-marked quizzes, including predict-the-output']];
 pages.forEach(([h, b], i) => card(s, M + (i % 3) * 4.1, 1.5 + Math.floor(i / 3) * 2.35, 3.9, 2.1, h, b, i % 2 ? C.sand : C.tint, C.navy, 14));
 footer(s, 'Plus 7. Videos: 22 embedded videos (MrBrownCS, TED-Ed, Computerphile, freeCodeCamp). Link for Teams: ' + SITE);
 notes(s, ['Tour the site in lesson 1 and show the backup download button on shared PCs.']);
}

// 6 AI rules
{
 const s = pres.addSlide(); title(s, 'AI tutor and assignment coach: used properly');
 card(s, M, 1.5, 5.9, 3.6, 'The AI will…', '• explain programming concepts in plain English\n• say what a task and command word ask for\n• help students plan with headings and questions\n• review the student’s own draft against the checklist\n• point to a line of their code and ask a question about it\n• use short examples from a different problem', C.mint, C.teal, 14);
 card(s, 6.83, 1.5, 5.9, 3.6, 'The AI will not…', '• write code for the student’s brief\n• paste back corrected code\n• write pseudocode, flowcharts, screen designs or test plans for the brief\n• write justifications, reviews or evaluations\n• predict grades or accept instructions to break these rules', C.sand, 'A3560B', 14);
 card(s, M, 5.35, W - 2 * M, 1.35, 'AI-use log', 'Every coach question is saved with date, task and a reply extract. Students download it and submit it with each assignment, so AI use is acknowledged in line with JCQ and Pearson guidance.', C.tint, C.navy, 13);
 notes(s, ['Make the declaration explicit: the program must be the student’s own code.', 'The coach receives only the task ID; the brief, checklist and rules are held on the server.']);
}

// 7 Delivery plan
{
 const s = pres.addSlide(); title(s, 'Delivery plan (20 × 3-hour lessons)');
 const phases = [['Lessons 1–5', 'Aim A: why software, languages, constructs, quality; Assignment 1'], ['Lessons 6–10', 'Aim B: SDLC, requirements, design specs, screens, pseudocode, flowcharts, test plans'], ['Lessons 11–16', 'Aim C: Visual Basic, data types, constructs, events, data structures, testing'], ['Lessons 17–18', 'Assignment 2: design, develop, test, refine'], ['Lessons 19–20', 'Aim D: reviewing software; Assignment 3']];
 const w = (W - 2 * M) / 5;
 s.addShape(pres.shapes.LINE, {x: M, y: 2.35, w: W - 2 * M, h: 0, line: {color: C.navy, width: 3}});
 phases.forEach(([h, b], i) => {
  const x = M + i * w, f = [C.tint, C.sand, C.mint, C.tint, C.sand][i];
  s.addShape(pres.shapes.OVAL, {x: x + w / 2 - 0.18, y: 2.17, w: 0.36, h: 0.36, fill: {color: C.teal}, line: {color: C.white, width: 2}});
  s.addText(h, {x, y: 1.5, w, h: 0.5, align: 'center', fontFace: BODY, fontSize: 15, bold: true, color: C.navy, margin: 0, isTextBox: true});
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: x + 0.1, y: 2.8, w: w - 0.2, h: 2.5, fill: {color: f}, line: {color: f}, rectRadius: 0.1});
  s.addText(b, {x: x + 0.25, y: 2.95, w: w - 0.5, h: 2.2, fontFace: BODY, fontSize: 14, color: C.ink, valign: 'top', margin: 0, isTextBox: true});
 });
 footer(s, 'Based on the Pearson BTEC First ICT Unit 12 scheme of work. Practical 10 (quiz project) is a full rehearsal before Assignment 2.');
 notes(s, ['Learners should spend lesson time and non-supervised time on assignments (scheme of work).']);
}

divider('Learning aim A', 'Understand the characteristics and uses of a software program · Assignment 1');

lessonSplit('A1–A2', 'Why software? Languages and compiling', 'input_process_output', 'explain uses of software, types of language and why programs are compiled',
 ['Inputs, processing, outputs, storage', 'Uses: games, productivity, information, repetitive/dangerous tasks, complex problems', 'Low-level vs high-level', 'Procedural vs event-driven', 'Compiler: check, optimise, translate'],
 [['Starter', 'Write instructions to make a cup of tea; swap and follow them literally.'], ['Practical', 'Practical 1: your first Windows Forms program.'], ['Check', 'Quiz 1.']],
 ['Demonstrate a centre-devised Hello World program, then a game, a web app and a desktop app, asking which language each might use.', 'Question: why can the CPU not run Visual Basic directly?', 'Videos (A1, A2): TED-Ed What’s an algorithm?; MrBrownCS high/low-level languages and translators.'], 'from_source_code_to_a_program_that_runs');

lessonSplit('A3–A4', 'Constructs, techniques and quality', 'six_measures_of_software_quality', 'identify constructs and techniques in a program and comment on its quality',
 ['Command words, subroutines, strings, files, data structures, events', 'Annotate someone else’s code', 'Six quality measures', 'Evidence from the code, then a specific improvement'],
 [['Starter', 'Spot five problems in a badly written program.'], ['Task', 'Workbook A3 and A4.'], ['Link', 'Assignment 1: 2A.P1, 2A.M1, 2A.D1.']],
 ['Model a quality comment: measure → evidence → improvement.', 'Support: the six-box quality diagram. Stretch: discuss trade-offs (efficiency vs readability).', 'Video (A4): MrBrownCS Testing and defensive programming.']);

{
 const s = pres.addSlide(); chip(s, 'ASG 1'); title(s, 'Assignment 1: Characteristics of software programs', {y: 0.55, size: 28});
 s.addText('Scenario: work experience at a software company; explain and assess two simple programs supplied by the teacher.', {x: M, y: 1.3, w: W - 2 * M, h: 0.45, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 const tasks = [['1A.1 / 2A.P1 · Pass', 'Identify / explain the purpose and characteristics of two programs, including tools and techniques used.'], ['2A.M1 · Merit', 'Comment on the quality of one program, suggest improvements, and draw a flowchart of the improved processing.'], ['2A.D1 · Distinction', 'Discuss the strengths and weaknesses of the program and reach a conclusion.']];
 tasks.forEach(([h, b], i) => card(s, M + i * 4.1, 1.95, 3.9, 2.6, h, b, [C.tint, C.mint, C.sand][i], C.navy, 14));
 card(s, M, 4.8, W - 2 * M, 1.4, 'Tools for students', 'Assignment builder: program analysis table, quality review table · AI coach (explain, plan, review, accuracy) · AI-use log · tip: run the programs, or dry-run them with a trace table', C.white, C.teal, 13);
 notes(s, ['Supply two short, different programs (e.g. one with selection, one with a loop). Do not use the examples from the Learn page.', 'Collect the AI-use log with submissions.']);
}

divider('Learning aim B', 'Design a software program');

lessonSplit('B1–B2', 'Life cycle, requirements and design specification', 'the_software_development_life_cycle', 'describe the SDLC and turn a brief into requirements and a design specification',
 ['Assess requirements → design → develop → test → maintain', 'Waterfall, iterative/agile, RAD', 'Purpose vs user requirements', 'Problem definition statement', 'Scope, inputs, outputs, processing, UI, constraints'],
 [['Starter', 'Getting ready for college: what are your stages?'], ['Task', 'Workbook B1 and B2: café ordering brief.'], ['Check', 'Quiz 2a.']],
 ['Use a short sample brief and have pairs extract requirements.', 'Video (B1): AltexSoft, Software development life cycle explained.']);

lessonSplit('B3', 'Screens, navigation and alternatives', 'annotated_screen_layout_and_navigation_d', 'design screen layouts and navigation and compare alternative solutions',
 ['Main tasks as input, processing, output', 'Annotate every control', 'Navigation diagrams', 'Two alternatives, compared', 'Justify against requirements and constraints'],
 [['Starter', 'Rate three real app screens for usability.'], ['Practical', 'Quiz screen design (scheme of work lesson 7).'], ['Link', '2B.M2 alternatives; 2B.D2 justification.']],
 ['Students design the quiz screen: question, four answers A–D, Submit, Quit, feedback area.', 'Stretch: prototype it in Visual Studio without code.']);

lessonSplit('B4', 'Algorithms: pseudocode, flowcharts, trace tables', 'flowchart_cinema_ticket_price', 'write algorithms as pseudocode and flowcharts and dry-run them',
 ['Five flowchart symbols', 'Pseudocode: structured English', 'Every decision has Yes and No exits', 'Trace tables to dry-run', 'Design before code'],
 [['Starter', 'Robot making tea: pseudocode in pairs.'], ['Practical', 'Practical 3: temperature converter from design to code.'], ['Check', 'Quiz 2b.']],
 ['Scheme of work lesson 10 tasks: multiply two numbers; °C to °F using F = C × 9 / 5 + 32.', 'Videos (B4): MrBrownCS Flowcharts; trace tables tutorial; pseudocode (stretch).'], 'flowchart_symbols');

lessonSplit('B5', 'Data, validation, predefined code and test plans', 'variables_are_labelled_boxes_in_memory', 'plan data, validation, error handling, predefined code and a test plan',
 ['Data structures and storage', 'Presence, type, range, length, lookup checks', 'Error handling and reporting', 'List predefined code and its source', 'Test plan: normal, boundary, erroneous'],
 [['Starter', 'Break this form: what could a user type?'], ['Task', 'Workbook B5: marks program test plan.'], ['Link', '2B.P3 design and test plan.']],
 ['Model a test plan with boundary data around 1–10.', 'Video (B5): MrBrownCS Data assurance considerations.']);

divider('Learning aim C', 'Develop and test a software program in Visual Basic');

lessonSplit('C1', 'The IDE, forms and events', 'the_parts_of_the_visual_studio_ide', 'use Visual Studio to build a form and write event handlers',
 ['Toolbox, designer, Properties, Solution Explorer', 'Name controls with prefixes', 'Double-click → event handler', 'Input from TextBox.Text; output to Label.Text', 'F5 to run; Build for an .exe'],
 [['Practical', 'Practical 1 and 2: first form; calculator.'], ['Task', 'Workbook C1.'], ['Check', 'Quiz 3a.']],
 ['Scheme of work lessons 11 and 15. Show properties changing live.', 'Videos (C1): MrBrownCS IDEs; freeCodeCamp VB.NET full course for reference.']);

lessonSplit('C2–C3', 'Variables, operators and selection', 'variables_are_labelled_boxes_in_memory', 'use data types, constants, operators and If/ElseIf/Select Case',
 ['Integer, Decimal, String, Char, Boolean, Date', 'Constants; local vs global', '+ − * / \\ Mod; comparison; And/Or/Not', 'If … ElseIf … Else; Select Case', 'Order of conditions matters'],
 [['Starter', 'Predict: 17 Mod 5 and 17 \\ 5.'], ['Practical', 'Practical 4: login and grade calculator.'], ['Check', 'Quiz 3b.']],
 ['Scheme of work lessons 12–14.', 'Videos (C2, C3): MrBrownCS Data types, variables and constants; 3 basic constructs; VB.NET If statements.']);

lessonSplit('C4–C5', 'Loops and subroutines', 'counter_controlled_and_condition_control', 'use For, Do While, Do … Loop Until, procedures and functions',
 ['For … Next for a known number of times', 'Do While / Loop Until for conditions', 'Recursion needs a base case', 'Sub vs Function; parameters; Return', 'Reuse and maintainability'],
 [['Starter', 'Trace a For loop on the board.'], ['Practical', 'Practical 5: loops and guessing game.'], ['Check', 'Quiz 3b.']],
 ['Refactor the calculator into functions to show the benefit.', 'Videos (C4, C5): Computerphile recursion (stretch); MrBrownCS subprograms and functions.']);

lessonSplit('C6–C7', 'Arrays, strings, files and robustness', 'an_array_and_a_record', 'use arrays, records, string handling and files, with validation and error handling',
 ['Arrays start at index 0', 'Structure for records', 'Length, Substring, ToUpper, IndexOf, Split', 'StreamWriter / StreamReader: open, read, write, close', 'TryParse, Try … Catch, comments, Build'],
 [['Practical', 'Practicals 6, 7 and 8.'], ['Task', 'Workbook C6 and C7.'], ['Check', 'Quiz 4.']],
 ['Scheme of work lesson 16.', 'Videos (C6, C7): MrBrownCS arrays, string handling, text files.'], 'writing_to_and_reading_from_a_text_file');

lessonSplit('C8', 'Testing, debugging and refining', 'three_kinds_of_error', 'test against a plan, debug, gather feedback and refine',
 ['Syntax, runtime and logic errors', 'Breakpoints (F9), stepping (F10/F11), Locals', 'Record expected vs actual, with screenshots', 'Feedback on usability and quality', 'Refine, re-test, update the design'],
 [['Practical', 'Practical 9: debugging challenge.'], ['Task', 'Workbook C8.'], ['Check', 'Quiz 4.']],
 ['Case study: cash machines paying out too much because of a software fault.', 'Videos (C8): MrBrownCS testing approaches; syntax and logic errors.']);

{
 const s = pres.addSlide(); chip(s, 'ASG 2'); title(s, 'Assignment 2: Design, develop and test', {y: 0.55, size: 28});
 s.addText('Scenario: a client brief describing a problem software could solve (e.g. replacing a paper booking or ordering system).', {x: M, y: 1.3, w: W - 2 * M, h: 0.45, fontFace: BODY, fontSize: 15, italic: true, color: C.muted, margin: 0, isTextBox: true});
 const ev = [['1B.2 / 2B.P2', 'purpose and user requirements'], ['1B.3 / 2B.P3', 'design and test plan'], ['2B.M2 · 2B.D2', 'alternatives; justified decisions'], ['1C.4 / 2C.P4', 'develop: UI, constructs, comments'], ['2C.M3', 'functional program meets brief'], ['1C.5 / 2C.P5', 'test and repair'], ['2C.M4 · 2C.D3', 'feedback; refine for quality']];
 ev.forEach(([c, t], i) => {
  const y = 1.95 + i * 0.62;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: M, y, w: 2.3, h: 0.5, fill: {color: i > 4 ? C.amber : C.teal}, line: {color: C.white}, rectRadius: 0.08});
  s.addText(c, {x: M, y, w: 2.3, h: 0.5, align: 'center', valign: 'middle', fontFace: BODY, fontSize: 13, bold: true, color: C.white, margin: 0, isTextBox: true});
  s.addText(t, {x: M + 2.45, y, w: 4.0, h: 0.5, valign: 'middle', fontFace: BODY, fontSize: 15, color: C.ink, margin: 0, isTextBox: true});
 });
 card(s, 7.3, 1.95, 5.43, 4.2, 'In the Assignment builder', '• requirements table\n• IPO tasks, alternatives, data and validation, predefined code sources\n• test plan with normal / boundary / erroneous types\n• development and changes log\n• feedback log\n• AI coach that will not write their code\n• AI-use log to hand in', C.tint, C.navy, 14);
 notes(s, ['Lessons 17–18 plus non-supervised time. Check source code includes commentary throughout (2C.P4).', 'For 2C.D3, look for refinements to code quality, not just new features.']);
}

divider('Learning aim D', 'Review the finished software program · Assignment 3');

lessonSplit('D1', 'Reviewing the finished program', 'six_measures_of_software_quality', 'review a program against requirements, purpose, user experience, constraints and quality',
 ['Requirements: fully, partly, not met', 'Fitness for purpose', 'User experience from feedback', 'Constraints and workarounds', 'Strengths, improvements, recommendations'],
 [['Practical', 'Review the Practical 10 quiz program.'], ['Task', 'Workbook D1: evaluation grid.'], ['Check', 'Quiz 5.']],
 ['Learners review software they wrote in the course, not their assignment work (scheme of work lesson 19).', 'Distinction: compare with the initial design and justify every change.']);

{
 const s = pres.addSlide(); chip(s, 'ASG 3'); title(s, 'Assignment 3: Review the finished program', {y: 0.55, size: 28});
 const tasks = [['1D.6 / 2D.P6 · Pass', 'Identify / explain how the final program is suitable for the original requirements and purpose.'], ['2D.M5 · Merit', 'Review the extent to which it meets the requirements, considering feedback from others and constraints.'], ['2D.D4 · Distinction', 'Evaluate against the initial designs and code quality, justify changes, recommend further improvements.']];
 tasks.forEach(([h, b], i) => card(s, M + i * 4.1, 1.6, 3.9, 2.8, h, b, [C.tint, C.mint, C.sand][i], C.navy, 14));
 card(s, M, 4.7, W - 2 * M, 1.5, 'Evidence to use', 'Test plan results and screenshots · feedback log · development and changes log · the review grid in the Assignment builder · the original design documents', C.white, C.teal, 14);
 notes(s, ['Lesson 20. Format can be a report or a presentation to the client.']);
}

// Practicals overview
{
 const s = pres.addSlide(); title(s, 'Ten practicals on the student site');
 const labs = ['First Windows Forms program', 'Two-number calculator', 'Temperature converter', 'Login and grades', 'Loops and guessing game', 'Arrays and strings', 'Save and load a file', 'Validation and errors', 'Debugging challenge', 'Quiz program project'];
 labs.forEach((t, i) => {
  const col = i % 5, row = Math.floor(i / 5), w = (W - 2 * M - 0.25 * 4) / 5, x = M + col * (w + 0.25), y = 1.6 + row * 2.45;
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x, y, w, h: 2.2, fill: {color: row ? C.sand : C.tint}, line: {color: row ? C.sand : C.tint}, rectRadius: 0.12});
  s.addText(String(i + 1), {x: x + 0.2, y: y + 0.15, w: 1, h: 0.8, fontFace: HEAD, fontSize: 36, bold: true, color: C.teal, margin: 0, isTextBox: true});
  s.addText(t, {x: x + 0.2, y: y + 1.0, w: w - 0.4, h: 1.05, fontFace: BODY, fontSize: 15, bold: true, color: C.ink, margin: 0, isTextBox: true, valign: 'top'});
 });
 footer(s, 'Visual Studio Community (Windows Forms, Visual Basic). Console versions run at dotnetfiddle.net. Practical 9 needs a teacher-prepared program with three faults.');
 notes(s, ['Map: 1 C1 · 2 C2 · 3 B4 · 4 C3 · 5 C4 · 6 C6 · 7–8 C7 · 9 C8 · 10 B3–D1.']);
}

// Closing
{
 const s = pres.addSlide(); s.background = {color: C.navy};
 s.addText('Ready to deliver', {x: M, y: 1.2, w: 7, h: 1.0, fontFace: HEAD, fontSize: 42, bold: true, color: C.white, margin: 0, isTextBox: true});
 bullets(s, ['Share the start page link in Teams', 'Lesson 1: tour the site and the Assignment guide', 'Install Visual Studio Community on lab PCs', 'Agree AI rules; collect AI-use logs', 'Use the quizzes as starters and exit checks'], M, 2.4, 6.6, 3.5, 18, C.white);
 const ch = fitH('three_kinds_of_error', 5.03);
 s.addShape(pres.shapes.ROUNDED_RECTANGLE, {x: 7.4, y: 2.4, w: 5.33, h: ch + 0.3, fill: {color: C.white}, line: {color: C.white}, rectRadius: 0.15});
 img(s, 'three_kinds_of_error', 7.55, 2.55, 5.03, 2.45);
 notes(s, ['Site: ' + SITE, 'The AI tutor and coach depend on the college Azure subscription being active; the rest of the site works without it.']);
}

pres.writeFile({fileName: path.join(process.env.OUT || __dirname, 'Unit12-Software-Development-Teacher-Deck.pptx')}).then(f => console.log('wrote', f));
