import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/method", status_code=200)
def test_counter():
    return {"method": "GET"}


@app.put("/method", status_code=200)
def test_counter():
    return {"method": "PUT"}


@app.options("/method", status_code=200)
def test_counter():
    return {"method": "OPTIONS"}


@app.delete("/method", status_code=200)
def test_counter():
    return {"method": "DELETE"}


@app.post("/method", status_code=201)
def test_counter():
    return {"method": "POST"}


if __name__ == "__main__":
    uvicorn.run(app)
