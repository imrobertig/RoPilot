# Provider integration guide

Provider adapters should implement one common interface:

- `id`: stable provider identifier
- `list_models()`: return available model identifiers where supported
- `generate(messages, tools, settings)`: stream or return a normalized response
- Normalize tool calls into RoPilot's internal schema.
- Surface rate limits and provider errors without retry loops.
- Never silently switch to a different provider or model.

Prefer official APIs or documented OpenAI-compatible endpoints. Do not automate private website endpoints or attempt to bypass provider restrictions.
