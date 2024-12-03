"""Main application."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routing import app_router
from database import engine
import models

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar los routers
app.include_router(app_router, tags=["Main"])

# Configuración del servidor para ejecutar localmente
if __name__ == "__main__":
    import uvicorn

    models.Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host="0.0.0.0", port=8001)
