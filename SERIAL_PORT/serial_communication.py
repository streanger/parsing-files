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
    print(some)
    return True

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

if __name__ == "__main__":
    ser = open_serial()
    commandsList = read_file(fileName="turn_on_24G_CUT_COMMANDS.txt", rmnl=True)
    #print(commandsList)
    #sys.exit()
    for command in commandsList:
        response = communication(ser, command)
        sleep(0.2)
    ser.close()
