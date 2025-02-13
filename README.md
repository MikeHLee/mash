# MASH (Master Shell)

A unified command-line interface for interacting with various Language Model providers.

## Installation

```bash
pip install mash
```

## Configuration

Before using MASH, you need to set up your API keys and configurations:

1. Create a `models/secrets.py` file with your API keys:
```python
OPENAI_API_KEY = "your-openai-key"
ANTHROPIC_API_KEY = "your-anthropic-key"
```

2. Configurations for each model are stored in their respective config files under `models/<provider>/configs.py`

## Usage

```bash
# Using GPT-4 (default)
mash ask "What is the meaning of life?"

# Using a specific model
mash ask "What is the meaning of life?" --model=claude
mash ask "What is the meaning of life?" --model=ollama

# Get help
mash --help
```

## Supported Models

- OpenAI GPT-4 (default)
- Anthropic Claude
- Local Ollama models

## License

MIT License
