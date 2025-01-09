from src.models.base import Base
from src.models.user import User
from src.models.endpoint import Endpoint
from src.models.check import Check
from typing import TypeVar

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType")
UpdateSchemaType = TypeVar("UpdateSchemaType")

__all__ = [
    "Base",
    "User",
    "Endpoint",
    "Check",
    "ModelType",
    "CreateSchemaType",
    "UpdateSchemaType"
]