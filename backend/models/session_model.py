import uuid
from datetime import datetime
from sqlalchemy import Column, String, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class WritingSessionModel(Base):
    """WritingSessionのテーブルモデル"""

    __tablename__ = "writing_session"
    session_id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),  # refactor: invert to server_default
    )
    topic = Column(
        String(50),
        nullable=False,
    )
    target_audience = Column(
        String(50),
        nullable=False,
    )
    outline = Column(
        JSON,
        default=list,
    )
    content = Column(
        JSON,
        default=dict,
    )
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

    def __repr__(self):
        return f"<WritingSession(session_id={self.session_id}, topic={self.topic})>)"
