import os

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
KENN_ZENN_URL = os.getenv("KENN_ZENN_URL", "http://host.docker.internal:9000")
openai_api_key = os.getenv("OPENAI_API_KEY")
