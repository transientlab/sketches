# obd-read

import obd

connection = obd.OBD()
if connection.is_connected():
    print("CONNECTED\nprotocol name: {}\nport name: {}\nprotocol id: {}\n".format(connection.protocol_name(), connection.port_name(), connection.protocol_id()))
    print("Available commands:")
    connection.print_commands()
else:
    print("CONNECTION ERROR")

cmd = obd.commands.GET_DTC
response = connection.query(cmd)
print(response.value)
connection.close()