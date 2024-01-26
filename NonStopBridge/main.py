import time

from api_c.apiwrite import StatusComs
from schemas.user import User

from pyModbusTCP.client import ModbusClient
from dotenv import dotenv_values

from config.db import inital_data, update_data


def main():
    env = dotenv_values(".env")
    print(env.get("PLC_ADDRESS"))
    c = ModbusClient(host=env.get("PLC_ADDRESS"), port=502, unit_id=1, auto_open=True)
    user = User()
    user.user = env.get("USER")
    user.password = env.get("PASSWORD")
    interval = env.get("INTERVAL")
    status = None
    status_men = None
    status_comp = None
    times = 0
    inital_data()
    while not status:
        try:
            status = StatusComs(user)
            print(status.user.user)
        except Exception as e:
            print(e)
    
    while True:
        try:
            status.read_status(c)       
            if status.modbus:
                status_comp = vars(status.status).copy()
                status_comp.pop("last_update")
                times += 1 
                if status_men != status_comp or times > (60/int(interval)):
                    status.write_status()
                    update_data(1, status_comp["peso"], status_comp["metros"], status_comp["rendimiento"])
                    status_men = status_comp.copy()
                    times = 0
        except Exception as e:
            print(e)
        time.sleep(int(interval))


if __name__ == "__main__":
    main()