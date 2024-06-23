from fastapi import FastAPI
from contrib.routers import api_router

app = FastAPI(tittle="workout_api")
app.include_router(api_router)


if __name__ == "main":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=0000, log_level="info", reload=True)

