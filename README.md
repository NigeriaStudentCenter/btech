# Unit 2: Azure tutor and private device workbook

Prepared 28 September 2026. This package supersedes the school-sign-in/cloud-workbook starter for the agreed anonymous design. It is not deployed. Local code tests are provided; live Azure and visual browser acceptance tests remain.

## What works without Azure

Publish the contents of site/ to GitHub Pages, keeping index.html, learning.html, workbook.js and config.js together. The illustrated lessons link to 16 workbook sections. Answers autosave in localStorage on that browser profile and website origin. Download all my work exports JSON; Continue from a backup restores it on another device. Students can print the current section. There is no workbook API, identity provider, analytics script or student database. Chat history stays only in page memory, clears on section change/reload, and is sent with a question to let the tutor follow the conversation. The application does not persist chat on its server.

The same link can go in any school's Teams. Students do not join your tenant. Each browser profile has one local workbook, not one per child: on shared profiles students must download then clear their work. Incognito, cleared browser storage or device resets can lose work. Always download a backup before leaving a school device. Use one workbook tab at a time. A changed site hostname/path deployment may affect access to prior browser storage; downloaded backups can be restored. JSON files contain students' written text; remind them not to type personal details. These files are backups, not executable HTML.

## Azure setup: IT checklist

No Azure access is required to inspect this package. To deploy it, your administrator needs:

- An Azure subscription/resource group and an Azure Functions app using Node.js 22, runtime v4.
- An Azure OpenAI resource with a compatible chat-completions model deployment, such as an available GPT-4.1-mini deployment. Confirm model availability and quota in your selected region. Set the *deployment name*, not a guessed model name.
- A system-assigned managed identity on the Function app. Grant it Cognitive Services OpenAI User on the model resource. No API key belongs in the HTML or GitHub.
- The course origin, for example https://YOUR-ORGANISATION.github.io (no repository path), and the Function URL.

Configure Function app settings:

```
FUNCTIONS_WORKER_RUNTIME=node
TUTOR_ENABLED=false
AZURE_OPENAI_ENDPOINT=https://YOUR-RESOURCE.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=YOUR-DEPLOYMENT-NAME
ALLOWED_ORIGINS=https://YOUR-ORGANISATION.github.io
```

Keep the Function host's required storage configuration provisioned by Azure; it is infrastructure, not a workbook database. Configure HTTPS and platform CORS for the same exact course origin. Do not use wildcard CORS. The code also checks origin, but an origin header is not authentication and can be forged outside a browser.

From api/, install dependencies with npm install, run npm test, and deploy using Azure Functions Core Tools (`func azure functionapp publish YOUR-FUNCTION-NAME`) or your approved Azure CI workflow. Commit the generated package lock in your maintained repository. Authenticate through your normal IT-controlled Azure session; do not paste credentials into chat.

Set site/config.js TUTOR_API_URL to https://YOUR-FUNCTION.azurewebsites.net/api/chat (or your Azure API Management gateway URL). Publish site/ on GitHub Pages. Leave TUTOR_ENABLED=false until gateway cost controls below are configured; then enable it for supervised testing.

## Anonymous access and spending controls

No student login means the tutor endpoint is publicly callable. CORS and a hidden URL cannot make it school-only. Before a public pilot, place Azure API Management or an equivalent Azure gateway in front of the Function, restrict direct backend ingress to that gateway, and configure shared request/token quotas and rate limits plus Azure model quota. A global quota does not require student identifiers, but students share the limit. Budget alerts are notifications, not hard spending stops. Keep a server-side kill switch (TUTOR_ENABLED). Do not embed a Function key, gateway secret or model key in public HTML.

This package does not provision the gateway or a rate-limit service. Configure and verify those in your Azure environment before inviting students. If strict school-only access is later required, it needs an access mechanism; an anonymous public link alone cannot prove school membership.

## Privacy and Azure-only operation

The backend accepts only section, mode, question and bounded recent chat for model context. It does not send workbook answers automatically, request a name/email, create student profiles or write transcripts to a database. It does not log message content. All model calls target an allowlisted Azure resource hostname using managed identity. There is no direct OpenAI API fallback or external search/retrieval.

Azure, your gateway and GitHub may still process technical metadata. Review platform request logging, retention and Azure model abuse-monitoring settings. store:false is not a guarantee that Azure retains no service data. Do not enable request/response-body tracing. No claim is made that Azure processing is physically inside your own network: regional/global/data-zone deployment choices determine processing geography. Have IT select the required deployment geography and, if needed, private endpoints between backend and model. GitHub serves only original course material; do not publish source PDFs or teacher answer keys.

## Tutor teaching behaviour

The tutor uses approved section explanations and examples, not teacher keys. It explains vocabulary in plain English for age 12–15, gives hints, asks diagnostic questions and creates new practice. The system prompt asks it not to complete assigned answers. This is a behavioural safeguard, not a guarantee: review representative responses before the student pilot. The model is not an official Pearson marker.

## Acceptance checks

1. Open a lesson, follow its workbook link, type answers, refresh and confirm restoration.
2. Download all work; restore in another browser profile; compare several sections.
3. Clear the device and check answers are gone. Test browser storage blocked: the message must direct students to download.
4. Ask Azure tutor a question in each topic A–F; try a follow-up. Confirm requests go only to your Azure endpoint and the browser sends no workbook automatically.
5. Ask for a completed assigned answer and to ignore tutor rules. Review scaffolding. Check unknown facts are handled honestly.
6. Disable tutor or exhaust quota: workbook remains usable and the tutor displays a clear failure.
7. Inspect Azure monitoring with IT: no application transcript persistence or body tracing. Verify gateway quotas and blocked direct backend access.

Local checks: `cd api && npm test`. These use Node's built-in test runner; no Azure login or model call is involved. There has been no live Azure test or visual browser QA in this environment.

Official deployment references:
- https://learn.microsoft.com/en-us/azure/foundry/openai/latest
- https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/managed-identity

## Four-part student pack

Share site/start.html as the Teams link. It links to brief.html (original formative course brief, with 16 matching tasks), learning.html (illustrated teaching), index.html (workbook and tutor), and revision.html (scan-informed original revision practice). The raw OCR transcript remains a teacher reference: it contains OCR limitations and reproduced source text and is not included in the public GitHub site. This practice brief does not constitute an official internally assessed Pearson assignment.
