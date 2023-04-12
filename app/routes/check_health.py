from fastapi import APIRouter

router = APIRouter(prefix='/server', tags=['Server'])


@router.get("/health-check")
def healt_check():
    return {"status": "The server is up and running flawless"}
