from fastapi import FastAPI, status, Response, Request
import uvicorn
import hashlib

app = FastAPI()


@app.get("/auth")
def validate_password(request: Request, response: Response):
    print(str(request.query_params))

    params = list(request.query_params.values())
    response.status_code = 401
    if len(params) == 2:
        password = params[0]
        password_hash = params[1]
        normal_to_hashed = hashlib.sha512(password.encode()).hexdigest()
        if password_hash == normal_to_hashed:
            response.status_code = 204

        print(password)
        print(password_hash)
        print(normal_to_hashed)
        
    return response

# params = str(request.query_params).split('&')
    # if len(params) == 2:
    #     password = ''
    #     turner = False
    #     for i in params[0]:
    #         if turner:
    #             password += i
    #         if i == '=':
    #             turner = True
    #
    #     password_hash = ''
    #     turner = False
    #     for i in params[1]:
    #         if turner:
    #             password_hash += i
    #         if i == '=':
    #             turner = True

if __name__ == '__main__':
    uvicorn.run(app)
