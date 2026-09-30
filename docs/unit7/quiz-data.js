'use strict';
// Unit 7 knowledge quizzes (original questions). Uses the shared engine in ../revision.js.
window.REVISION_KEY = 'unit7-quiz-v1';
window.REVISION_FILE = 'my-digital-environments-quiz-answers.json';
const ch = (id, section, prompt, options, answer, feedback, context) => ({id, marks: 1, type: 'choice', section, prompt, options, answer, feedback, context});
window.REVISION_TESTS = [
{
 id: 'q1', title: 'Quiz 1: Number systems', short: '1 Numbers', guided: true,
 intro: 'Convert between binary, denary and hexadecimal, and use units of data. Show your working on paper, then type the answer and press Check.',
 questions: [
  {id: 'q1a', title: 'Conversions', scenario: 'Type each answer with no spaces or prefixes.', parts: [
   {id: 'a', marks: 6, type: 'fields', section: 'NS', prompt: 'Convert each number.', grid: 3, fields: [
    {id: 'b1', label: '1011 0110 (binary) to denary', accept: ['182']},
    {id: 'b2', label: '0010 1101 (binary) to denary', accept: ['45']},
    {id: 'd1', label: '200 (denary) to 8-bit binary', accept: ['11001000', '1100 1000']},
    {id: 'd2', label: '77 (denary) to 8-bit binary', accept: ['01001101', '0100 1101']},
    {id: 'h1', label: '3F (hex) to denary', accept: ['63']},
    {id: 'h2', label: '1101 1010 (binary) to hex', accept: ['DA', 'da']}]},
   ch('b', 'NS', 'What is the largest denary number an 8-bit unsigned binary number can hold?', ['128', '255', '256', '512'], '255', 'Eight 1s = 128+64+32+16+8+4+2+1 = 255. There are 256 values because 0 is included.'),
   ch('c', 'NS', 'Why do technicians use hexadecimal?', ['Computers process hex faster than binary', 'It is a shorter, easier-to-read way to write binary: one hex digit = 4 bits', 'It uses less storage', 'It is needed for encryption'], 'It is a shorter, easier-to-read way to write binary: one hex digit = 4 bits', 'Computers still store binary; hex just makes long binary values (MAC addresses, colours, memory addresses) readable.')]},
  {id: 'q1b', title: 'Units and arithmetic', scenario: 'Choose the best answer.', parts: [
   ch('a', 'NS', 'How many bytes are in 1 kibibyte (KiB)?', ['1000', '1024', '8', '8192'], '1024', 'Binary prefixes (KiB, MiB, GiB) use powers of 2: 2¹⁰ = 1024. Decimal prefixes (kB, MB) use 1000.'),
   ch('b', 'NS', 'What is 0110 1001 + 0101 0111 in binary?', ['1100 0000', '1011 1110', '1100 0001', '1010 0000'], '1100 0000', '105 + 87 = 192 = 1100 0000. Check by converting back to denary.'),
   ch('c', 'NS', 'What happens if the answer to an 8-bit addition needs a 9th bit?', ['The computer adds an extra bit automatically', 'An overflow error: the extra bit is lost', 'The answer is rounded', 'The CPU switches to hexadecimal'], 'An overflow error: the extra bit is lost', 'The result does not fit the register, so it is wrong unless the overflow is detected.'),
   ch('d', 'NS', 'In 8-bit two’s complement, what is 1111 1110?', ['254', '−2', '−126', '−1'], '−2', 'The top bit is worth −128: −128 + 64+32+16+8+4+2 = −2.')]}]
},
{
 id: 'q2', title: 'Quiz 2: Hardware', short: '2 Hardware', guided: true,
 intro: 'Physical computer systems, internal components and devices.',
 questions: [
  {id: 'q2a', title: 'Types of computer system', scenario: 'Match each situation to the best system.', parts: [
   ch('a', 'H1', 'A washing machine controls its drum, water and heater with a small built-in computer.', ['Server', 'Embedded system', 'Mainframe', 'Quantum computer'], 'Embedded system', 'A dedicated computer built into a larger device, with one job, low power and low cost.'),
   ch('b', 'H1', 'A bank processes millions of card transactions every hour with very high reliability.', ['Personal computer', 'Mainframe', 'Tablet', 'Embedded system'], 'Mainframe', 'Mainframes handle huge volumes of transactions reliably, with redundant components.'),
   ch('c', 'H1', 'A research team models the climate using thousands of processors working together.', ['Supercomputer', 'Server', 'Laptop', 'Smart speaker'], 'Supercomputer', 'Supercomputers run massively parallel calculations for science and simulation.'),
   ch('d', 'H1', 'Which is a common characteristic of embedded systems?', ['Easy to upgrade with new software', 'Dedicated to one task, low power and often real-time', 'Very high processing power', 'A full desktop operating system'], 'Dedicated to one task, low power and often real-time', 'They are designed for one job and usually run firmware in ROM or flash.')]},
  {id: 'q2b', title: 'Inside the computer', scenario: 'Choose the best answer.', parts: [
   ch('a', 'H2', 'Which memory loses its contents when the power is switched off?', ['ROM', 'RAM', 'SSD', 'Flash'], 'RAM', 'RAM is volatile. ROM and flash storage keep their contents.'),
   ch('b', 'H2', 'What does ROM usually hold in a PC?', ['The user’s documents', 'The firmware (BIOS/UEFI) that starts the computer', 'Open programs', 'Virtual memory'], 'The firmware (BIOS/UEFI) that starts the computer', 'It must survive power-off so the computer can boot.'),
   ch('c', 'H2', 'Why does cache improve CPU performance?', ['It stores files permanently', 'It holds frequently used data and instructions very close to the CPU, faster than RAM', 'It increases the clock speed', 'It adds more cores'], 'It holds frequently used data and instructions very close to the CPU, faster than RAM', 'The CPU waits less for data from main memory.'),
   ch('d', 'H2', 'Which storage has no moving parts, is fast and resists knocks?', ['Magnetic hard disk', 'Solid state drive', 'Optical disc', 'Magnetic tape'], 'Solid state drive', 'SSDs use flash memory, so they suit laptops and phones.'),
   ch('e', 'H2', 'A video editor needs to render 3D effects quickly. Which component matters most?', ['Network interface card', 'GPU', 'Optical drive', 'CMOS battery'], 'GPU', 'A GPU has thousands of small cores for parallel graphics work.'),
   ch('f', 'H2', 'A gaming PC CPU gets very hot under load. What is the best cooling choice for high performance?', ['No cooling', 'Liquid cooling', 'Removing the case', 'A slower hard disk'], 'Liquid cooling', 'Coolant carries heat to a radiator: quieter and better for high-power CPUs, though it costs more.')]}]
},
{
 id: 'q3', title: 'Quiz 3: Software', short: '3 Software', guided: true,
 intro: 'Operating systems, utilities, development tools and applications.',
 questions: [
  {id: 'q3a', title: 'Operating systems and utilities', scenario: 'Choose the best answer.', parts: [
   ch('a', 'SW1', 'Which type of operating system must respond within a guaranteed time, e.g. in a car’s airbag controller?', ['Multi-user', 'Real-time', 'Single-user single-task', 'Distributed'], 'Real-time', 'Real-time operating systems guarantee a response within a strict time limit.'),
   ch('b', 'SW1', 'Which is NOT a job of the operating system?', ['Memory management', 'Managing peripherals through drivers', 'Writing the user’s essay', 'Providing a user interface'], 'Writing the user’s essay', 'That is application software. The OS manages hardware, memory, files, processes, security and the interface.'),
   ch('c', 'SW2', 'Which utility reorganises the parts of files on a magnetic disk so they are stored together?', ['Antivirus', 'Defragmenter', 'Compression', 'Firewall'], 'Defragmenter', 'Contiguous files are read faster. SSDs do not need defragmenting.'),
   ch('d', 'SW2', 'Which compression must be used for a program file or spreadsheet?', ['Lossy', 'Lossless', 'Either', 'Neither'], 'Lossless', 'Every bit must be restored exactly or the file will not work.')]},
  {id: 'q3b', title: 'Development tools and applications', scenario: 'Choose the best answer.', parts: [
   ch('a', 'SW3', 'Which translator converts the whole program into machine code before it runs?', ['Interpreter', 'Compiler', 'Assembler for high-level code', 'Debugger'], 'Compiler', 'A compiler produces an executable; an interpreter translates and runs one line at a time.'),
   ch('b', 'SW3', 'Which IDE feature lets a programmer pause the program on a line and inspect variables?', ['Syntax highlighting', 'Breakpoints (debugger)', 'Auto-complete', 'Version control'], 'Breakpoints (debugger)', 'Breakpoints and stepping help find logic errors.'),
   ch('c', 'SW3', 'Why use version control such as Git?', ['It compiles code faster', 'It records every change so a team can collaborate and roll back', 'It removes bugs automatically', 'It encrypts code'], 'It records every change so a team can collaborate and roll back', 'Branches and merges let many developers work on the same project safely.'),
   ch('d', 'SW4', 'A company wants one system to hold customer details, sales history and follow-up tasks. Which application type?', ['CRM software', 'Photo editor', 'Compiler', 'Defragmenter'], 'CRM software', 'Customer relationship management software centralises customer data.')]}]
},
{
 id: 'q4', title: 'Quiz 4: Networks', short: '4 Networks', guided: true,
 intro: 'Network types, connectivity, topologies, models, components, the OSI and TCP/IP models, packets, protocols, bandwidth and latency.',
 questions: [
  {id: 'q4a', title: 'Types, topologies and models', scenario: 'Choose the best answer.', parts: [
   ch('a', 'N1', 'A council connects its offices across one city with high-speed links. Which network type?', ['PAN', 'LAN', 'MAN', 'WLAN'], 'MAN', 'A metropolitan area network covers a town or city.'),
   ch('b', 'N3', 'Which topology has every device connected to a central switch, so one cable fault only affects one device?', ['Bus', 'Star', 'Ring', 'Full mesh'], 'Star', 'The switch isolates faults, but it is a single point of failure.'),
   ch('c', 'N3', 'In which model do all devices share files directly with no central server?', ['Client–server', 'Peer-to-peer', 'Thin client', 'Cloud'], 'Peer-to-peer', 'Cheap and simple for small groups, but hard to manage and back up.'),
   ch('d', 'N2', 'Which connection is best for a long, high-speed link between two buildings with electrical interference?', ['Copper twisted pair', 'Fibre optic', 'Bluetooth', 'Infrared'], 'Fibre optic', 'Light signals are immune to electromagnetic interference and travel long distances.')]},
  {id: 'q4b', title: 'Layers and protocols', scenario: 'Select the correct layer or protocol.', parts: [
   {id: 'a', marks: 4, type: 'order', section: 'N5', prompt: 'Put the TCP/IP layers in order from top (closest to the user) to bottom.', steps: [{id: 'app', text: 'Application'}, {id: 'tra', text: 'Transport'}, {id: 'int', text: 'Internet'}, {id: 'net', text: 'Network access'}], base: ['app', 'tra', 'int', 'net']},
   {id: 'b', marks: 6, type: 'fields', section: 'N7', prompt: 'Which protocol does each job?', grid: 2, fields: [
    {id: 'web', label: 'Secure web pages', options: ['HTTPS', 'FTP', 'SMTP', 'IMAP', 'DHCP', 'DNS'], accept: ['HTTPS']},
    {id: 'send', label: 'Sending email to a mail server', options: ['HTTPS', 'FTP', 'SMTP', 'IMAP', 'DHCP', 'DNS'], accept: ['SMTP']},
    {id: 'sync', label: 'Reading email kept in sync on several devices', options: ['HTTPS', 'FTP', 'SMTP', 'IMAP', 'DHCP', 'DNS'], accept: ['IMAP']},
    {id: 'ip', label: 'Giving a device an IP address automatically', options: ['HTTPS', 'FTP', 'SMTP', 'IMAP', 'DHCP', 'DNS'], accept: ['DHCP']},
    {id: 'name', label: 'Turning a domain name into an IP address', options: ['HTTPS', 'FTP', 'SMTP', 'IMAP', 'DHCP', 'DNS'], accept: ['DNS']},
    {id: 'file', label: 'Transferring files to a server', options: ['HTTPS', 'FTP', 'SMTP', 'IMAP', 'DHCP', 'DNS'], accept: ['FTP']}]},
   {id: 'c', marks: 4, type: 'fields', section: 'N5', prompt: 'At which OSI layer does each work?', grid: 2, fields: [
    {id: 'sw', label: 'A switch (MAC addresses)', options: ['Physical', 'Data link', 'Network', 'Transport', 'Application'], accept: ['Data link']},
    {id: 'rt', label: 'A router (IP addresses)', options: ['Physical', 'Data link', 'Network', 'Transport', 'Application'], accept: ['Network']},
    {id: 'tcp', label: 'TCP', options: ['Physical', 'Data link', 'Network', 'Transport', 'Application'], accept: ['Transport']},
    {id: 'cab', label: 'A fibre cable', options: ['Physical', 'Data link', 'Network', 'Transport', 'Application'], accept: ['Physical']}]}]},
  {id: 'q4c', title: 'Packets and performance', scenario: 'Choose the best answer.', parts: [
   ch('a', 'N6', 'Which part of a packet holds the CRC used to detect errors?', ['Header', 'Payload', 'Trailer', 'Sequence number'], 'Trailer', 'The receiver recalculates the CRC and compares it with the trailer.'),
   ch('b', 'N6', 'What lets the receiver put packets back in the right order?', ['TTL', 'Sequence number', 'MAC address', 'Port number'], 'Sequence number', 'Packets can take different routes and arrive out of order.'),
   ch('c', 'N8', 'A video call is choppy even though the download speed is high. Which is the most likely cause?', ['High latency and jitter', 'Too much bandwidth', 'Lossless compression', 'A fast SSD'], 'High latency and jitter', 'Real-time services need low, steady delay as well as enough bandwidth.'),
   ch('d', 'N8', 'How long does a 400 Mb file take to download at 50 Mbps (ignoring overheads)?', ['2 seconds', '8 seconds', '20 seconds', '50 seconds'], '8 seconds', 'Time = size ÷ speed = 400 ÷ 50 = 8 s. Check both are in bits.')]}]
},
{
 id: 'q5', title: 'Quiz 5: Virtual, cloud and resilient environments', short: '5 Virtual & cloud', guided: true,
 intro: 'Virtualisation, cloud types and delivery models, and resilience.',
 questions: [
  {id: 'q5a', title: 'Virtualisation', scenario: 'Choose the best answer.', parts: [
   ch('a', 'V1', 'Which hypervisor is installed directly on the server hardware?', ['Type 1 (bare metal)', 'Type 2 (hosted)', 'Emulator app', 'A virtual switch'], 'Type 1 (bare metal)', 'Type 1 is efficient and secure; type 2 runs as an application on a normal OS.'),
   ch('b', 'V1', 'Which feature means a VM can be copied to another host as a set of files?', ['Isolation', 'Portability', 'Aggregation', 'Emulation'], 'Portability', 'This also improves disaster recovery.'),
   ch('c', 'V1', 'Which is a drawback of virtualisation?', ['Fewer physical servers', 'Extra load on the host, so VMs can run slower than on real hardware', 'Easier testing', 'Snapshots'], 'Extra load on the host, so VMs can run slower than on real hardware', 'VMs share the host’s resources, so performance can also be falsely represented.')]},
  {id: 'q5b', title: 'Cloud', scenario: 'Use the specification’s responsibility split.', parts: [
   {id: 'a', marks: 3, type: 'fields', section: 'C1', prompt: 'Which delivery model is each example?', grid: 3, fields: [
    {id: 'm365', label: 'Microsoft 365 in a browser', options: ['IaaS', 'PaaS', 'SaaS'], accept: ['SaaS']},
    {id: 'vm', label: 'Renting a virtual server and installing your own OS settings and software', options: ['IaaS', 'PaaS', 'SaaS'], accept: ['IaaS']},
    {id: 'app', label: 'Uploading your code to a platform that runs it for you', options: ['IaaS', 'PaaS', 'SaaS'], accept: ['PaaS']}]},
   ch('b', 'C1', 'With SaaS, what does the client still manage?', ['Hardware and virtualisation', 'The runtime', 'Only user accounts and data', 'The operating system'], 'Only user accounts and data', 'Everything else is managed by the provider.'),
   ch('c', 'C1', 'Which cloud benefit lets a ticket website handle a sudden rush of buyers?', ['Elasticity', 'Isolation', 'Emulation', 'Latency'], 'Elasticity', 'Resources scale up automatically for the peak and down afterwards.')]},
  {id: 'q5c', title: 'Resilience', scenario: 'Choose the best answer.', parts: [
   ch('a', 'R1', 'Which standby site has systems running and data mirrored for almost immediate failover?', ['Cold site', 'Warm site', 'Hot site', 'Backup tape'], 'Hot site', 'Fastest recovery, highest cost.'),
   ch('b', 'R1', 'Removing unused ports, services and default accounts from a server is called…', ['Device hardening', 'Redundancy', 'Defragmentation', 'Aggregation'], 'Device hardening', 'It reduces the attack surface.'),
   ch('c', 'R1', 'Why is an offsite or cloud backup needed as well as an onsite one?', ['It is faster to restore', 'It survives a fire, flood or theft at the main site', 'It removes the need for patches', 'It is cheaper than no backup'], 'It survives a fire, flood or theft at the main site', 'Onsite backups restore quickly; offsite copies survive a local disaster.'),
   ch('d', 'R1', 'Which is a benefit of a resilient digital environment?', ['Reduced downtime', 'More single points of failure', 'Higher latency', 'Fewer backups needed'], 'Reduced downtime', 'Services stay available, protecting income and reputation.')]}]
}
];
