from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "Healthy",
        "service": "EV Fleet Data Platform",
        "version": "1.0.0",
    }