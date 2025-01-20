from sqlalchemy import Column, Integer, String, Text, Date, TIMESTAMP
from app.database import Base

class Leyenda(Base):
    __tablename__ = "leyendas"

    id = Column(Integer, primary_key=True, index=True)  # ID único
    nombre = Column(String(255), nullable=False)       # Nombre de la leyenda
    descripcion = Column(Text, nullable=False)         # Descripción de la leyenda
    fecha_leyenda = Column(Date, nullable=False)       # Fecha asociada a la leyenda
    provincia = Column(String(100), nullable=False)    # Provincia
    canton = Column(String(100), nullable=False)       # Cantón
    distrito = Column(String(100), nullable=False)     # Distrito
    imagen_url = Column(String(255))                   # URL de la imagen asociada
    fecha_creacion = Column(TIMESTAMP, nullable=False) # Fecha de creación
    
