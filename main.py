from fastapi import FastAPI, status, Response
import uvicorn
import hashlib

app = FastAPI()

# /auth?password=haslo&password_hash=013c6889f799cd986a735118e1888727d1435f7f623d05d58c61bf2cd8b49ac90105e5786ceaabd62bbc27336153d0d316b2d13b36804080c44aa6198c533215
# /auth?password=haslo&password_hash=f34ad4b3ae1e2cf33092e2abb60dc0444781c15d0e2e9ecdb37e4b14176a0164027b05900e09fa0f61a1882e0b89fbfa5dcfcc9765dd2ca4377e2c794837e091


@app.get("/auth")
def root(password: str, password_hash: str, response: Response):
    normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()
    response.status_code = status.HTTP_401_UNAUTHORIZED
    if password_hash == normal_to_hashed:
        response.status_code = status.HTTP_204_NO_CONTENT

    return response


if __name__ == "__main__":
    uvicorn.run(app)
