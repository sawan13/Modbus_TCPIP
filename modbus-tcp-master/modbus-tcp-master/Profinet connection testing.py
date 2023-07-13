# import snap7
# client = snap7.client.Client()
# client.connect("192.168.200.10", 0, 0, 1102)
# client.get_connected()


# from pycomm3 import LogixDriver

# with LogixDriver('192.168.0.1') as plc:
#     tag_value = plc.read_tag('YourTagName')
#     print(tag_value)





# import snap7

# # Define HMI connection parameters
# hmi_ip = '192.168.200.22'  # Replace with the IP address of your Siemens HMI
# # rack = 0  # Rack number of the HMI
# # slot = 2  # Slot number of the HMI

# # Create a Snap7 client object
# client = snap7.client.Client()

# # Connect to the HMI
# client.connect(hmi_ip)
# # Read data from a specific area and address
# # area = snap7.types.AREA_PE   # Example: Process Inputs area (PE)
# # address = 0                  # Example: Start address
# # data_size = 4                # Example: Number of bytes to read
# # data = client.read_area(area, 0, address, data_size)

# # # Convert the received data to integer or any other data type as per your requirement
# # value = int.from_bytes(data, byteorder='big')

# # # Print the value
# # print("Read value:", value)

# # # Write data to a specific area and address
# # new_value = 12345  # New value to write
# # data = new_value.to_bytes(data_size, byteorder='big')
# # client.write_area(area, 0, address, data)

# # Disconnect from the HMI
# client.disconnect()




    # import snap7

    # def check_plc_connection(plc_ip):
    #     try:
    #         # Create a Snap7 client object
    #         client = snap7.client.Client()

    #         # Attempt to connect to the PLC
    #         client.connect(plc_ip)

    #         # If the above line is reached, the connection is successful
    #         print("PLC connection is active")
            
    #         # Disconnect from the PLC
    #         client.disconnect()
    #     except Exception as e:
    #         # If an exception occurs, the connection is not successful
    #         print("PLC connection is inactive")
    #         print("Error:", e)

    # # Replace '192.168.0.1' with the IP address of your Siemens PLC
    # plc_ip = '192.168.200.10'
    # check_plc_connection(plc_ip)





# import snap7

# def check_hmi_connection(hmi_ip):
#     try:
#         # Create a Snap7 client object
#         client = snap7.client.Client()

#         # Attempt to connect to the HMI
#         client.connect(hmi_ip, 0, 2)

#         # If the above line is reached, the connection is successful
#         print("HMI connection is active")

#         # Disconnect from the HMI
#         client.disconnect()
#     except Exception as e:
#         # If an exception occurs, the connection is not successful
#         print("HMI connection is inactive")
#         print("Error:", e)

# # Replace '192.168.200.22' with the IP address of your Siemens HMI
# hmi_ip = '192.168.200.22'
# check_hmi_connection(hmi_ip)
