import sys
import os

def read_file(fileName, rmnl=False):
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
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
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    path = os.path.join(path, fileName)
    with open(path, mode) as file:
        for item in content:
            if rmSign:
                for sign in rmSign:
                    item = (str(item)).replace(sign, "")
            file.writelines(str(item)+endline)
        file.close()
        if response:
            print("--< written to: {0} | contentType: {1}".format(fileName, contentType))
    return True

def main(args):
    file = ""
    if not args:
        print(">>> tool for convert print statement from py2.x to py3.x in script")
        print(">>> usage:")
        print(">>> <script> <file_py_2x.py>")
        sys.exit
    else:
        file = args[0]
        if not os.path.isfile(file):
            print(">>> file not exists")
            sys.exit()
        if not file[-3:] == ".py":
            print(">>> file is not a python script")
            sys.exit()
    #file = "some.txt"
    content = read_file(file)
    newFile = []
    for line in content:
        if "print" in line:
            printIndex = line.find("print")
            if not line[printIndex+5] == " ":
                newLine = line
            #make sure 'print' isnt in variable or function name
            elif line[:printIndex].split() == []:
                newLine = line[:printIndex] + "print(" + line[printIndex+6:-1] + ")" + "\n"
            elif "#" in line[:printIndex].split():
                newLine = line[:printIndex] + "print(" + line[printIndex+6:-1] + ")" + "\n"
        else:
            newLine = line
        newFile.append(newLine)
    write_file(file[:-3] + "New.py", newFile, endline="")
    return True


if __name__ == "__main__":
    main(sys.argv[1:])

