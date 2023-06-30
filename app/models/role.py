from sqlalchemy import Column, String

from .base import BaseModel


class Role(BaseModel):
    __tablename__ = 'role'
    name = Column(String(100), nullable=False)
