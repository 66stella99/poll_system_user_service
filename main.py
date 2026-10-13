from contextlib import asynccontextmanager

from fastapi import FastAPI

from controller.user_controller import router as user_router
from repository.database import database


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(title="Poll System - User Service", lifespan=lifespan)

app.include_router(user_router)
