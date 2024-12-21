from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.sql import text
from sqlmodel.ext.asyncio.session import AsyncSession

from .config.database import get_session

app = FastAPI(title="Coffee Api")


@app.get("/", status_code=200)
async def root():
    return {"message": "Welcome to Life Tracker"}


@app.get("/test-db-connection")
async def test_db_connection(session: AsyncSession = Depends(get_session)):
    try:
        result = await session.exec(text("SELECT 1"))
        return {"status": "success", "message": "Database connected!"}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Database connection error")
        return {"status": "error", "message": str(e)}
