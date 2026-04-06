from fastapi import APIRouter

router = APIRouter(prefix="/characters", tags=["characters"])


@router.get("/")
def list_characters():
    return {
        "characters": [],
        "message": "Lista de characters ainda sera implementada",
    }
