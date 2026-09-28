# Live deployment (28 Sep 2026)

- Course site: GitHub Pages from `docs/` → https://nigeriastudentcenter.github.io/btech/start.html (the Teams link)
- Gateway: Azure API Management `btech-tutor-apim` (Consumption, rg `btech-tutor-rg`, Sweden Central)
  - API `tutor` → POST/OPTIONS `/tutor/chat`, product `btech-course`: rate-limit 60 calls/min, quota 6,000 calls/day (preflights count too)
  - Public counter key (subscription `btech-course-public`) is in `docs/config.js` as `?k=` — not a secret; regenerate in APIM + update config.js if abused
  - Adds the Function key from named value `btech-func-key` (secret)
- Function: `btech-tutor-api` (Flex Consumption, Node 22, authLevel `function` so direct calls without the gateway's key get 401; platform CORS = the Pages origin only; max 40 instances)
  - Settings: `TUTOR_ENABLED` (kill switch), `AZURE_OPENAI_ENDPOINT=https://ai-tutor-agent.services.ai.azure.com`, `AZURE_OPENAI_DEPLOYMENT=btech-tutor-gpt41mini`, `ALLOWED_ORIGINS=https://nigeriastudentcenter.github.io`
  - System-assigned identity has Cognitive Services OpenAI User on `AI-Tutor-Agent` (rg `AI`)
- Model: `btech-tutor-gpt41mini` (gpt-4.1-mini 2025-04-14, DataZoneStandard = EU data zone, 20K tokens/min hard cap)

Deploy API: `cd api && npm test && func azure functionapp publish btech-tutor-api --javascript`
Turn tutor off: `az functionapp config appsettings set -n btech-tutor-api -g btech-tutor-rg --settings TUTOR_ENABLED=false`

## Learning page "Go deeper" content
`docs/learning.html` has a "Go deeper" block in each of the 16 sections (original text and SVG diagrams).
Edit the content in `tools/deeper/section_*.py`, then run `python3 tools/build_learning.py` — it replaces the
blocks between `<!-- deeper:ID -->` markers, so it is safe to run repeatedly.
