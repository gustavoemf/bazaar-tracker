from app.db.base import Base
from app.db.session import engine

# Importa os models para que fiquem registrados no metadata
from app.models import Character, Auction  # noqa: F401


def init_db():
    Base.metadata.create_all(bind=engine)