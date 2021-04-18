from fastapi import FastAPI, status, Response
import uvicorn
import hashlib

app = FastAPI()


@app.get("/auth")
def validate_password(password: str, password_hash: str, response: Response):
    normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()
    response.status_code = status.HTTP_401_UNAUTHORIZED
    if password_hash == normal_to_hashed:
        response.status_code = status.HTTP_204_NO_CONTENT

    return response


if __name__ == '__main__':
    uvicorn.run(app)
