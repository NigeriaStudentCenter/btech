'use strict';
// Unit 12 Software Development quizzes (original questions). Uses the shared engine in ../revision.js.
window.REVISION_KEY = 'unit12-quiz-v1';
window.REVISION_FILE = 'my-software-development-quiz-answers.json';
const ch = (id, section, prompt, options, answer, feedback, context) => ({id, marks: 1, type: 'choice', section, prompt, options, answer, feedback, context});
const QM = ['Efficiency', 'Maintainability', 'Portability', 'Reliability', 'Robustness', 'Usability'];
window.REVISION_TESTS = [
{
 id: 'q1', title: 'Quiz 1: Software, languages and quality', short: '1 Software', guided: true,
 intro: 'Learning aim A: why software is used, programming languages, constructs and quality.',
 questions: [
  {id: 'q1a', title: 'Software and languages', scenario: 'Choose the best answer.', parts: [
   ch('a', 'A1', 'A robot arm welds car doors all day without tiring. Which use of software is this?', ['Gaming and entertainment', 'Completing repetitive tasks', 'Information storage', 'Solving complex problems'], 'Completing repetitive tasks', 'Robots repeat the same task accurately and safely.'),
   ch('b', 'A1', 'Which is system software?', ['A spreadsheet', 'An operating system', 'A computer game', 'A web browser'], 'An operating system', 'System software runs the computer itself.'),
   ch('c', 'A2', 'Which is the only language a CPU can run directly?', ['Visual Basic', 'Pseudocode', 'Machine code', 'Python'], 'Machine code', 'Everything else must be translated into machine code.'),
   ch('d', 'A2', 'Visual Basic runs code when the user clicks a button. This makes it…', ['Procedural', 'Event-driven', 'Low-level', 'Machine code'], 'Event-driven', 'Code runs in response to events.'),
   ch('e', 'A2', 'What does a compiler do?', ['Runs one line at a time', 'Translates the whole program into machine code before it runs', 'Draws the user interface', 'Stores data in a file'], 'Translates the whole program into machine code before it runs', 'It also reports syntax errors and produces an executable.')]},
  {id: 'q1b', title: 'Quality', scenario: 'Which quality measure is described?', parts: [
   {id: 'a', marks: 6, type: 'fields', section: 'A4', prompt: 'Choose the measure.', grid: 2, fields: [
    {id: 'crash', label: 'Typing a letter in a number box does not crash it', options: QM, accept: ['Robustness']},
    {id: 'comments', label: 'Comments and clear names make it easy to change', options: QM, accept: ['Maintainability']},
    {id: 'mac', label: 'It runs on Windows and macOS', options: QM, accept: ['Portability']},
    {id: 'correct', label: 'The totals it calculates are always right', options: QM, accept: ['Reliability']},
    {id: 'fast', label: 'It uses little memory and processor time', options: QM, accept: ['Efficiency']},
    {id: 'easy', label: 'New staff can use it without training', options: QM, accept: ['Usability']}]}]}]
},
{
 id: 'q2', title: 'Quiz 2: Designing a program', short: '2 Design', guided: true,
 intro: 'Learning aim B: the life cycle, design specifications, flowcharts and test data.',
 questions: [
  {id: 'q2a', title: 'Life cycle and design', scenario: 'Put the stages in order, then answer.', parts: [
   {id: 'a', marks: 5, type: 'order', section: 'B1', prompt: 'Put the stages of the software development life cycle in order.', steps: [{id: 'r', text: 'Assess requirements'}, {id: 'd', text: 'Design specification'}, {id: 'c', text: 'Develop code'}, {id: 't', text: 'Test'}, {id: 'm', text: 'Maintain'}], base: ['r', 'd', 'c', 't', 'm']},
   ch('b', 'B2', 'The program must be written in Visual Basic and finished in four weeks. These are…', ['Inputs', 'Outputs', 'Constraints', 'User requirements'], 'Constraints', 'Constraints limit how the program can be designed and developed.'),
   ch('c', 'B2', 'Which describes the current problem and how software will solve it?', ['Problem definition statement', 'Test plan', 'Navigation diagram', 'Trace table'], 'Problem definition statement', 'It shows you understand the client’s problem.'),
   ch('d', 'B3', 'Which diagram shows how the screens of a program link together?', ['Flowchart', 'Navigation diagram', 'Trace table', 'IPO table'], 'Navigation diagram', 'A flowchart shows an algorithm; a navigation diagram shows screens.')]},
  {id: 'q2b', title: 'Flowcharts and test data', scenario: 'Choose the best answer.', parts: [
   {id: 'a', marks: 4, type: 'fields', section: 'B4', prompt: 'Which flowchart symbol is used for each?', grid: 2, fields: [
    {id: 'dec', label: 'Is age over 18?', options: ['Oval', 'Parallelogram', 'Rectangle', 'Diamond'], accept: ['Diamond']},
    {id: 'in', label: 'Input the price', options: ['Oval', 'Parallelogram', 'Rectangle', 'Diamond'], accept: ['Parallelogram']},
    {id: 'proc', label: 'total = price × quantity', options: ['Oval', 'Parallelogram', 'Rectangle', 'Diamond'], accept: ['Rectangle']},
    {id: 'end', label: 'End', options: ['Oval', 'Parallelogram', 'Rectangle', 'Diamond'], accept: ['Oval']}]},
   {id: 'b', marks: 4, type: 'fields', section: 'B5', prompt: 'A program accepts whole numbers of tickets from 1 to 8. What type of test data is each?', grid: 2, fields: [
    {id: 'n', label: '4', options: ['Normal', 'Boundary', 'Erroneous'], accept: ['Normal']},
    {id: 'b1', label: '8', options: ['Normal', 'Boundary', 'Erroneous'], accept: ['Boundary']},
    {id: 'e1', label: '9', options: ['Normal', 'Boundary', 'Erroneous'], accept: ['Erroneous']},
    {id: 'e2', label: 'two', options: ['Normal', 'Boundary', 'Erroneous'], accept: ['Erroneous']}]},
   ch('c', 'B5', 'Which validation check makes sure a name box is not left empty?', ['Range check', 'Presence check', 'Length check', 'Type check'], 'Presence check', 'It checks something has been entered.')]}]
},
{
 id: 'q3', title: 'Quiz 3: Writing code', short: '3 Code', guided: true,
 intro: 'Learning aim C: data types, operators, selection, loops, subroutines, arrays and strings. Work each one out before you check.',
 questions: [
  {id: 'q3a', title: 'Data and operators', scenario: 'Type each answer.', parts: [
   {id: 'a', marks: 4, type: 'fields', section: 'C2', prompt: 'What is the result?', grid: 2, fields: [
    {id: 'mod', label: '20 Mod 6', accept: ['2']},
    {id: 'idiv', label: '20 \\ 6', accept: ['3']},
    {id: 'join', label: '"Code" & "Club"', accept: ['CodeClub', '"CodeClub"']},
    {id: 'len', label: '"Visual Basic".Length', accept: ['12']}]},
   {id: 'b', marks: 4, type: 'fields', section: 'C2', prompt: 'Choose the best data type.', grid: 2, fields: [
    {id: 'phone', label: 'A phone number like 07700 900123', options: ['Integer', 'Decimal', 'String', 'Boolean'], accept: ['String']},
    {id: 'price', label: 'A price like 12.99', options: ['Integer', 'Decimal', 'String', 'Boolean'], accept: ['Decimal']},
    {id: 'paid', label: 'Whether a bill has been paid', options: ['Integer', 'Decimal', 'String', 'Boolean'], accept: ['Boolean']},
    {id: 'seats', label: 'The number of seats on a bus', options: ['Integer', 'Decimal', 'String', 'Boolean'], accept: ['Integer']}]}]},
  {id: 'q3b', title: 'Predict the output', scenario: 'Trace each piece of code.', parts: [
   ch('a', 'C3', 'mark = 55. If mark >= 70 Then "D" ElseIf mark >= 55 Then "M" ElseIf mark >= 40 Then "P" Else "U". What is shown?', ['D', 'M', 'P', 'U'], 'M', 'The first true condition is mark >= 55.'),
   ch('b', 'C4', 'total = 0 : For i = 1 To 4 : total = total + i : Next. What is total?', ['4', '6', '10', '24'], '10', '1 + 2 + 3 + 4 = 10.'),
   ch('c', 'C4', 'How many times does For k = 0 To 10 Step 5 run?', ['2', '3', '5', '10'], '3', 'k = 0, 5, 10.'),
   ch('d', 'C6', 'names = {"Ali", "Bea", "Cal"}. What is names(1)?', ['Ali', 'Bea', 'Cal', 'Error'], 'Bea', 'VB arrays start at index 0.'),
   ch('e', 'C6', 'What does "Bedford".Substring(3, 4) give?', ['Bedf', 'ford', 'dfor', 'Bed'], 'ford', 'Start at index 3 (the f), take 4 characters.'),
   ch('f', 'C5', 'Which kind of subroutine returns a value?', ['Procedure (Sub)', 'Function', 'Event', 'Constant'], 'Function', 'A function returns a value with Return.')]}]
},
{
 id: 'q4', title: 'Quiz 4: Testing and debugging', short: '4 Testing', guided: true,
 intro: 'Learning aim C: errors, debugging tools, files and robustness.',
 questions: [
  {id: 'q4a', title: 'Which kind of error?', scenario: 'Choose syntax, runtime or logic.', parts: [
   {id: 'a', marks: 4, type: 'fields', section: 'C8', prompt: 'Error type', grid: 2, fields: [
    {id: 's', label: 'Dim total As Integr (misspelt)', options: ['Syntax', 'Runtime', 'Logic'], accept: ['Syntax']},
    {id: 'r', label: 'CInt("hello") crashes the program', options: ['Syntax', 'Runtime', 'Logic'], accept: ['Runtime']},
    {id: 'l', label: 'An average is calculated by dividing by the wrong number', options: ['Syntax', 'Runtime', 'Logic'], accept: ['Logic']},
    {id: 'l2', label: 'If age > 18 should have been If age >= 18', options: ['Syntax', 'Runtime', 'Logic'], accept: ['Logic']}]},
   ch('b', 'C8', 'Which debugger tool pauses the program at a chosen line?', ['Build', 'Breakpoint', 'Toolbox', 'Properties window'], 'Breakpoint', 'Press F9 on a line, then step through with F10.'),
   ch('c', 'C7', 'What stops a program crashing when a file is missing?', ['A breakpoint', 'Error handling such as File.Exists or Try … Catch', 'A longer variable name', 'Compiling'], 'Error handling such as File.Exists or Try … Catch', 'Handle the problem and show a helpful message.'),
   ch('d', 'C7', 'Why does a program need file handling to keep bookings?', ['Variables are lost when the program closes', 'Files run faster than variables', 'Files make the program portable', 'It is required to compile'], 'Variables are lost when the program closes', 'Files store data permanently.'),
   ch('e', 'C8', 'Why should you re-test after fixing a fault?', ['To make the code longer', 'To prove the fix worked and nothing else broke', 'Because the compiler requires it', 'To change the requirements'], 'To prove the fix worked and nothing else broke', 'One change can affect other parts.')]}]
},
{
 id: 'q5', title: 'Quiz 5: Reviewing software', short: '5 Review', guided: true,
 intro: 'Learning aim D: reviewing and evaluating a finished program.',
 questions: [
  {id: 'q5a', title: 'Reviewing', scenario: 'Choose the best answer.', parts: [
   ch('a', 'D1', 'Which is the best evidence that a requirement has been met?', ['“I think it works”', 'A passed test with a screenshot', 'The length of the code', 'The colour of the form'], 'A passed test with a screenshot', 'Reviews need evidence.'),
   ch('b', 'D1', '“Users found the buttons easy to find and the messages clear.” Which review area is this?', ['Constraints', 'User experience', 'Portability', 'Scope'], 'User experience', 'It is about how it feels to use the program.'),
   ch('c', 'D1', 'A feature was not added because the college PCs could not print. This is an example of…', ['A constraint', 'A strength', 'Robustness', 'A data type'], 'A constraint', 'Device capabilities are a constraint; explain how you worked around it.'),
   ch('d', 'D1', 'What does a Distinction review (2D.D4) need that a Pass review does not?', ['A longer introduction', 'Comparison with the initial design, justified changes and recommendations', 'More screenshots of the code', 'A different program'], 'Comparison with the initial design, justified changes and recommendations', 'Evaluate against the design and code quality, then recommend improvements.')]}]
}
];
