from fastapi import FastAPI
from app.controllers import user_controller

app = FastAPI()

# Mount API routes
app.include_router(user_controller.router, prefix="/api/users")

