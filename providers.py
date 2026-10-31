from dataclasses import asdict, dataclass

@dataclass(frozen=True)
class Provider:
    id: str
    label: str
    connection: str
    implemented: bool = False

_PROVIDERS = [
    Provider("openai", "OpenAI", "official_api"),
    Provider("anthropic", "Anthropic Claude", "official_api"),
    Provider("google", "Google Gemini", "official_api"),
    Provider("deepseek", "DeepSeek", "official_api"),
    Provider("moonshot", "Kimi", "official_api"),
    Provider("qwen", "Qwen", "official_api_or_compatible"),
    Provider("zai", "Z.AI / GLM", "official_api"),
    Provider("openrouter", "OpenRouter", "openai_compatible"),
    Provider("groq", "Groq", "openai_compatible"),
    Provider("together", "Together AI", "openai_compatible"),
    Provider("ollama", "Ollama (local)", "local_http"),
    Provider("custom", "Custom OpenAI-compatible endpoint", "openai_compatible"),
]

def list_providers():
    return [asdict(provider) for provider in _PROVIDERS]
