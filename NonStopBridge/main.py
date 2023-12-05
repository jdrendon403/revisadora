import time

from api_c.apiwrite import StatusComs
from schemas.user import User

from pyModbusTCP.client import ModbusClient
from dotenv import dotenv_values


def main():
    env = dotenv_values(".env")
    # c = ModbusClient(host="172.16.5.10", port=502, unit_id=1, auto_open=True)
    c = ModbusClient(host=env.get("PLC_ADDRESS"), port=502, unit_id=1, auto_open=True)
    user = User()
    user.user = env.get("USER")
    user.password = env.get("PASSWORD")
    interval = env.get("INTERVAL")
    status = None
    while not status:
        try:
            status = StatusComs(user)
        except Exception as e:
            print(e)
    
    while True:
        try:
            status.read_status(c)
            if status.modbus:
                status.write_status()
        except Exception as e:
            print(e)

        time.sleep(int(interval))


if __name__ == "__main__":
    main()