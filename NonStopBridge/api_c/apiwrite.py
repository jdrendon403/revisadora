import requests
import json

from datetime import datetime

from schemas.status import Status
from schemas.user import User

from utilities.array_u import array_subset, chararraytofloat

from dotenv import dotenv_values


class StatusComs():
    token: str
    user: User
    base_url: str
    modbus: bool
    status: Status

    def __init__(self, user:User) -> None:
        env = dotenv_values(".env")
        self.base_url = env.get("BASE_URL")
        self.user = user
        self.status = Status()
        self.modbus = False
        self.login()
        return

    def login(self):
        url = self.base_url + "login/"
        data = json.dumps(self.user.__dict__)
        response = requests.post(url, data)
        print(response.status_code)
        self.token = "Bearer " + response.json()["token"]
        return



    def write_status(self):
        url = self.base_url + "write_status/"
        headers = {
            'accept': 'application/json',
            'Authorization': '',
            'Content-Type': 'application/json'
        }
        headers['Authorization'] = self.token
        data = json.dumps(self.status.__dict__)
        response = requests.put(url, data=data, headers=headers)
        return
    
    def read_status(self, m_client):
        regs = m_client.read_holding_registers(2000, 120)
        if regs:
            regs.extend(m_client.read_holding_registers(2120, 120))

            self.status.articulo = ''.join(array_subset(regs.copy(), 0, 20))
            self.status.cliente = ''.join(array_subset(regs.copy(), 20, 20))
            self.status.n_articulo = ''.join(array_subset(regs.copy(), 40, 20))
            self.status.color = ''.join(array_subset(regs.copy(), 100, 20))
            self.status.peso = chararraytofloat(array_subset(regs.copy(), 200, 5))
            self.status.metros = chararraytofloat(array_subset(regs.copy(), 220, 5))
            self.status.n_rollo = int(chararraytofloat(array_subset(regs.copy(), 120, 5)))
            self.status.rendimiento = chararraytofloat(array_subset(regs.copy(), 140, 20))
            self.status.operario = ''.join(array_subset(regs.copy(), 160, 20))
            self.status.ancho = chararraytofloat(array_subset(regs.copy(), 180, 20))

            self.status.last_update = str(datetime.now())
            self.modbus = True
        else:
            self.modbus=False



