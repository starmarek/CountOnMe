from fastapi import APIRouter
from sqlalchemy import text

from ..deps import SessionDep

router = APIRouter()


@router.get("/")
def read_users(session: SessionDep) -> str:
    result = session.execute(text("select 'hello world'"))
    return str(result.all())
