from fastapi import FastAPI

app = FastAPI(title="Coffee Api")


@app.get("/", status_code=200)
async def root():
    return {"message": "Welcome to Life Tracker"}
