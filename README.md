# RoPilot

An extensible AI development agent for Roblox Studio.

RoPilot is designed around provider adapters instead of being tied to a handful of chatbot websites. It aims to support official model APIs, OpenAI-compatible endpoints, and local models through Ollama, with Roblox Studio connected through a local bridge and MCP.

> Status: early starter scaffold. This repository is not yet a complete AI Bridge replacement. Provider adapters and the Studio tool bridge need integration testing before everyday use.

## Goals

- Switch models without restarting a Studio session.
- Support multiple providers through a common interface.
- Support local models through Ollama.
- Keep provider credentials on the user's machine.
- Use explicit tool permissions and preview destructive edits.
- Keep the Roblox integration modular.

## Planned providers

| Provider | Connection |
|---|---|
| OpenAI | Official API |
| Anthropic Claude | Official API |
| Google Gemini | Official API |
| DeepSeek | Official API |
| Moonshot Kimi | Official API |
| Qwen | Official API / compatible endpoint |
| Z.AI / GLM | Official API |
| OpenRouter | OpenAI-compatible API |
| Groq | OpenAI-compatible API |
| Together AI | OpenAI-compatible API |
| Ollama | Local HTTP API |
| Any OpenAI-compatible endpoint | User-configured base URL |

Provider availability, model names, pricing, and rate limits are controlled by each provider and can change.

## Architecture

```text
RoPilot UI / browser extension
          |
          v
Local RoPilot bridge (127.0.0.1)
          |
          +---- Provider registry
          |        +---- Official API adapters
          |        +---- OpenAI-compatible adapter
          |        +---- Ollama adapter
          |
          +---- Agent loop / tool permissions
          |
          +---- Roblox Studio MCP connector (planned)
```

## Quick start (bridge scaffold)

Requires Python 3.11+.

```bash
cd bridge
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -e .
uvicorn ropilot_bridge.main:app --host 127.0.0.1 --port 8765
```

Open `http://127.0.0.1:8765/health`.

The current bridge exposes a health endpoint and a provider registry scaffold. It does not yet execute Roblox Studio actions.

## Configuration

Copy `.env.example` to `.env` and add only the API keys for providers you use. Never commit `.env`.

For local Ollama, start Ollama separately and configure its local endpoint in the future settings UI.

## Security model

- Bind the bridge to loopback (`127.0.0.1`) by default.
- Do not expose the bridge to the public internet.
- Keep API keys out of browser extension code and source control.
- Validate every tool request against an allowlist.
- Require confirmation for destructive or broad changes.
- Log tool names and outcomes, but never log secrets.

## Roadmap

- [x] Initial project structure
- [x] Provider interface and registry scaffold
- [x] Local bridge health endpoint
- [ ] OpenAI-compatible chat adapter
- [ ] Ollama adapter
- [ ] Anthropic and Gemini adapters
- [ ] Agent loop with bounded tool calls
- [ ] Roblox Studio MCP connector
- [ ] Script read/edit tools with diff preview
- [ ] Play-test and output inspection
- [ ] Browser extension UI
- [ ] Automated tests and signed releases

## License

MIT. See [LICENSE](LICENSE).
