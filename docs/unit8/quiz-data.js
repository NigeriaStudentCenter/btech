'use strict';
// Unit 8 Security knowledge quizzes (original questions). Uses the shared engine in ../revision.js.
window.REVISION_KEY = 'unit8-quiz-v1';
window.REVISION_FILE = 'my-security-quiz-answers.json';
const ch = (id, section, prompt, options, answer, feedback, context) => ({id, marks: 1, type: 'choice', section, prompt, options, answer, feedback, context});
const CAT = ['Human resources', 'Commercially sensitive', 'Access information'];
window.REVISION_TESTS = [
{
 id: 'q1', title: 'Quiz 1: Security risks', short: '1 Risks', guided: true,
 intro: 'Confidential information, why it matters, and what happens when it leaks.',
 questions: [
  {id: 'q1a', title: 'Types of confidential information', scenario: 'Choose the category for each item.', parts: [
   {id: 'a', marks: 6, type: 'fields', section: 'S1', prompt: 'Which category does each belong to?', grid: 2, fields: [
    {id: 'sal', label: 'Salaries and benefits', options: CAT, accept: ['Human resources']},
    {id: 'ip', label: 'Product designs (intellectual property)', options: CAT, accept: ['Commercially sensitive']},
    {id: 'pin', label: 'A door access PIN', options: CAT, accept: ['Access information']},
    {id: 'cl', label: 'Client contact details', options: CAT, accept: ['Commercially sensitive']},
    {id: 'bio', label: 'Staff fingerprint templates', options: CAT, accept: ['Access information']},
    {id: 'addr', label: 'Staff home addresses', options: CAT, accept: ['Human resources']}]},
   ch('b', 'S1', 'Why do organisations keep salaries confidential?', ['To avoid paying tax', 'So competitors cannot offer higher wages to poach staff, and staff do not demand comparable pay', 'Because salaries are intellectual property', 'To comply with the CIA triad'], 'So competitors cannot offer higher wages to poach staff, and staff do not demand comparable pay', 'Both reasons are named in the specification.'),
   ch('c', 'S1', 'A pharmacy leaks patient records and is found to have broken regulations. Which impact is specific to regulated professions?', ['Loss of licence to practise', 'Buffer overflow', 'Data corruption', 'A DDoS attack'], 'Loss of licence to practise', 'Non-compliance can stop a regulated business from operating at all.')]}]
},
{
 id: 'q2', title: 'Quiz 2: Technical threats', short: '2 Threats', guided: true,
 intro: 'Malware, botnets, hacking, social engineering and network attacks.',
 questions: [
  {id: 'q2a', title: 'Name the threat', scenario: 'Choose the best answer.', parts: [
   ch('a', 'T1', 'Files on a server are encrypted and a message demands payment in cryptocurrency.', ['Spyware', 'Ransomware', 'Worm', 'Keylogger'], 'Ransomware', 'Mitigate with offline or offsite backups so files can be restored.'),
   ch('b', 'T1', 'Malware spreads across a network by itself through an unpatched weakness.', ['Virus', 'Worm', 'Trojan', 'Phishing'], 'Worm', 'A virus needs a file to be run; a worm spreads on its own.'),
   ch('c', 'T1', 'Thousands of infected smart cameras flood a website with requests.', ['DoS from one PC', 'DDoS from a botnet', 'SQL injection', 'Pharming'], 'DDoS from a botnet', 'Many sources make it hard to block.'),
   ch('d', 'T2', "An attacker types ' OR '1'='1 into a login box and gets in.", ['Cross-site scripting', 'SQL injection', 'Buffer overflow', 'Brute force'], 'SQL injection', 'Prevent with parameterised queries and input validation.'),
   ch('e', 'T2', 'A comment posted on a forum contains a script that runs in every reader’s browser.', ['Cross-site scripting', 'SQL injection', 'Vishing', 'Watering hole'], 'Cross-site scripting', 'Prevent by encoding output and validating input.'),
   ch('f', 'T2', 'A program writes a long input past the end of its memory area and overwrites the next instruction address.', ['Buffer overflow', 'Brute force', 'Man-in-the-middle', 'Botnet'], 'Buffer overflow', 'Prevent with bounds checking and patches.')]},
  {id: 'q2b', title: 'Social engineering and network attacks', scenario: 'Match each attack.', parts: [
   {id: 'a', marks: 6, type: 'fields', section: 'T3', prompt: 'Which attack is it?', grid: 2, fields: [
    {id: 'sms', label: 'A text with a fake parcel-delivery link', options: ['Phishing', 'Spear phishing', 'Smishing', 'Vishing', 'Pharming', 'USB baiting'], accept: ['Smishing']},
    {id: 'call', label: 'A caller claiming to be the bank asks for your PIN', options: ['Phishing', 'Spear phishing', 'Smishing', 'Vishing', 'Pharming', 'USB baiting'], accept: ['Vishing']},
    {id: 'usb', label: 'Infected memory sticks left in the car park', options: ['Phishing', 'Spear phishing', 'Smishing', 'Vishing', 'Pharming', 'USB baiting'], accept: ['USB baiting']},
    {id: 'redir', label: 'Typing the correct bank address but landing on a fake site', options: ['Phishing', 'Spear phishing', 'Smishing', 'Vishing', 'Pharming', 'USB baiting'], accept: ['Pharming']},
    {id: 'target', label: 'An email to the finance manager using their name and a real project', options: ['Phishing', 'Spear phishing', 'Smishing', 'Vishing', 'Pharming', 'USB baiting'], accept: ['Spear phishing']},
    {id: 'mass', label: 'A mass email “your account will close” with a login link', options: ['Phishing', 'Spear phishing', 'Smishing', 'Vishing', 'Pharming', 'USB baiting'], accept: ['Phishing']}]},
   ch('b', 'T4', 'What is the best protection when using a hotel’s open Wi-Fi?', ['Turn up the screen brightness', 'Use a VPN and only HTTPS sites', 'Disable the firewall', 'Share files publicly'], 'Use a VPN and only HTTPS sites', 'Encryption stops anyone on the network reading your traffic.'),
   ch('c', 'T4', 'An API returns any customer’s record if you change the ID number in the request. What is missing?', ['Authorisation checks', 'A faster server', 'Compression', 'A bigger buffer'], 'Authorisation checks', 'The API must check the user is allowed to see that record.')]}]
},
{
 id: 'q3', title: 'Quiz 3: Vulnerabilities', short: '3 Vulnerabilities', guided: true,
 intro: 'Technical, human and physical vulnerabilities and their impact.',
 questions: [
  {id: 'q3a', title: 'Spot the weakness', scenario: 'Choose the best answer.', parts: [
   ch('a', 'V1', 'A bug is exploited by attackers before the vendor has released a fix. This is a…', ['Legacy system', 'Zero-day vulnerability', 'Firmware update', 'Air gap'], 'Zero-day vulnerability', 'There is no patch yet, so other controls must reduce the risk.'),
   ch('b', 'V1', 'Which is an inadequate security process?', ['Using MFA', 'Allowing short, reused passwords', 'Patching monthly', 'Hashing passwords'], 'Allowing short, reused passwords', 'An inadequate password policy is named in the specification.'),
   ch('c', 'V2', 'An employee is dismissed. What must happen immediately?', ['Send a thank-you email', 'Suspend their user accounts and remove them from the premises', 'Change the Wi-Fi name', 'Buy new PCs'], 'Suspend their user accounts and remove them from the premises', 'Otherwise a malicious employee could still copy or delete data.'),
   ch('d', 'V2', 'Which control reduces human error when deleting files?', ['Confirmation boxes', 'Tailgating', 'Air gaps', 'Port scanning'], 'Confirmation boxes', 'Also file properties such as read-only, and training.'),
   ch('e', 'V3', 'A visitor follows a member of staff through a swipe-card door.', ['Shoulder surfing', 'Tailgating', 'Vishing', 'Pharming'], 'Tailgating', 'Poor access control: train staff, use turnstiles, monitor doors.'),
   ch('f', 'V3', 'Laptops used on a building site keep breaking. Which control fits?', ['Rugged machines', 'Spear phishing training', 'Asymmetric encryption', 'A DMZ'], 'Rugged machines', 'Poor system robustness is fixed with tougher hardware.')]}]
},
{
 id: 'q4', title: 'Quiz 4: Threat mitigation', short: '4 Mitigation', guided: true,
 intro: 'Technical controls, encryption, access controls, backups, testing and firewalls.',
 questions: [
  {id: 'q4a', title: 'Choose the control', scenario: 'Choose the best answer.', parts: [
   ch('a', 'M2', 'Which method should a website use to store passwords?', ['Symmetric encryption', 'Salted hashing', 'Plain text', 'Compression'], 'Salted hashing', 'Hashes cannot be reversed; the salt defeats precomputed tables.'),
   ch('b', 'M2', 'In asymmetric encryption, which key do you use to send someone a secret message?', ['Your private key', 'Their public key', 'Their private key', 'A shared symmetric key only'], 'Their public key', 'Only their private key can decrypt it.'),
   ch('c', 'M3', 'Which is true multi-factor authentication?', ['Password and PIN', 'Password and code from a phone app', 'Two passwords', 'Username and password'], 'Password and code from a phone app', 'Something you know plus something you have.'),
   ch('d', 'M1', 'Which removes unnecessary services, ports and default accounts from a server?', ['Device hardening', 'Staff vetting', 'Differential backup', 'Smishing'], 'Device hardening', 'It reduces the attack surface.'),
   ch('e', 'M4', 'Which backup copies only the changes since the last FULL backup?', ['Full', 'Incremental', 'Differential', 'Mirror'], 'Differential', 'Restore needs the full backup plus the latest differential.'),
   ch('f', 'M4', 'What makes a penetration test ethical?', ['It uses special software', 'Written permission from the owner and an agreed scope', 'It is done at night', 'It finds no problems'], 'Written permission from the owner and an agreed scope', 'Without permission it is unauthorised access.')]},
  {id: 'q4b', title: 'Firewall rules', scenario: 'Which firewall rule type is each?', parts: [
   {id: 'a', marks: 4, type: 'fields', section: 'M5', prompt: 'Rule type', grid: 2, fields: [
    {id: 'ip', label: 'Block traffic from a known malicious address', options: ['Inbound/outbound rule', 'Traffic type rule', 'Application rule', 'IP address rule'], accept: ['IP address rule']},
    {id: 'app', label: 'Block a file-sharing program', options: ['Inbound/outbound rule', 'Traffic type rule', 'Application rule', 'IP address rule'], accept: ['Application rule']},
    {id: 'tel', label: 'Block Telnet (port 23), allow HTTPS (443)', options: ['Inbound/outbound rule', 'Traffic type rule', 'Application rule', 'IP address rule'], accept: ['Traffic type rule']},
    {id: 'in', label: 'Deny all unrequested connections coming in from the internet', options: ['Inbound/outbound rule', 'Traffic type rule', 'Application rule', 'IP address rule'], accept: ['Inbound/outbound rule']}]},
   ch('b', 'M5', 'Why put guest Wi-Fi on a separate VLAN?', ['It makes Wi-Fi faster', 'A compromised guest device cannot reach internal systems', 'It removes the need for passwords', 'It encrypts all traffic'], 'A compromised guest device cannot reach internal systems', 'Virtual segregation contains a breach.')]}]
},
{
 id: 'q5', title: 'Quiz 5: CIA triad and IAAA', short: '5 CIA & IAAA', guided: true,
 intro: 'How the parts of effective security fit together.',
 questions: [
  {id: 'q5a', title: 'CIA triad', scenario: 'Which element is MAINLY affected?', parts: [
   {id: 'a', marks: 4, type: 'fields', section: 'C1', prompt: 'Choose the element.', grid: 2, fields: [
    {id: 'leak', label: 'Customer records posted online', options: ['Confidentiality', 'Integrity', 'Availability'], accept: ['Confidentiality']},
    {id: 'ddos', label: 'A DDoS takes the booking site offline', options: ['Confidentiality', 'Integrity', 'Availability'], accept: ['Availability']},
    {id: 'grade', label: 'A student changes marks in the database', options: ['Confidentiality', 'Integrity', 'Availability'], accept: ['Integrity']},
    {id: 'flood', label: 'A flood destroys the only server', options: ['Confidentiality', 'Integrity', 'Availability'], accept: ['Availability']}]},
   ch('b', 'C1', 'How does confidentiality support integrity?', ['Encrypted data is always correct', 'If fewer people can access the data, fewer people can tamper with it', 'It makes data available', 'It removes the need for backups'], 'If fewer people can access the data, fewer people can tamper with it', 'This is the relationship given in the specification.')]},
  {id: 'q5b', title: 'IAAA', scenario: 'Put the stages in order, then answer.', parts: [
   {id: 'a', marks: 3, type: 'order', section: 'C2', prompt: 'Put the IAAA stages in the order they happen.', steps: [{id: 'i', text: 'Identification'}, {id: 'au', text: 'Authentication'}, {id: 'az', text: 'Authorisation'}, {id: 'ac', text: 'Accountability'}], base: ['i', 'au', 'az', 'ac']},
   ch('b', 'C2', 'Access control lists and role-based access are techniques for…', ['Identification', 'Authentication', 'Authorisation', 'Accountability'], 'Authorisation', 'They decide what an authenticated user may do.'),
   ch('c', 'C2', 'Why do shared logins break accountability?', ['They are slower', 'Actions cannot be traced to one individual', 'They use biometrics', 'They block MFA'], 'Actions cannot be traced to one individual', 'Audit logs only record the shared account.')]}]
}
];
