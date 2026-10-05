# Signal — Prompt Safety & Literacy

A compact, responsive learning app for prompt literacy, AI security, and responsible cybersecurity practice. The interface is plain HTML/CSS/JavaScript; the backend uses only Python's standard library. No model weights, bundled datasets, npm packages, or third-party Python dependencies are required.

## Run locally

Requires Python 3.10 or newer.

1. Open this project folder in VS Code.
2. Start the server: `python app.py`
3. Visit `http://127.0.0.1:8000`.
4. Stop the server with Ctrl+C.

### Open on another device on your private Wi-Fi/LAN

Run `run-on-lan.bat` on the host computer, or start the server with `python app.py --host 0.0.0.0 --port 8000`. The terminal prints a `http://<host-LAN-IP>:8000` address. Open that address on the other device while both devices are on the same trusted network. Keep the host computer and server running. If the device cannot connect, allow Python/app port 8000 through Windows Firewall on the **Private** network profile only. The normal `python app.py` command remains localhost-only.

LAN mode has no user accounts or authentication and is intended only for a trusted home/private network. Do not use public Wi-Fi or router port forwarding. Learner progress is kept separately in each browser and does not sync between devices.

The tutor works in mock/demo mode without credentials. To optionally connect an OpenAI-compatible chat-completions API, set `OPENAI_API_KEY` in the server process environment. Optionally set `OPENAI_BASE_URL` and `OPENAI_MODEL`. Never put API credentials in browser code, HTML, or a committed file. This is a learning/demo app, not a hardened production service. Before a public launch, add operational controls such as rate limiting and monitoring; do not enter personal or sensitive information, and do not configure a paid API key unless usage is controlled.

### Prepare a public demo URL on Render

The included `render.yaml` requests the service slug `signal-prompt-safety`, which would produce a URL like `https://signal-prompt-safety.onrender.com` if that name is available. Render requires a GitHub repository: push this project, sign in to Render, and create a Blueprint from that repository. The provider allocates the final URL after creation; no domain is purchased. Free web services can sleep when idle and may take time to wake. Public hosting is for a demo only; the tutor/progress does not provide accounts, and progress stays in each visitor's browser.

## Test

Run `python -m unittest discover -s tests -v`.

## Learning scope

- NIST AI RMF: Govern, Map, Measure, Manage concepts
- OWASP LLM security: prompt injection, indirect injection, RAG, tool boundaries, excessive agency
- NIST CSF 2.0: Govern, Identify, Protect, Detect, Respond, Recover
- MITRE ATT&CK: defensive threat analysis and detection mapping
- Cloud Security Alliance concepts: shared responsibility and IAM
- Bloom's Taxonomy: a progression from remembering to creating
- Prompt literacy: context-aware reflection, safe alternatives, and explicit reasoning
- Interview practice: searchable names from the 2026 Fortune 500 list plus original AI-security/cybersecurity practice scenarios for Fortune 500, Big Tech, and custom employers

Course progress is saved as per-lesson checklists; a pathway is counted complete only when all its lessons are checked. The overview tracks active calendar days, the current consecutive-day streak, and milestone achievements. Interview questions can be checked off as practiced. Progress is stored in browser local storage on that device/browser, not on the server; it does not automatically sync between devices. The searchable company names are a 2026 snapshot of the [Fortune 500 ranking](https://fortune.com/ranking/fortune500/2026/). Company interview content is original, illustrative practice material—not verified or verbatim interview questions—and the project is not affiliated with those companies. For employers outside the curated examples, prompts are adapted to the company name and AI/cybersecurity role themes, not claims about that employer's actual hiring process.

Lessons introduce direct and indirect prompt injection, safe prompt construction, tool authorization, defense-in-depth, and isolated sandbox testing. The project is educational and does not provide real-system safeguard-bypass instructions.

## Important limitations

The prompt analyzer is intentionally a small, transparent heuristic demonstration. It can miss risky requests and flag benign ones; it is not an authorization check, production guardrail, or substitute for human review. The optional model connection has a safety-oriented system prompt, but prompts and model outputs are not guaranteed safe. A production service needs independently enforced access control, validated tool calls, rate limits, abuse monitoring, privacy controls, and security review. Retrieved documents must be treated as untrusted data.

## Storage budget: 80 MB maximum

The application source and static assets are tiny and dependency-free; the supplied project files are expected to remain far below 1 MB. Keep the complete project folder under 80 MB by not committing virtual environments, caches, downloaded model weights, or build outputs. Check the folder size periodically in File Explorer. Python itself and any external hosted model are not bundled in this project; local model weights are deliberately not used.

External font loading is optional. If offline use is required, remove the Google Fonts links in `static/index.html` and use the system font fallbacks in `static/styles.css`.
