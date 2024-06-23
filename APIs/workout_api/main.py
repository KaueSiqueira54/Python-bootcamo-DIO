from fastapi import FastAPI

app = FastAPI(tittle="workout_api")

if __name__ == "main":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=0000, log_level="info", reload=True)

