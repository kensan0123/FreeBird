from pydantic import Field, field_validator
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    OPENAI_API_KEY: str = Field(pattern=r"^sk-.+")
    OPENAI_API_KEY_FILE: str | None = None
    ROOT_DIR: str
    ARTICLE_DIR: str = Field(default="./articles")
    GITHUB_USER: str
    GITHUB_PAT: str
    GITHUB_PAT_FILE: str | None = None

    @field_validator("OPENAI_API_KEY", mode="before")
    @classmethod
    def load_openai_key(cls, v, info):
        """環境変数またはファイルからOPENAI_API_KEYを読み込む"""
        if v and v.startswith("sk-"):
            return v
        file_path = info.data.get("OPENAI_API_KEY_FILE")
        if file_path and Path(file_path).exists():
            return Path(file_path).read_text().strip()
        return v

    @field_validator("GITHUB_PAT", mode="before")
    @classmethod
    def load_github_pat(cls, v, info):
        """環境変数またはファイルからGITHUB_PATを読み込む"""
        if v and v.startswith("ghp_"):
            return v
        file_path = info.data.get("GITHUB_PAT_FILE")
        if file_path and Path(file_path).exists():
            return Path(file_path).read_text().strip()
        return v
