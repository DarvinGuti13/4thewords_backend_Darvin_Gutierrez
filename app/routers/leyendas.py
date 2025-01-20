from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Leyenda
from app.database import get_db
from pydantic import BaseModel
from typing import Optional

################################ router para leyendas##########################################
router = APIRouter(
    prefix="/leyendas",
    tags=["leyendas"]
)

########################### Obtener todas las leyendas############################################
@router.get("/")
def obtener_leyendas(db: Session = Depends(get_db)):
    leyendas = db.query(Leyenda).all()
    return leyendas


########################### Filtrar leyendas por Nombre ###########################################
@router.get("/filtrar")
def filtrar_leyendas(
    nombre: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(Leyenda)
    if nombre:
        query = query.filter(Leyenda.nombre.like(f"%{nombre}%"))
    
    return query.all()




############################################## Modelo para crear leyenda#######################################
class LeyendaCreate(BaseModel):
    nombre: str
    descripcion: str
    fecha_leyenda: str
    provincia: str
    canton: str
    distrito: str
    imagen_url: str
    

######################################### Crear una nueva leyenda #########################################
@router.post("/")
def crear_leyenda(
    leyenda: LeyendaCreate, 
    db: Session = Depends(get_db)
):
    # Valida si ya existe una leyenda con el mismo nombre
    leyenda_existente = db.query(Leyenda).filter(Leyenda.nombre == leyenda.nombre).first()
    if leyenda_existente:
        raise HTTPException(
            status_code=400,
            detail=f"La leyenda con el nombre '{leyenda.nombre}' ya existe."
        )

    try:
        # Crear una nueva leyenda
        nueva_leyenda = Leyenda(
            nombre=leyenda.nombre,
            descripcion=leyenda.descripcion,
            fecha_leyenda=leyenda.fecha_leyenda,
            provincia=leyenda.provincia,
            canton=leyenda.canton,
            distrito=leyenda.distrito,
            imagen_url=leyenda.imagen_url,
        )
        db.add(nueva_leyenda)
        db.commit()
        db.refresh(nueva_leyenda)
        return nueva_leyenda

    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear la leyenda: {str(e)}"
        )


#################### Obtener una leyenda específica por ID####################
@router.get("/{leyenda_id}")
def obtener_leyenda(leyenda_id: int, db: Session = Depends(get_db)):
    leyenda = db.query(Leyenda).filter(Leyenda.id == leyenda_id).first()
    if not leyenda:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    return leyenda

class LeyendaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    fecha_leyenda: Optional[str] = None
    provincia: Optional[str] = None
    canton: Optional[str] = None
    distrito: Optional[str] = None
    imagen_url: Optional[str] = None

################## Actualiza o edita Leyenda seleccionada #################

@router.put("/{leyenda_id}")
def actualizar_leyenda(
    leyenda_id: int,
    leyenda_data: LeyendaUpdate,  
    db: Session = Depends(get_db)
):
    # Buscar la leyenda por ID
    leyenda = db.query(Leyenda).filter(Leyenda.id == leyenda_id).first()
    if not leyenda:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    
    for key, value in leyenda_data.dict(exclude_unset=True).items():
        setattr(leyenda, key, value)

    db.commit()
    db.refresh(leyenda)
    return {"message": "Leyenda actualizada exitosamente", "leyenda": leyenda}



###############################Eliminar Leyenda#################################

@router.delete("/{leyenda_id}")
def eliminar_leyenda(
    leyenda_id: int,
    confirmar: bool = False,  # Parámetro para confirmación
    db: Session = Depends(get_db)
):
    # Verificar si la leyenda existe
    leyenda = db.query(Leyenda).filter(Leyenda.id == leyenda_id).first()
    if not leyenda:
        raise HTTPException(status_code=404, detail="Leyenda no encontrada")
    
    # Verificar confirmación
    if not confirmar:
        raise HTTPException(
            status_code=400,
            detail="Se requiere confirmación para eliminar la leyenda."
        )

    # Eliminar la leyenda
    db.delete(leyenda)
    db.commit()
    return {"message": "Leyenda eliminada exitosamente"}
