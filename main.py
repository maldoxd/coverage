from fastapi import FastAPI
from app.api import member_coverage

app = FastAPI()

app.include_router(member_coverage.router)

@app.get("/")
async def init():
    return "Init api test interview =)"
