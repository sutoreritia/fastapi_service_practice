from fastapi import FastAPI

app = FastAPI(title="FastAPI Service Practice")


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "fastapi_service_practice"}


@app.get("/version")
def get_version():
    return {"version": "1.0.0", "stage": "learning"}