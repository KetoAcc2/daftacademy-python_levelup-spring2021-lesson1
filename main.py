import datetime
from datetime import datetime as dt

from fastapi import FastAPI, status, Response, Request
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class ClientIdCounter:
    def __init__(self):
        self.client_id = 0

    def counter(self):
        self.client_id += 1
        return self.client_id


class Data(BaseModel):
    name: str
    surname: str


counter = ClientIdCounter()


@app.post("/register")
def register_vaccination(data: Data, response: Response):
    if data.name is None or data.name == '' or\
            data.surname is None or data.surname == '':
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return response
    name = delete_numbers_or_signs(data.name.replace(' ', ''))
    surname = delete_numbers_or_signs(data.surname.replace(' ', ''))
    client_id = counter.counter()
    days_to_add = len(name) + len(surname)
    tmpDate = dt.today()
    register_date = str(tmpDate.__format__('%Y-%m-%d'))
    vaccination_date = str((tmpDate + datetime.timedelta(days=days_to_add)).__format__('%Y-%m-%d'))

    print('days_to_add:', days_to_add)
    print(client_id)
    print(name, len(name))
    print(surname, len(surname))
    print(register_date)
    print(vaccination_date)

    response.status_code = status.HTTP_201_CREATED

    preparedData = {
        "id": client_id,
        "name": data.name,
        "surname": data.surname,
        "register_date": register_date,
        "vaccination_date": vaccination_date
    }

    return preparedData


def delete_numbers_or_signs(string: str):
    tmp = ""
    for i in string:
        if i.isalpha():
            tmp += i
    return tmp


if __name__ == '__main__':
    uvicorn.run(app)
