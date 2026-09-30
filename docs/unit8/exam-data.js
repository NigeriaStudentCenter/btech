'use strict';
// Unit 8 Security exam practice (original questions in the style of the T Level core written exam). Uses ../revision.js.
window.REVISION_KEY = 'unit8-exam-v1';
window.REVISION_FILE = 'my-security-exam-practice.json';
const FOR_AGAINST = [
 {label: 'Points for / strengths', hint: 'e.g. this control would protect the business because…'},
 {label: 'Points against / limits', hint: 'e.g. but it costs… / it depends on…'},
 {label: 'My judgement', hint: 'Overall… because the most important risk is…'}
];
const GUIDE = [
 {term: 'State / identify', text: 'Give a short answer: a word, phrase or fact.'},
 {term: 'Describe', text: 'Say what something is or does. One mark per relevant, accurate point.'},
 {term: 'Explain', text: 'Give a point and then say why or how, using “because” or “so that”. Apply it to the scenario.'},
 {term: 'Discuss', text: 'Look at different sides: how it works, benefits, drawbacks and what it depends on.'},
 {term: 'Evaluate / justify', text: 'Weigh strengths against weaknesses for this scenario and reach a supported judgement.'},
 {term: 'Timing', text: 'About 1 minute per mark, plus reading time for the scenario.'}
];
window.REVISION_TESTS = [
{
 id: 'e1', title: 'Exam practice 1: short and medium answers', short: 'Practice 1',
 intro: 'Questions worth 1–6 marks. Auto-marked questions are checked when you press Check; written answers are self-marked: tick only what your answer really says.',
 guide: GUIDE, guided: true,
 questions: [
 {id: 'e1q1', title: 'Brightside Dental: risks', scenario: 'Brightside Dental has three surgeries. It stores patient records, staff salaries and supplier contracts on a server, and staff use swipe cards and PINs to enter the building.',
  parts: [
   {id: 'a', marks: 3, type: 'text', section: 'S1', prompt: 'Identify three types of confidential information Brightside holds, one from each category.', criteria: ['Human resources: staff salaries/benefits or staff personal details', 'Commercially sensitive: patient (client) details or supplier contracts', 'Access information: swipe card data, PINs, usernames/passwords']},
   {id: 'b', marks: 2, type: 'text', section: 'S1', prompt: 'Explain why Brightside must keep patient details confidential.', criteria: ['To protect patient privacy / comply with data protection regulations', 'Consequence: a leak could bring fines, loss of trust, legal action or loss of licence to practise']},
   {id: 'c', marks: 4, type: 'text', section: 'S1', prompt: 'Explain two impacts on Brightside if patient records were leaked.', criteria: ['Impact 1 named, e.g. non-compliance/fines or loss of licence to practise', '…explained for Brightside, e.g. the regulator fines the practice / it may be stopped from operating', 'Impact 2 named, e.g. loss of trust, damaged image, legal action, financial loss', '…explained, e.g. patients move to another dentist, reducing income']}]},
 {id: 'e1q2', title: 'Threats', scenario: 'A receptionist receives an email that appears to come from the practice’s software supplier asking them to log in to a link to “renew the licence today”.',
  parts: [
   {id: 'a', marks: 1, type: 'choice', section: 'T3', prompt: 'Name this type of attack.', options: ['Phishing', 'Vishing', 'Buffer overflow', 'DDoS'], answer: 'Phishing', feedback: 'It is an email pretending to be a trusted organisation. If it used the receptionist’s name and real details it would be spear phishing.'},
   {id: 'b', marks: 3, type: 'text', section: 'T3', prompt: 'Describe three features that could show the email is not genuine.', criteria: ['Look-alike or unusual sender address', 'Urgency or threats (“today”)', 'Link to an unfamiliar web address / generic greeting / unexpected request for a password']},
   {id: 'c', marks: 2, type: 'text', section: 'T1', prompt: 'Explain how ransomware could affect the practice.', criteria: ['Encrypts patient records/files and demands payment', 'Appointments and treatment records unavailable, so the practice cannot operate normally (disruption of service)']},
   {id: 'd', marks: 4, type: 'text', section: 'T2', prompt: 'The online booking form is vulnerable to SQL injection. Explain what this means and one way to prevent it.', criteria: ['The attacker enters SQL code into a form input', 'The code becomes part of the database query, so it can read, change or delete data', 'Prevention: parameterised queries / prepared statements', '…because input is treated as data, not as code (or input validation, least-privilege database account)']}]},
 {id: 'e1q3', title: 'Vulnerabilities', scenario: 'The practice server runs an operating system that no longer receives updates, and staff often leave their PCs unlocked.',
  parts: [
   {id: 'a', marks: 2, type: 'text', section: 'V1', prompt: 'Explain why an unsupported operating system is a vulnerability.', criteria: ['No security patches are released for newly discovered weaknesses', 'Attackers can exploit known or zero-day vulnerabilities that will never be fixed']},
   {id: 'b', marks: 2, type: 'text', section: 'V2', prompt: 'Describe two ways to improve staff cyber hygiene.', criteria: ['Lock unattended machines (e.g. automatic screen lock, Windows+L)', 'Do not write down passwords / use a password manager / training']},
   {id: 'c', marks: 2, type: 'text', section: 'V3', prompt: 'Explain one way the practice can stop tailgating into the staff area.', criteria: ['A control: staff training/no-tailgating policy, turnstile or airlock door, CCTV or guard monitoring', 'Why: only people who badge in themselves can enter, so unauthorised people cannot follow']}]},
 {id: 'e1q4', title: 'Controls', scenario: 'Brightside wants to improve its security.',
  parts: [
   {id: 'a', marks: 2, type: 'text', section: 'M3', prompt: 'Explain how multi-factor authentication would protect staff accounts.', criteria: ['Needs two or more different factors, e.g. password plus a code from an app', 'A stolen or phished password alone is not enough to log in']},
   {id: 'b', marks: 3, type: 'fields', section: 'M4', prompt: 'Name the backup type.', grid: 3, fields: [
    {id: 'a', label: 'Copies everything', options: ['Full', 'Incremental', 'Differential'], accept: ['Full']},
    {id: 'b', label: 'Changes since the last backup of any type', options: ['Full', 'Incremental', 'Differential'], accept: ['Incremental']},
    {id: 'c', label: 'Changes since the last full backup', options: ['Full', 'Incremental', 'Differential'], accept: ['Differential']}]},
   {id: 'c', marks: 2, type: 'text', section: 'M2', prompt: 'Explain why passwords should be stored as hashes.', criteria: ['A hash is one-way and cannot be turned back into the password', 'If the database is stolen the passwords are not directly readable; login compares hashes']},
   {id: 'd', marks: 3, type: 'text', section: 'C2', prompt: 'Describe the role of authorisation and accountability in Brightside’s patient record system.', criteria: ['Authorisation: users only access records and actions their role allows (e.g. receptionists cannot see clinical notes)', 'Techniques: role-based access control / access control lists', 'Accountability: audit logs record who viewed or changed each record, so actions can be traced']}]}
 ]
},
{
 id: 'e2', title: 'Exam practice 2: extended answers', short: 'Practice 2 (long)',
 intro: 'The longer questions are marked by level: the examiner judges the quality of the whole answer. Plan first, write developed paragraphs linked to the scenario, then mark yourself against the levels.',
 guide: GUIDE, guided: true,
 questions: [
 {id: 'e2q1', title: 'Securing a growing online shop', scenario: 'StitchBox sells craft kits online. It has 12 staff, some working from home. It stores customer names, addresses and order histories; payments are handled by a payment provider. Last month a member of staff clicked a phishing link and their email account was used to send spam. The owner has a budget of £6,000 for security this year.',
  parts: [
   {id: 'a', marks: 2, type: 'text', section: 'T3', prompt: 'Improve this weak point. A student wrote: “Staff training stops phishing.” Rewrite it as one developed point applied to StitchBox.', starter: 'Training would help StitchBox because…', criteria: ['How: staff learn to spot red flags (sender, urgency, links) and report suspicious emails', 'Applied/limited: reduces the chance of a repeat of last month’s incident, but people still make mistakes, so combine with MFA']},
   {id: 'b', marks: 12, type: 'essay', section: 'M3', prompt: 'Evaluate the security measures StitchBox should prioritise with its £6,000 budget.', structure: 'Main risks for StitchBox → two or three measures, each explained and applied → benefits and drawbacks/costs → justified priority order.', plan: FOR_AGAINST, criteria: ['Identifies the main risks: phishing/account takeover, remote working on insecure Wi-Fi, loss of customer data, ransomware', 'MFA on email and systems: cheap, stops stolen passwords being used; drawback: login slower, recovery process needed', 'Staff training: tackles the cause of last month’s incident; drawback: needs repeating, not foolproof', 'VPN or secure remote access for home workers; drawback: cost/setup, can slow connections', 'Backups (offsite/offline, tested) to mitigate ransomware and protect availability', 'Updates/patching, anti-malware and device hardening on staff devices', 'Password manager and password policy to stop weak and reused passwords', 'Considers cost against the £6,000 budget and the size of the business', 'Links to CIA: customer data confidentiality, availability of the shop', 'Justified priority order, e.g. MFA and training first because they address the incident that already happened']}]},
 {id: 'e2q2', title: 'CIA and IAAA in a hospital', scenario: 'Northfield Hospital is moving to a new electronic patient record system used by doctors, nurses, receptionists and managers across 20 wards. Staff currently share logins on some ward PCs.',
  parts: [
   {id: 'a', marks: 3, type: 'text', section: 'C1', prompt: 'Explain how the three elements of the CIA triad interrelate in the patient record system.', criteria: ['Confidentiality: only authorised staff access patient data', 'Integrity: records are accurate and untampered; confidentiality supports this because fewer people can change them', 'Availability: records must be available to clinicians when needed; available data is only useful if its integrity is intact']},
   {id: 'b', marks: 9, type: 'essay', section: 'C2', prompt: 'Discuss how Northfield Hospital could apply the IAAA model to the new system.', structure: 'Take each stage of IAAA in turn: technique, why it suits the hospital, a drawback. Finish with the problem of shared logins.', plan: [{label: 'Identification and authentication', hint: 'cards, usernames, biometrics, MFA'}, {label: 'Authorisation', hint: 'roles, ACLs'}, {label: 'Accountability', hint: 'audit logs, activity'}], criteria: ['Identification: individual usernames or staff ID cards (possession) or biometrics', 'Authentication: MFA such as smart card plus PIN, or biometrics, suited to busy wards (fast tap-in)', 'Drawback: biometrics cannot be changed if compromised; cards lost; cost of readers', 'Authorisation: role-based access (doctor, nurse, receptionist, manager) so each sees only what they need', 'ACLs for specific records or wards; roles must be updated when staff change jobs', 'Accountability: audit logs record who viewed or changed each record', 'Shared logins must end because they break accountability (actions cannot be traced) and weaken confidentiality', 'Balance with availability: clinicians need fast access in emergencies (e.g. break-glass access that is logged)', 'Supported conclusion']}]}
 ]
}
];
