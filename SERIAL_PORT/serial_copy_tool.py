import serial
import io
from time import sleep
import os
import sys

def open_serial():
    ser = serial.Serial("COM26", baudrate=115200, timeout=0.1)	#this is for now (like any other this kind of rubbish :))
    return ser

def all_indexes(value, data):
    indexes = [key for key, item in enumerate(data) if item == value]
    return indexes

def communication(serial, command):
    if not serial:
        return False
    #while (1):
    #command = input(">")
    if command == "QUIT":
        ser.close()
        return False
    #ser.write("\n".encode('utf-8'))
    command += "\n"
    ser.write(command.encode('utf-8'))
    some = ser.readlines()
    some = "".join([item.decode('utf-8') for item in some])
    print(some)
    return True, some

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

def make_dir(dirName="REPLACED"):
    path = script_path()
    path = os.path.join(path, dirName)
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as exc:
            print("error while making new dir...")
            sys.exit()
    return path

def write_file(fileName, content, endline="\n", overWrite=False, response=True, rmSign=[]):
    if not content:
        return False
    contentType = type(content)
    if contentType in (list, tuple):
        pass
    elif contentType in (int, str):
        content = [str(content)]
    elif contentType is (dict):
        content = list(content.items())
    else:
        return False
    if overWrite:
        mode="w"
    else:
        mode="a"
    path = script_path()
    path = make_dir("WEB_CONTENT")   #make new dir
    path = os.path.join(path, fileName)
    with open(path, mode) as file:
        for item in content:
            if rmSign:
                for sign in rmSign:
                    item = (str(item)).replace(sign, "")
            file.writelines(str(item)+endline)
        file.close()
        if response:
            print("\n--< written to: {0} | contentType: {1}".format(fileName, contentType))
    return True


if __name__ == "__main__":
    ser = open_serial()
    response = True
    while (response):
        command = input(">")
        response, text = communication(ser, command)
        #if command == "ls":
        if command == "xxxx":
            files = text.split()
            #files = [item for item in files if item[-4:] in (".htm", ".txt", ".css")]
            files = [item for item in files if item[-3:] in (".js")]
            #print(files)
            for file in files:
                listDir = os.listdir(os.path.join(script_path(), "WEB_CONTENT"))
                if not (file in listDir):
                    command = "cat " + file
                    response, text = communication(ser, command)
                    if text:
                        if file[-4:] == ".htm":
                            start = all_indexes("<", text)[0]
                            stop = all_indexes(">", text)[-1]+1
                            text = text[start:stop]
                    else:
                        continue
                    #input("continue? ")
                else:
                    continue
                try:
                    write_file(fileName=file,
                               content=text,
                               response=True,
                               overWrite=True,
                               endline="")
                except:
                    write_file(fileName="CANT_WRITE.txt",
                               content=file,
                               response=True,
                               overWrite=False,
                               endline="\n")
