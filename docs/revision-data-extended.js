'use strict';
// Test 4: original extended-response practice (6–12 marks), marked by level like the exam's long questions.
const FOR_AGAINST = [
 {label: 'Points for / strengths', hint: 'e.g. cheaper to run because…'},
 {label: 'Points against / limits', hint: 'e.g. but it depends on…'},
 {label: 'My judgement', hint: 'Overall… because the most important factor is…'}
];
window.REVISION_TESTS.push({
 id: 't4', title: 'Revision test 4 — extended answers', short: 'Test 4 (long answers)',
 intro: 'The 6–12 mark questions carry the most marks in the exam. They are marked by level: the examiner judges the quality of the whole answer, not one mark per point. Plan first, write in developed paragraphs linked to the scenario, then mark your answer against the levels.',
 guide: [
  {term: 'Discuss', text: 'Explore the issue from different angles: how things work, benefits, drawbacks and what they depend on. A conclusion is not always required, but it helps.'},
  {term: 'Evaluate', text: 'Weigh up strengths and weaknesses against the scenario, then give a supported judgement: which option, and why that reason outweighs the others.'},
  {term: 'Analyse', text: 'Break the situation into its parts, explain how each part affects the result, and show how the parts connect.'},
  {term: 'Develop a point', text: 'Point → explain how or why → apply it to this scenario → link it back to the question. One developed point is worth more than three listed ones.'},
  {term: 'Timing', text: 'About 1¼ minutes per mark: roughly 8 minutes for 6 marks and 15 minutes for 12 marks, including planning.'}
 ],
 guided: true,
 questions: [
 {
  id: 't4q1', title: 'Cloud laptops for Oakfield School',
  scenario: 'Oakfield School is replacing the 30 desktop PCs in its computer room. The IT manager wants low-cost cloud laptops: they have 4 GB RAM and 64 GB of storage, run a browser-based operating system, and save all work to online storage. Students use office software, coding websites and some video editing. The school’s internet connection is shared by 900 students.',
  parts: [
   {id:'a', marks:2, type:'text', section:'A1', prompt:'Improve this weak point. A student wrote: “Cloud laptops are cheaper.” Rewrite it as one developed point applied to Oakfield.', hint:'Say why they are cheaper, and what that means for Oakfield.', starter:'Cloud laptops cost less because… so Oakfield could…', criteria:['Explains why: basic, low-spec hardware and little local storage, and free or lower-cost software/OS licences (less maintenance too)','Applies it: e.g. the saving on 30 machines could fund more devices or a faster internet connection']},
   {id:'b', marks:12, type:'essay', section:'A1', prompt:'Evaluate whether Oakfield should replace the desktop PCs with cloud laptops.', structure:'Introduction (one sentence) → strengths applied to Oakfield → limitations applied to Oakfield → what the decision depends on → justified recommendation.', plan: FOR_AGAINST, criteria:['Lower purchase and running costs; cheaper to replace or repair','Central management: updates and settings pushed from one place, fewer local faults for the technician','Work saved online, so students can reach it at home and do not lose it if a laptop breaks (automatic backup)','Portable and quick to start up, so they can be used in any classroom','Depends on the internet: 900 students share the connection, so it may be slow or fail, stopping lessons','4 GB RAM and a low-power CPU struggle with video editing; browser-based OS may not run specialist or offline software','Security and privacy: student data stored by an outside provider (data protection, account security)','Implementation: staff training, moving existing files, testing that coding websites work','Possible compromise: cloud laptops for most tasks, plus a few high-spec PCs for video editing, or an upgraded internet connection','A clear recommendation that weighs the most important factors for Oakfield']}
  ]
 },
 {
  id: 't4q2', title: 'Three-site health centre',
  scenario: 'Brookside Health runs three clinics. Each clinic keeps its own patient records on a local server. Managers want one shared system, so that any clinic can open any patient’s record.',
  parts: [
   {id:'a', marks:9, type:'essay', section:'A3', prompt:'Discuss the impact on Brookside and its patients of storing and using patient data across multiple computer systems.', structure:'Use the five impact headings from the specification — access, cost, implementation, productivity, security — and apply each one to Brookside.', plan:[{label:'Access and productivity', hint:'Who can reach what, from where, and how much faster?'},{label:'Cost and implementation', hint:'What must be bought, moved, tested and taught?'},{label:'Security and risks', hint:'What could go wrong with sensitive health data?'}], criteria:['Access: a patient can be seen at any clinic with the full history available, e.g. allergies and medicines','Productivity: less time phoning other clinics or re-entering data; fewer duplicate records and errors','Records must stay synchronised; a network failure could stop a clinic reaching the data (needs a backup link or local copy)','Cost: new servers or cloud hosting, network links, licences and support','Implementation: data migration and merging duplicate patients, testing, staff training, possible downtime during the switch','Security: health data is special-category personal data (data protection law), so it needs encryption, role-based access and audit logs','More users and sites means more ways in for attackers; a breach would affect all three clinics','A balanced conclusion about whether the benefits outweigh the risks for Brookside']}
  ]
 },
 {
  id: 't4q3', title: 'Pixel Harbour animation studio',
  scenario: 'Pixel Harbour is a small animation studio with 12 artists. Rendering a finished scene takes many hours. The studio can either buy each artist a powerful 16-core workstation, or keep the artists’ current computers and buy a render cluster of 20 networked computers that shares the rendering work.',
  parts: [
   {id:'a', marks:2, type:'text', section:'B1', prompt:'Improve this weak point. A student wrote: “A cluster is faster.” Rewrite it as one developed point applied to Pixel Harbour.', hint:'Why is a cluster faster for this particular job?', starter:'A render cluster would finish scenes faster because…', criteria:['Explains why: rendering can be split into independent frames, which the 20 nodes process in parallel at the same time','Applies it: scenes render overnight rather than over days, so artists get feedback sooner and meet deadlines']},
   {id:'b', marks:12, type:'essay', section:'B2', prompt:'Evaluate the two options for Pixel Harbour.', structure:'Explain how each option speeds up rendering → strengths and limits of each for this studio → costs and practical issues → recommendation.', plan: FOR_AGAINST, criteria:['Multi-core workstations: many cores render one artist’s scene in parallel on their own machine, with no network needed','Each artist also gets a faster machine for everyday modelling and previews (better productivity)','But cores share one memory/bus, and each machine sits idle when its artist is not rendering','Cluster: the render is split across 20 nodes, and frames are independent, so it scales very well','Cluster resources are shared and can run all night; more nodes can be added later','Cluster issues: network speed to send scene files, needs render-management software, power, cooling and space, a single point of management','Reliability: if one cluster node fails the others continue; if a workstation fails, that artist is stuck','Cost comparison: 12 high-end workstations vs 20 cluster nodes plus networking and running costs','Compromise options, e.g. a smaller cluster plus upgraded RAM/GPUs, or cloud rendering for peaks','A justified recommendation based on the studio’s workload']}
  ]
 },
 {
  id: 't4q4', title: 'Open source for a charity',
  scenario: 'A local food-bank charity has 8 donated office computers and almost no budget. A volunteer suggests installing a free open-source operating system and open-source office software instead of buying licences.',
  parts: [
   {id:'a', marks:6, type:'essay', section:'A2', prompt:'Discuss the use of open-source software by the charity.', structure:'What open source means → benefits for this charity → drawbacks for this charity → what it depends on.', plan: FOR_AGAINST, criteria:['Open source: the source code is available to inspect, change and share under its licence, usually free','No licence fees, so the tight budget goes on the charity’s real work; runs well on older donated computers','Community updates and security fixes; code can be checked for back doors','Volunteers may be unfamiliar with it, so training is needed; some staff may resist change','Compatibility: files from partners using proprietary software may not look the same, and some specialist software/drivers may not exist','Support comes from forums and volunteers rather than a paid helpdesk, which is a risk if the one volunteer who knows it leaves']}
  ]
 },
 {
  id: 't4q5', title: 'Homes Online photo gallery',
  scenario: 'Homes Online is an estate agency website. Each property listing has up to 30 photos. Many buyers browse on phones using mobile data, but sellers want their homes to look sharp and attractive.',
  parts: [
   {id:'a', marks:9, type:'essay', section:'C3', prompt:'Analyse how image resolution, colour depth and compression affect the photos on Homes Online.', structure:'Take each factor in turn: what it is → its effect on quality → its effect on file size and loading → the right choice for this website. Then show how the factors interact.', plan:[{label:'Resolution', hint:'Pixels, detail, file size, phone vs desktop screens'},{label:'Colour depth', hint:'Bits per pixel, number of colours, banding'},{label:'Compression', hint:'Lossy vs lossless, artefacts, loading speed'}], criteria:['Resolution: more pixels give sharper detail and allow zooming into rooms, but file size grows with width × height','Phones do not need huge images: serve smaller versions to phones and larger ones on request (thumbnails vs full view)','Colour depth: 24-bit gives about 16.7 million colours for realistic photos; lower depth causes banding in skies and walls','File size = width × height × colour depth, so each factor multiplies the others','Lossy compression (JPEG) greatly reduces size for faster loading on mobile data, with little visible loss at sensible settings','Too much compression causes blocky artefacts that make homes look worse, which sellers will not accept','Keep lossless or high-quality originals so new sizes can be made later without extra loss','Links to the business: fast pages keep buyers browsing; sharp photos keep sellers happy, so a balance is needed']}
  ]
 },
 {
  id: 't4q6', title: 'Hilltop Farm sensors',
  scenario: 'Hilltop Farm is putting 40 wireless soil sensors across its fields. Every 10 minutes each sensor sends a small reading to a base station in the farmhouse, which uploads the data to a cloud dashboard. The wireless signal is weak at the far edges of the fields, and the sensors run on batteries.',
  parts: [
   {id:'a', marks:12, type:'essay', section:'E1', prompt:'Evaluate how the farm’s data should be transmitted, and how errors should be detected and dealt with, from the sensors to the dashboard.', structure:'Channel and connection types → packets and protocols → detecting errors → correcting errors (ARQ vs FEC) → security → recommendation.', plan: FOR_AGAINST, criteria:['Sensors mainly send data to the base (simplex or half-duplex); half-duplex lets the base acknowledge or change settings','Serial wireless transmission of small packets containing sensor ID (source), base address (destination), payload, sequence number and checksum','Sequence numbers or timestamps show missing readings; the base can spot a sensor that has stopped reporting','Weak signal at the edges makes corrupted packets more likely: a checksum or CRC detects them','ARQ (acknowledge and resend) is simple and works well because readings are small and a short delay does not matter','But every resend and acknowledgement uses battery power, and the far sensors may need many retries','FEC adds redundant data so some errors are fixed without resending; this suits weak links but makes every packet larger','Options such as relay/mesh nodes or a better aerial reduce errors at the source','Security: readings encrypted and devices authenticated so false data cannot be injected; secure upload (HTTPS) to the cloud','A justified recommendation, e.g. checksum + ARQ with limited retries, plus relays for the far fields']}
  ]
 }
 ]
});
