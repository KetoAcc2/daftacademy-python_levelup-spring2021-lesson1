from fastapi import FastAPI, status, Response, Request
import uvicorn
import hashlib

app = FastAPI()


@app.get("/auth")
def validate_password(request: Request, response: Response):
    print(str(request.query_params))

    params = str(request.query_params).split('&')
    password = ''
    turner = False
    for i in params[0]:
        if turner:
            password += i
        if i == '=':
            turner = True

    password_hash = ''
    turner = False
    for i in params[1]:
        if turner:
            password_hash += i
        if i == '=':
            turner = True

    if password_hash is not None and password is not None and password_hash != '' and password != '':
        normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()
        if password_hash == normal_to_hashed:
            response.status_code = status.HTTP_204_NO_CONTENT
        else:
            response.status_code = status.HTTP_401_UNAUTHORIZED
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED

    return response


if __name__ == '__main__':
    uvicorn.run(app)
