from fastapi import APIRouter
import uuid
from datetime import datetime
from backend.schemas.assistant_schemas import (
    WritingInfo,
    WritingSession,
    SuggestionRequest,
    SuggestionResponse,
)
from agents.suggestion_agent import SuggestAgent
from backend.session.session_manager import SessionManager

router = APIRouter(prefix="/assist", tags=["assist"])


@router.post("/bigin")
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


@router.post("/suggest")
def writing_assist(suggest_request: SuggestionRequest) -> SuggestionResponse:
    session_manager: SessionManager = SessionManager()
    suggest_agent: SuggestAgent = SuggestAgent()

    writing_session: WritingSession = session_manager.get_session(
        session_id=suggest_request.session_id
    )

    response: SuggestionResponse = suggest_agent.generate_suggestion(
        writing_session=writing_session,
        current_section_id=suggest_request.current_section_id,
        current_content=suggest_request.current_content,
    )

    return response
