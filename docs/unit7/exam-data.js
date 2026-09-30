'use strict';
// Unit 7 exam practice (original questions in the style of the T Level core written exam). Uses ../revision.js.
window.REVISION_KEY = 'unit7-exam-v1';
window.REVISION_FILE = 'my-digital-environments-exam-practice.json';
const FOR_AGAINST = [
 {label: 'Points for / strengths', hint: 'e.g. this would help the business because…'},
 {label: 'Points against / limits', hint: 'e.g. but it depends on…'},
 {label: 'My judgement', hint: 'Overall… because the most important factor is…'}
];
const GUIDE = [
 {term: 'State / identify', text: 'Give a short answer: a word, phrase or fact. No explanation needed.'},
 {term: 'Describe', text: 'Say what something is or does, with its features. One mark per relevant, accurate point.'},
 {term: 'Explain', text: 'Give a point and then say why or how, using “because” or “so that”. Apply it to the scenario.'},
 {term: 'Discuss', text: 'Look at different sides of the issue: how it works, benefits, drawbacks and what it depends on.'},
 {term: 'Evaluate / justify', text: 'Weigh strengths against weaknesses for this scenario and reach a supported judgement.'},
 {term: 'Timing', text: 'About 1 minute per mark, plus reading time for the scenario.'}
];
window.REVISION_TESTS = [
{
 id: 'e1', title: 'Exam practice 1: short and medium answers', short: 'Practice 1',
 intro: 'Questions worth 1–6 marks, like the short-answer questions in the exam. Auto-marked questions are checked when you press Check; written answers are self-marked: tick only what your answer really says.',
 guide: GUIDE, guided: true,
 questions: [
 {id: 'e1q1', title: 'Harbour Fitness: hardware', scenario: 'Harbour Fitness runs three gyms. Members scan a card at the door, use treadmills with built-in screens, and staff use desktop PCs at reception. Head office wants a new PC for editing promotional videos.',
  parts: [
   {id: 'a', marks: 1, type: 'choice', section: 'H1', prompt: 'The treadmill contains a small computer that controls speed and incline. What type of computer system is this?', options: ['Server', 'Embedded system', 'Mainframe', 'Supercomputer'], answer: 'Embedded system', feedback: 'It is dedicated to one task inside a larger device.'},
   {id: 'b', marks: 2, type: 'text', section: 'H1', prompt: 'Describe two characteristics of the computer in the treadmill.', hint: 'Think about its size, power, task and software.', criteria: ['Dedicated to a single task / limited functions', 'Low power and/or low cost and/or small size', 'Often real-time, runs firmware stored in ROM/flash, rarely updated by the user (any one more)']},
   {id: 'c', marks: 4, type: 'text', section: 'H2', prompt: 'Explain two hardware features the video-editing PC should have. Link each to the task.', hint: 'Point → because → so the video editor can…', starter: 'The PC needs … because …', criteria: ['A multi-core, high clock-speed CPU', '…because rendering/encoding video uses a lot of processing and can run in parallel across cores', 'A powerful GPU and/or plenty of RAM (e.g. 32 GB) and/or a fast, large SSD', '…because effects/previews use the GPU, large project files must stay in memory, or big video files load and save quickly']},
   {id: 'd', marks: 2, type: 'text', section: 'H2', prompt: 'Explain why the PC’s processor needs cooling.', criteria: ['Processors produce heat when they work', 'Without cooling the CPU throttles (slows) or is damaged / the system becomes unstable']}]},
 {id: 'e1q2', title: 'Numbers', scenario: 'Show your working on paper.',
  parts: [
   {id: 'a', marks: 3, type: 'fields', section: 'NS', prompt: 'Complete the conversions.', grid: 3, fields: [
    {id: 'a', label: '1110 0101 to denary', accept: ['229']},
    {id: 'b', label: '156 to 8-bit binary', accept: ['10011100', '1001 1100']},
    {id: 'c', label: '9C to denary', accept: ['156']}]},
   {id: 'b', marks: 2, type: 'text', section: 'NS', prompt: 'A student says a 2 TB drive holds exactly 2 000 GiB. Explain why this is wrong.', criteria: ['TB is a decimal unit (10¹² bytes) but GiB is binary (2³⁰ bytes)', 'So 2 TB is about 1 863 GiB: fewer GiB than GB, which is why drives look smaller in the OS']}]},
 {id: 'e1q3', title: 'Harbour Fitness: software', scenario: 'The gym booking system is being rewritten by a small in-house team of three developers.',
  parts: [
   {id: 'a', marks: 2, type: 'text', section: 'SW1', prompt: 'State two functions of an operating system.', criteria: ['Any one of: memory management, process/task scheduling, file management', 'Any other of: peripheral/driver management, security and user accounts, user interface, network management']},
   {id: 'b', marks: 2, type: 'text', section: 'SW2', prompt: 'Describe how backup software helps the gym.', criteria: ['Copies data (full/incremental/differential) on a schedule to another location', 'So booking and member data can be restored after a failure, deletion or ransomware']},
   {id: 'c', marks: 4, type: 'text', section: 'SW3', prompt: 'Explain two features of an IDE that would help the team.', criteria: ['Debugger / breakpoints / stepping', '…lets them find logic errors by pausing and inspecting variables', 'One of: syntax highlighting, auto-complete, error checking, built-in version control, build/run tools', '…explained: e.g. spots mistakes early, speeds up typing, lets three developers share and roll back code']},
   {id: 'd', marks: 2, type: 'text', section: 'SW3', prompt: 'Explain one difference between a compiler and an interpreter.', criteria: ['Compiler translates the whole program into machine code/an executable before it runs; interpreter translates and runs one line at a time', 'Consequence: compiled code runs faster and the source is not needed; an interpreter stops at the first error, which is easier for testing']}]},
 {id: 'e1q4', title: 'Harbour Fitness: networks', scenario: 'Each gym has a LAN with a switch, Wi-Fi for members, and a router linking to the internet. Head office hosts the booking server.',
  parts: [
   {id: 'a', marks: 2, type: 'text', section: 'N4', prompt: 'Explain the difference between the role of the switch and the router.', criteria: ['Switch connects devices within one LAN, forwarding frames using MAC addresses', 'Router connects different networks (e.g. the LAN to the internet), forwarding packets using IP addresses']},
   {id: 'b', marks: 3, type: 'text', section: 'N6', prompt: 'Describe the structure of a data packet.', criteria: ['Header: source and destination IP addresses, sequence number (plus protocol/TTL)', 'Payload: the chunk of data being sent', 'Trailer: CRC/checksum for error checking']},
   {id: 'c', marks: 2, type: 'text', section: 'N8', prompt: 'Members complain that video workouts buffer in the evening. Explain one likely cause.', criteria: ['Bandwidth is shared: many members stream at once in the evening, causing congestion', 'So each device gets less throughput / packets are delayed or dropped, causing buffering']},
   {id: 'd', marks: 4, type: 'fields', section: 'N7', prompt: 'Name the protocol for each job.', grid: 2, fields: [
    {id: 'a', label: 'Booking website served securely', options: ['HTTPS', 'SMTP', 'DHCP', 'DNS', 'FTP'], accept: ['HTTPS']},
    {id: 'b', label: 'Members’ phones get an IP address', options: ['HTTPS', 'SMTP', 'DHCP', 'DNS', 'FTP'], accept: ['DHCP']},
    {id: 'c', label: 'Booking confirmations are sent', options: ['HTTPS', 'SMTP', 'DHCP', 'DNS', 'FTP'], accept: ['SMTP']},
    {id: 'd', label: 'harbourfitness.example is found', options: ['HTTPS', 'SMTP', 'DHCP', 'DNS', 'FTP'], accept: ['DNS']}]}]},
 {id: 'e1q5', title: 'Cloud and resilience', scenario: 'Harbour Fitness is moving its booking system to the cloud.',
  parts: [
   {id: 'a', marks: 2, type: 'text', section: 'C1', prompt: 'Describe the difference between a public and a private cloud.', criteria: ['Public: infrastructure owned by a provider and shared by many customers', 'Private: used by one organisation only, giving more control but a higher cost']},
   {id: 'b', marks: 3, type: 'text', section: 'C1', prompt: 'The gym chooses PaaS. State three things the gym must still manage.', criteria: ['Application software', 'Data', 'User accounts']},
   {id: 'c', marks: 2, type: 'text', section: 'R1', prompt: 'Explain how device hardening improves resilience.', criteria: ['Removing unneeded ports, services, apps, accounts and permissions', 'Reduces the attack surface, so there are fewer vulnerabilities to exploit']}]}
 ]
},
{
 id: 'e2', title: 'Exam practice 2: extended answers', short: 'Practice 2 (long)',
 intro: 'The longer questions are marked by level: the examiner judges the quality of the whole answer. Plan first, write developed paragraphs linked to the scenario, then mark yourself against the levels.',
 guide: GUIDE, guided: true,
 questions: [
 {id: 'e2q1', title: 'Virtualising a college’s servers', scenario: 'Westbrook College runs 14 physical servers in one room: file, email, web, database, print and several test servers for computing students. Many run at 10% load. The servers are six years old and the room has had two cooling failures this year.',
  parts: [
   {id: 'a', marks: 2, type: 'text', section: 'V1', prompt: 'Improve this weak point. A student wrote: “Virtualisation saves money.” Rewrite it as one developed point applied to Westbrook.', starter: 'Virtualising would save money because…', criteria: ['Why: several lightly loaded servers can run as VMs on a few hosts (sharing/aggregation)', 'Applied: fewer servers to buy, power and cool, which matters because the room has cooling problems']},
   {id: 'b', marks: 9, type: 'essay', section: 'V1', prompt: 'Discuss the benefits and drawbacks for Westbrook of replacing its physical servers with virtual machines on a type 1 hypervisor.', structure: 'Benefits applied to Westbrook → drawbacks applied to Westbrook → what success depends on → short conclusion.', plan: FOR_AGAINST, criteria: ['Consolidation: 14 servers running at 10% load could run on 2–3 hosts, cutting hardware, power and cooling costs', 'Lower carbon footprint and less heat, reducing the cooling-failure risk', 'Central management through the hypervisor; easy to create and remove servers', 'Snapshots and portability improve disaster recovery; VMs can move if a host fails (resilience)', 'Safe, disposable test servers for computing students (testing and education benefit); isolation contains problems', 'Type 1 runs on bare metal, so it is efficient and secure compared with type 2', 'Drawbacks: extra load on the hosts; VMs run slower than bare hardware; performance can be misleading when VMs share a host', 'Consolidation creates a single point of failure unless there are at least two hosts and shared storage; staff need new skills and licences cost money', 'A balanced conclusion applied to Westbrook']},
   {id: 'c', marks: 6, type: 'essay', section: 'R1', prompt: 'Explain how Westbrook could make its new environment more resilient.', structure: 'Choose three methods from the specification, explain each and apply it to the college.', plan: [{label: 'Method 1', hint: 'e.g. redundancy'}, {label: 'Method 2', hint: 'e.g. backups: onsite, offsite, cloud'}, {label: 'Method 3', hint: 'e.g. patching, hardening, standby site, training'}], criteria: ['Redundancy: two or more hosts, RAID, dual power supplies and network links remove single points of failure', 'Backups: onsite for fast restores plus offsite/cloud copies that survive a local disaster; test recovery procedures', 'Updates and patches applied promptly to the hypervisor and VMs to close vulnerabilities', 'Device hardening: close unused ports and services, remove default accounts, least privilege', 'A warm or cold site or cloud replicas for disaster recovery, chosen by cost and acceptable downtime', 'Staff training and standard operating procedures; secure disposal of the old servers’ drives']}]},
 {id: 'e2q2', title: 'Moving a shop to the cloud', scenario: 'Kemi’s Crafts sells handmade goods online. Its website and stock database run on one server in the owner’s spare room. Sales are steady most of the year but grow ten times before Christmas. The owner has limited IT skills.',
  parts: [
   {id: 'a', marks: 3, type: 'text', section: 'C1', prompt: 'Explain how elasticity would help Kemi’s Crafts.', criteria: ['Resources scale up automatically when demand rises', 'Handles the ten-times Christmas peak without the site slowing or crashing', 'Scales back down afterwards, so she only pays for extra capacity while it is needed']},
   {id: 'b', marks: 12, type: 'essay', section: 'C1', prompt: 'Evaluate whether Kemi’s Crafts should use IaaS or SaaS for its online shop.', structure: 'What each model means and who manages what → strengths and limits of each for this business → recommendation with reasons.', plan: FOR_AGAINST, criteria: ['IaaS: rents virtual servers; the client manages the OS, middleware, runtime, applications, data and user accounts', 'IaaS gives most control and flexibility, e.g. keep the existing website and database', 'But the owner has limited IT skills: patching and securing the OS would be a risk and take time or paid help', 'SaaS: a ready-made e-commerce platform; the client manages only user accounts and data', 'SaaS needs no installation or maintenance; the provider handles security, updates, backups and scaling', 'SaaS limits: less customisation, monthly fees, depends on the provider (lock-in) and on the internet', 'Both remove the single server in the spare room (resilience, no hardware cost) and offer elasticity for Christmas', 'Security and data protection of customer data with each option', 'A justified recommendation (likely SaaS, given skills) that weighs the most important factors']}]}
 ]
}
];
