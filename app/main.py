from fastapi import FastAPI
from routes.check_health import router as check_router

app = FastAPI()

app.include_router(check_router)
