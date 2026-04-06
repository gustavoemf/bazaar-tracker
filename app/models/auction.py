from sqlalchemy import Column, ForeignKey, Integer, String

from app.db.base import Base


class Auction(Base):
    __tablename__ = "auctions"

    id = Column(Integer, primary_key=True, index=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    status = Column(String, nullable=False, default="active")
    current_bid = Column(Integer, nullable=True)
    final_price = Column(Integer, nullable=True)