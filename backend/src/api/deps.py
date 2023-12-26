import typing as t

from fastapi import Depends
from sqlalchemy.orm import Session

from ..database import engine


def get_db() -> t.Generator:
    with Session(engine) as session:
        yield session


SessionDep = t.Annotated[Session, Depends(get_db)]
