import serial
import io
from time import sleep
import os
import sys

def open_serial():
    ser = serial.Serial("COM26", baudrate=115200, timeout=0.1)
    return ser

def communication(serial, command):
    if not serial:
        return False
    if command == "QUIT":
        ser.close()
        return False
    command += "\n"
    ser.write(command.encode('utf-8'))
    some = ser.readlines()
    some = "".join([item.decode('utf-8') for item in some])
    #print(some)
    return some

def read_file(fileName, rmnl=False):
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    path = os.path.join(path, fileName)
    try:
        with open(path, "r") as file:
            if rmnl:
                fileContent = file.read().splitlines()
            else:
                fileContent = file.readlines()
    except:
        fileContent = []
    return fileContent

def iter_commands(commands=[], timeouts=(1, 0.01)):
    input("press enter to continue ")
    for index, command in enumerate(commands):
        if not index:
            ser.timeout = timeouts[0] #[s]
            response = communication(ser, command)
        else:
            ser.timeout = timeouts[1] #[s]
            response = communication(ser, command)  
        print(response)

if __name__ == "__main__":
    ser = open_serial()
    ser.timeout = 0.2
    turn_on_24G = read_file(fileName="turn_on_24G_COMMANDS.txt", rmnl=True)
    turn_off_24G = read_file(fileName="turn_off_24G_COMMANDS.txt", rmnl=True)
    turn_on_5G = read_file(fileName="turn_on_5G_COMMANDS.txt", rmnl=True)
    turn_off_5G = read_file(fileName="turn_off_5G_COMMANDS.txt", rmnl=True)    


    iter_commands(turn_off_24G, (0.5, 0.01))
    iter_commands(turn_off_5G, (0.5, 0.01))
    iter_commands(turn_on_24G, (2, 0.01))    
    iter_commands(turn_on_5G, (2, 0.01))    
    clientList = communication(ser, "ip neigh")
    print("\n", clientList)
    ser.close()



















