
import snap7

def check_plc_connection(plc_ip, rack, slot):
    try:
        # Create a Snap7 client object
        client = snap7.client.Client()

        # Attempt to connect to the PLC
        client.connect(plc_ip, rack, slot)

        # If the above line is reached, the connection is successful
        print("PLC connection is active")



        # Define the memory area and data to read
        data_length = 10  # Number of bytes to read
        db_number = 1  # DB number to read from
        start_address = 0  # Starting byte address

        # Read data from the DB
        data = plc.db_read(db_number, start_address, data_length)

        # Print the read data
        print(data)

        
        # Disconnect from the PLC
    #     client.disconnect()
    # except Exception as e:
    #     # If an exception occurs, the connection is not successful
    #     print("PLC connection is inactive")
    #     print("Error:", e)

# Replace '192.168.0.1' with the IP address of your Siemens PLC
plc_ip = '192.168.200.10'
rack = 0  # Rack number of the PLC
slot = 1  # Slot number of the PLC
check_plc_connection(plc_ip, rack, slot)
