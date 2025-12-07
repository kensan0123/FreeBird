from pydantic import BaseModel
from typing import Literal


class PublishRequest(BaseModel):
    slug: str


class PublishResponse(BaseModel):
    status: Literal["published!", "failed"]
    slug: str
