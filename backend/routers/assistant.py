from fastapi import APIRouter
import uuid
from datetime import datetime
from backend.schemas.assistant_schemas import WritingInfo, WritingSession, OutlineSection

router = APIRouter(prefix="/create", tags=["create"])


@router.post("/")
def create_session(writing_info: WritingInfo) -> WritingSession:
    writing_session: WritingSession = WritingSession(
        session_id=str(uuid.uuid4()),
        topic=writing_info.topic,
        target_audience=writing_info.target_audience,
        outline=[],
        content={},
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    return writing_session
