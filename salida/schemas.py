# ==========================================================
# SCHEMAS PYDANTIC — GENERADOS AUTOMÁTICAMENTE
# Fuente: psm_fastapi.api  |  NO EDITAR
# ==========================================================

from pydantic import BaseModel
from datetime import datetime


class Producto(BaseModel):
    nombre        : str
    precio        : float
    stock         : float
    disponible    : bool

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Laptop Pro",
                "precio": 999.99,
                "stock": 42,
                "disponible": True,
            }
        }


class Cliente(BaseModel):
    nombre        : str
    email         : str
    edad          : float

    class Config:
        json_schema_extra = {
            "example": {
                "nombre": "Laptop Pro",
                "email": "usuario@ejemplo.com",
                "edad": 30,
            }
        }


class Pedido(BaseModel):
    numero        : float
    total         : float
    estado        : str
    fecha         : datetime

    class Config:
        json_schema_extra = {
            "example": {
                "numero": 1001,
                "total": 150.00,
                "estado": "pendiente",
                "fecha": "2024-01-15",
            }
        }


class Factura(BaseModel):
    numeroFactura : float
    total         : float
    cantidadArticulos : float
    fechaGeneracion : datetime
    cliente       : str
    nombreCliente : float

    class Config:
        json_schema_extra = {
            "example": {
                "numeroFactura": 0.0,
                "total": 150.00,
                "cantidadArticulos": 0.0,
                "fechaGeneracion": "2024-01-15T00:00:00",
                "cliente": "cliente ejemplo",
                "nombreCliente": 0.0,
            }
        }

