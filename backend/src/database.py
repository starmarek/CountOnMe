from sqlalchemy import create_engine

from .config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
