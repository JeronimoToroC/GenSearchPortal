"""Main routing."""

from fastapi import APIRouter

app_router = APIRouter()

@app_router.get("/", summary="Main route", tags=["Main"])
def main():
    """Main route."""
    return {"message": "Hello World"}
