from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    server = Column(String, nullable=False, index=True)
    vocation = Column(String, nullable=True)