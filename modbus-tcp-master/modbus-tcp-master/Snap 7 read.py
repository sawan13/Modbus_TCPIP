import snap7

# Define the IP address and TCP port of the PLC
plc_ip = '192.168.200.10'
rack = 0  # Rack number of the HMI
slot = 1  # Slot number of the HMI

# Connect to the PLC
plc = snap7.client.Client()
plc.connect(plc_ip, rack, slot)

# Read data from a specific area and address
area = snap7.types.AREA_PE   # Example: Process Inputs area (PE)
address = 0                  # Example: Start address
data_size = 4                # Example: Number of bytes to read
data = client.read_area(area, 0, address, data_size)


# Read the value of the input
input_value = plc.read_area(area, 0, byte_offset, snap7.snap7types.S7WLBit, bit_offset)

# Print the value of the input
print(data)

# Disconnect from the PLC
plc.disconnect()
