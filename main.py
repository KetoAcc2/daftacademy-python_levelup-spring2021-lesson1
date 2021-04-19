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
    client_id = counter.counter()
    days_to_add = len(data.name) + len(data.surname)
    tmpDate = dt.today()
    registration_date = str(tmpDate.__format__('%Y-%m-%d'))
    vaccination_date = str((tmpDate + datetime.timedelta(days=days_to_add)).__format__('%Y-%m-%d'))

    print(client_id)
    print(data.name)
    print(data.surname)
    print(registration_date)
    print(vaccination_date)

    response.status_code = status.HTTP_201_CREATED

    return response.status_code, data


if __name__ == '__main__':
    uvicorn.run(app)
