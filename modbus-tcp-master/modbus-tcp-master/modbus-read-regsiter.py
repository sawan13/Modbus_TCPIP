from pymodbus.client.sync import ModbusTcpClient
from datetime import datetime, time
import random
import json
import time


# datetime object containing current date and time
def current_time():
    now = datetime.now().isoformat()
    return now

host = 'localhost'   #ip of your hmi
port = 502
client = ModbusTcpClient(host, port)
while True:
    client.connect()

    rr = client.read_holding_registers(1000,1,unit=1)
 
    data = {
        "datetime": current_time(),
        "data": rr.registers[0]    # register will return a list. To query individual register specify the array item e.g. registers[0] to get value from first register

    }
    print(json.dumps(data))
    time.sleep(5)