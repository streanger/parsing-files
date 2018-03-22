import os
import sys

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
    path = make_dir()   #make new dir
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

def main():
    filesTxt = [item for item in os.listdir() if item[-4:]==".txt"]
    for item in filesTxt:
        try:
            content = read_file(item)
        except:
            print("wrong name or file not exists: {0}".format(item))
            continue
        for x in range(3, 150):
            content = [item.replace(' '*x, '') for item in content]   #remove multi-spaces
        fileOut = item.split(".")[0]+"_CUT.txt"
        write_file(fileName=fileOut,
                   content=content,
                   response=True,
                   overWrite=True,
                   endline="")   


if __name__ == "__main__":
    main()
    #todo -> read list of sign to convert as arg
    #args = sys.argv[1:]
    #toReplace = eval(args[0])  #put args[0] as "[('some','thing'),('this','then')]"










