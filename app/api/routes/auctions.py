from fastapi import APIRouter

router = APIRouter(prefix="/auctions", tags=["auctions"])


@router.get("/")
def list_auctions():
    return {
        "auctions": [],
        "message": "Lista de auctions ainda será implementada"
    }