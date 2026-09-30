'use strict';
// Unit 19 knowledge quizzes (original questions). Uses the shared engine in ../revision.js.
window.REVISION_KEY = 'unit19-quiz-v1';
window.REVISION_FILE = 'my-networking-quiz-answers.json';
const ch = (id, section, prompt, options, answer, feedback, context) => ({id, marks: 1, type: 'choice', section, prompt, options, answer, feedback, context});
window.REVISION_TESTS = [
{
 id: 'q1', title: 'Quiz 1: Network types, topologies and models', short: '1 Types & models', guided: true,
 intro: 'Check you can match network types, topologies and models to real situations. Press Check after each answer.',
 questions: [
  {id: 'q1a', title: 'Choosing network types', scenario: 'Pick the best answer for each situation.', parts: [
   ch('a', 'A1a', 'A café wants customers to use the internet on their own phones.', ['LAN with cables to each table', 'WLAN', 'SAN', 'MAN'], 'WLAN', 'Customers bring mobile devices and move around, so wireless is the only practical choice.'),
   ch('b', 'A1a', 'A bank links its offices in London, Lagos and New York.', ['PAN', 'LAN', 'WAN', 'WLAN'], 'WAN', 'Sites in different countries are joined by a wide area network, usually through service providers.'),
   ch('c', 'A1a', 'Suppliers log in to see a company’s stock levels and orders.', ['Intranet', 'Extranet', 'Internet', 'PAN'], 'Extranet', 'An extranet opens part of a private system to trusted outside users.'),
   ch('d', 'A1a', 'Many servers in a data centre need very fast shared access to storage.', ['SAN', 'WLAN', 'PAN', 'Extranet'], 'SAN', 'A storage area network gives servers dedicated, high-speed access to shared storage.'),
   ch('e', 'A1a', 'Staff-only web pages for booking rooms and reading HR policies.', ['Internet', 'Extranet', 'Intranet', 'Cloud'], 'Intranet', 'An intranet is private to the organisation’s own staff.')]},
  {id: 'q1b', title: 'Topologies', scenario: 'Think about how each layout behaves when something fails.', parts: [
   ch('a', 'A1b', 'In which topology does one broken cable stop every device from communicating?', ['Star', 'Bus', 'Mesh', 'Extended star'], 'Bus', 'All devices share one cable, so a break splits the network.'),
   ch('b', 'A1b', 'Which topology is used in almost every modern office LAN?', ['Bus', 'Ring', 'Star / extended star', 'Full mesh'], 'Star / extended star', 'Each device has its own cable to a switch, so faults are isolated and devices are easy to add.'),
   ch('c', 'A1b', 'Which topology gives the most alternative paths but costs the most to cable?', ['Mesh', 'Star', 'Bus', 'Ring'], 'Mesh', 'Every device links to many others, so it survives failures but needs lots of cables and ports.'),
   ch('d', 'A1b', 'Which IEEE standard family defines Wi-Fi?', ['802.3', '802.11', '802.15', '802.1Q'], '802.11', '802.3 is wired Ethernet, 802.15 is personal networks such as Bluetooth.')]},
  {id: 'q1c', title: 'Network models and trends', scenario: 'Match the model or trend to the client.', parts: [
   ch('a', 'A1c', 'A three-person hairdresser wants to share one printer and a few files with no IT staff.', ['Peer-to-peer', 'Client/server', 'Thin client', 'SAN'], 'Peer-to-peer', 'Cheap and quick to set up; there are too few users to need a server.'),
   ch('b', 'A1c', 'A college with 800 PCs needs central logins, permissions and backups.', ['Peer-to-peer', 'Client/server', 'Bluetooth PAN', 'Ad hoc Wi-Fi'], 'Client/server', 'Central servers manage logins, permissions and backups for many users.'),
   ch('c', 'A1c', 'A call centre wants cheap, identical desks with no data stored on them.', ['Thin client', 'Peer-to-peer', 'Mesh', 'PAN'], 'Thin client', 'The server does the processing and storage; the desk devices are cheap and hold no data.'),
   ch('d', 'A1d', 'Software that lets one physical server run several virtual machines is a…', ['Router', 'Hypervisor', 'Switch', 'Firewall'], 'Hypervisor', 'The hypervisor creates and runs the virtual machines.'),
   ch('e', 'A1d', 'Staff using their own phones and laptops on the company network is called…', ['SDN', 'SaaS', 'BYOD', 'NAT'], 'BYOD', 'Bring your own device: flexible, but it brings security and support challenges.')]}
 ]
},
{
 id: 'q2', title: 'Quiz 2: OSI, TCP/IP, protocols and ports', short: '2 OSI & ports', guided: true,
 intro: 'Layers, protocols and port numbers come up in every networking job. Aim for full marks, then try again tomorrow to make it stick.',
 questions: [
  {id: 'q2a', title: 'The OSI layers', scenario: 'The OSI model has seven layers.', parts: [
   {id: 'a', marks: 3, type: 'order', section: 'A3', prompt: 'Put the OSI layers in order from layer 7 (top) to layer 1 (bottom).', hint: 'All People Seem To Need Data Processing (7 down to 1).', steps: [{id: 'app', text: 'Application'}, {id: 'pre', text: 'Presentation'}, {id: 'ses', text: 'Session'}, {id: 'tra', text: 'Transport'}, {id: 'net', text: 'Network'}, {id: 'dat', text: 'Data link'}, {id: 'phy', text: 'Physical'}], base: ['app', 'pre', 'ses', 'tra', 'net', 'dat', 'phy']},
   {id: 'b', marks: 5, type: 'fields', section: 'A3', prompt: 'At which OSI layer does each work?', grid: 2, fields: [
    {id: 'sw', label: 'A switch', options: ['Physical', 'Data link', 'Network', 'Transport', 'Application'], accept: ['Data link']},
    {id: 'rt', label: 'A router', options: ['Physical', 'Data link', 'Network', 'Transport', 'Application'], accept: ['Network']},
    {id: 'cab', label: 'A copper cable', options: ['Physical', 'Data link', 'Network', 'Transport', 'Application'], accept: ['Physical']},
    {id: 'tcp', label: 'TCP', options: ['Physical', 'Data link', 'Network', 'Transport', 'Application'], accept: ['Transport']},
    {id: 'http', label: 'HTTP', options: ['Physical', 'Data link', 'Network', 'Transport', 'Application'], accept: ['Application']}]},
   {id: 'c', marks: 3, type: 'fields', section: 'A3', prompt: 'What is the unit of data (PDU) called at each layer?', grid: 3, fields: [
    {id: 't', label: 'Transport', options: ['Bits', 'Frame', 'Packet', 'Segment'], accept: ['Segment']},
    {id: 'n', label: 'Network', options: ['Bits', 'Frame', 'Packet', 'Segment'], accept: ['Packet']},
    {id: 'd', label: 'Data link', options: ['Bits', 'Frame', 'Packet', 'Segment'], accept: ['Frame']}]}]},
  {id: 'q2b', title: 'Protocols and ports', scenario: 'Type the well-known port number.', parts: [
   {id: 'a', marks: 6, type: 'fields', section: 'A3', prompt: 'Which port does each service use by default?', grid: 3, fields: [
    {id: 'https', label: 'HTTPS', accept: ['443']}, {id: 'http', label: 'HTTP', accept: ['80']}, {id: 'dns', label: 'DNS', accept: ['53']},
    {id: 'ssh', label: 'SSH', accept: ['22']}, {id: 'smtp', label: 'SMTP', accept: ['25', '587']}, {id: 'rdp', label: 'RDP (remote desktop)', accept: ['3389']}]},
   ch('b', 'A3', 'Which transport protocol would a live video call normally use?', ['TCP, because every packet must arrive', 'UDP, because speed matters more than re-sending lost packets', 'FTP', 'ARP'], 'UDP, because speed matters more than re-sending lost packets', 'Waiting for re-sent packets would freeze the call, so UDP keeps it flowing.'),
   ch('c', 'A3', 'What is a socket?', ['A wall plug for a network cable', 'An IP address combined with a port number', 'A type of switch', 'A wireless channel'], 'An IP address combined with a port number', 'For example 192.168.1.10:443. It lets one device hold many conversations at once.'),
   ch('d', 'A3', 'Adding headers as data moves down the layers is called…', ['Encryption', 'Encapsulation', 'Compression', 'Routing'], 'Encapsulation', 'Each layer wraps the data in its own header; the receiver removes them in reverse.')]}
 ]
},
{
 id: 'q3', title: 'Quiz 3: IP addressing and subnetting', short: '3 IP addressing', guided: true,
 intro: 'Use the method from lesson B1b. Work on paper, then type your answers. Hosts per subnet = 2^(host bits) − 2.',
 questions: [
  {id: 'q3a', title: 'Working out a subnet', scenario: 'A PC has the address 192.168.5.130/26.', parts: [
   {id: 'a', marks: 5, type: 'fields', section: 'B1b', prompt: 'Work out the details of the PC’s network.', hint: '/26 means blocks of 64 in the last number: .0, .64, .128, .192. Which block contains 130?', grid: 2, fields: [
    {id: 'mask', label: 'Subnet mask (dotted)', accept: ['255.255.255.192']},
    {id: 'net', label: 'Network address', accept: ['192.168.5.128']},
    {id: 'first', label: 'First usable host', accept: ['192.168.5.129']},
    {id: 'last', label: 'Last usable host', accept: ['192.168.5.190']},
    {id: 'bc', label: 'Broadcast address', accept: ['192.168.5.191']}]},
   {id: 'b', marks: 3, type: 'fields', section: 'B1b', prompt: 'How many usable hosts are there in each network?', grid: 3, fields: [
    {id: 'p27', label: '/27', accept: ['30']}, {id: 'p28', label: '255.255.255.240', accept: ['14']}, {id: 'p30', label: '/30', accept: ['2']}]}]},
  {id: 'q3b', title: 'Valid and private addresses', scenario: 'Decide whether each address can be used as stated.', parts: [
   ch('a', 'B1b', 'Can 10.0.0.255/24 be given to a PC?', ['Yes', 'No: it is the broadcast address of 10.0.0.0/24'], 'No: it is the broadcast address of 10.0.0.0/24', 'With /24 the last address of the network (.255) is reserved for broadcasts.'),
   ch('b', 'B1b', 'Which of these is a private address?', ['172.20.1.1', '172.32.1.1', '192.169.1.1', '8.8.8.8'], '172.20.1.1', 'The private block 172.16.0.0/12 runs from 172.16.0.0 to 172.31.255.255.'),
   ch('c', 'B1b', 'A PC is 192.168.40.25/24. Which default gateway is valid?', ['192.168.41.1', '192.168.40.1', '192.168.40.255', '10.0.0.1'], '192.168.40.1', 'The gateway must be a usable address in the PC’s own network, 192.168.40.0/24.'),
   ch('d', 'A4', 'A laptop shows 169.254.8.17. What does this tell you?', ['It has a public address', 'It could not get an address from DHCP', 'It is using IPv6', 'It is the default gateway'], 'It could not get an address from DHCP', 'Addresses starting 169.254 are self-assigned when no DHCP server answers.'),
   {id: 'e', marks: 1, type: 'fields', section: 'B1b', prompt: 'Shorten this IPv6 address as far as possible: 2001:0db8:0000:0000:0000:0000:0000:0001', hint: 'Drop leading zeros in each group, then replace one run of zero groups with ::', fields: [{id: 'v6', label: 'Shortened address', accept: ['2001:db8::1']}]}]}
 ]
},
{
 id: 'q4', title: 'Quiz 4: Devices, media and services', short: '4 Devices & services', guided: true,
 intro: 'Hardware, cabling and the services that make a network useful.',
 questions: [
  {id: 'q4a', title: 'Devices and media', scenario: 'Choose the best answer.', parts: [
   ch('a', 'A2a', 'Which device connects different networks and chooses the best path for packets?', ['Switch', 'Router', 'Access point', 'Hub'], 'Router', 'Routers work with IP addresses and routing tables at layer 3.'),
   ch('b', 'A2a', 'Which device learns MAC addresses and forwards frames within a LAN?', ['Router', 'Switch', 'Modem', 'Firewall'], 'Switch', 'A switch builds a MAC address table and sends each frame only to the right port.'),
   ch('c', 'A2a', 'Two buildings are 400 m apart. Which cable should link them?', ['Cat6 UTP', 'Fibre optic', 'Coaxial', 'USB'], 'Fibre optic', 'Copper Ethernet only reaches 100 m; fibre reaches kilometres and is immune to interference.'),
   ch('d', 'A2a', 'Which feature lets a switch power IP phones and access points through the network cable?', ['VLAN', 'PoE', 'NAT', 'SSID'], 'PoE', 'Power over Ethernet sends power down the same cable as the data.'),
   ch('e', 'A2b', 'Which tool shows every router a packet passes through?', ['ping', 'tracert / traceroute', 'ipconfig', 'nslookup'], 'tracert / traceroute', 'It lists each hop, which helps find where a delay or break is.')]},
  {id: 'q4b', title: 'Services', scenario: 'Which service does the job?', parts: [
   {id: 'a', marks: 5, type: 'fields', section: 'A4', prompt: 'Match each job to the service.', grid: 2, fields: [
    {id: 'a1', label: 'Gives devices an IP address automatically', options: ['DNS', 'DHCP', 'NAT', 'SMTP', 'Directory service'], accept: ['DHCP']},
    {id: 'a2', label: 'Turns a name like intranet.local into an IP address', options: ['DNS', 'DHCP', 'NAT', 'SMTP', 'Directory service'], accept: ['DNS']},
    {id: 'a3', label: 'Lets many private addresses share one public address', options: ['DNS', 'DHCP', 'NAT', 'SMTP', 'Directory service'], accept: ['NAT']},
    {id: 'a4', label: 'Sends email between servers', options: ['DNS', 'DHCP', 'NAT', 'SMTP', 'Directory service'], accept: ['SMTP']},
    {id: 'a5', label: 'Central database of users and groups for logins', options: ['DNS', 'DHCP', 'NAT', 'SMTP', 'Directory service'], accept: ['Directory service']}]},
   {id: 'b', marks: 3, type: 'order', section: 'A4', prompt: 'Put the four DHCP messages in order.', steps: [{id: 'd', text: 'Discover'}, {id: 'o', text: 'Offer'}, {id: 'r', text: 'Request'}, {id: 'a', text: 'Acknowledge'}], base: ['d', 'o', 'r', 'a']}]}
 ]
},
{
 id: 'q5', title: 'Quiz 5: Design, configuration and troubleshooting', short: '5 Build & fix', guided: true,
 intro: 'The practical side of Assignment 2: design aims, Cisco commands, Linux permissions and fixing faults.',
 questions: [
  {id: 'q5a', title: 'Design aims', scenario: 'Which design aim is each client describing?', parts: [
   ch('a', 'B1a', '“We expect to double our staff in two years.”', ['Scalability', 'Redundancy', 'Affordability', 'Manageability'], 'Scalability', 'The network must grow without being rebuilt.'),
   ch('b', 'B1a', '“If one switch fails, the office must keep working.”', ['Scalability', 'Redundancy', 'Performance', 'Adaptability'], 'Redundancy', 'Duplicate devices or links remove the single point of failure.'),
   ch('c', 'B1b', 'Why put guest Wi-Fi devices in their own VLAN?', ['To make them faster', 'To keep them separate from staff systems for security', 'To give them public IP addresses', 'Because Wi-Fi cannot use VLANs'], 'To keep them separate from staff systems for security', 'VLANs isolate groups of devices; traffic between them must pass through a router where rules apply.')]},
  {id: 'q5b', title: 'Commands', scenario: 'Type the command.', parts: [
   {id: 'a', marks: 4, type: 'fields', section: 'C1', prompt: 'Cisco IOS commands', hint: 'Full commands or common short forms are accepted.', grid: 2, fields: [
    {id: 'en', label: 'Move from user EXEC to privileged EXEC', accept: ['enable', 'en']},
    {id: 'ns', label: 'Turn on an interface', accept: ['no shutdown', 'no shut']},
    {id: 'save', label: 'Save the configuration so it survives a restart', accept: ['copy running-config startup-config', 'copy run start', 'write memory', 'wr', 'write']},
    {id: 'sib', label: 'List every interface with its IP address and status', accept: ['show ip interface brief', 'sh ip int br', 'show ip int brief', 'sh ip int brief']}]},
   {id: 'b', marks: 2, type: 'fields', section: 'B3', prompt: 'Linux permission numbers (chmod)', grid: 2, fields: [
    {id: 'p1', label: 'Owner rwx, group r-x, others none', accept: ['750']},
    {id: 'p2', label: 'Owner rw-, group r--, others none', accept: ['640']}]}]},
  {id: 'q5c', title: 'Troubleshooting', scenario: 'Fix faults methodically.', parts: [
   {id: 'a', marks: 3, type: 'order', section: 'C2', prompt: 'Put the troubleshooting steps in order.', steps: [{id: 'id', text: 'Identify the problem'}, {id: 'th', text: 'Form a theory of the likely cause'}, {id: 'te', text: 'Test the theory'}, {id: 'fx', text: 'Plan and apply the fix'}, {id: 've', text: 'Verify it works'}, {id: 'do', text: 'Document the fault and fix'}], base: ['id', 'th', 'te', 'fx', 've', 'do']},
   ch('b', 'C2', 'A PC can reach devices in its own LAN but not in any other network. What is the most likely cause?', ['The cable is unplugged', 'The default gateway is wrong or missing', 'The monitor is off', 'DNS is working'], 'The default gateway is wrong or missing', 'Traffic for other networks goes to the default gateway; if it is wrong, only local traffic works.'),
   ch('c', 'C2', 'You configured a router interface but the link stays down. What did you most likely forget?', ['hostname', 'no shutdown', 'enable secret', 'banner motd'], 'no shutdown', 'Router interfaces are off until you use no shutdown.')]}
 ]
}
];
