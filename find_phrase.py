import os
import sys
import itertools

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

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

def all_indexes(value, data):
    try:
        indexes = [key for key, item in enumerate(data) if item == value]
    except:
        indexes = []   #to not cause error while searching for start
    return indexes

def grouper(n, l):
    return [tuple(l[i:i+n]) for i in range(0, len(l), n)]

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

def main(commands=[]):
    phrase = commands[0]    #put phrase to search for
    path = script_path()
    filesHtm = [item for item in os.listdir(path) if os.path.isfile(item)]
    filesHtm.remove(sys.argv[0])    #remove script from files to search

    searchResult = ["Phrase to search for: " + phrase + "<hr>"]
    for file in filesHtm:
        content = read_file(file)
        LINES = ""
        for index, line in enumerate(content):
            if phrase in line:
                LINES += str(index) + ", "
        if LINES:
            searchResult.append("<br><file> " + file + " <lines> " + LINES)

    if "-w" in commands:
        write_file(fileName="phrase_" + phrase + ".txt",
                   content=searchResult,
                   response=True,
                   overWrite=True,
                   endline="\n")   
    else:
        for item in searchResult:
            print(item)

            
if __name__ == "__main__":
    main(sys.argv[1:])

