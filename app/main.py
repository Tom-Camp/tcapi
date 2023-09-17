from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import User, database

app = FastAPI(title="Tom.Camp")

origins = [
    "http://tcapi.localhost",
    "https://tcapi.localhost",
    "http://tcapi.localhost:8008",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return await User.objects.all()


@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
