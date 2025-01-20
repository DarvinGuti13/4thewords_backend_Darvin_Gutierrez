from fastapi import FastAPI
from .database import Base, engine
from .routers import leyendas
from app.routers import leyendas
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import uvicorn

# Cargar las variables del archivo .env
load_dotenv()

# Crear la aplicación FastAPI
app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir solicitudes desde el frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear las tablas en la base de datos (si no existen)
Base.metadata.create_all(bind=engine)

# Incluir los routers de la API
app.include_router(leyendas.router)

# Verifica que el backend esté levantado
@app.get("/")
def read_root():
    return {"message": "¡Backend levantado correctamente en el puerto configurado!"}

# Configuración principal para levantar el servidor
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("app.main:app", host="127.0.0.1", port=port, reload=True)

