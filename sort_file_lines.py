import os
import sys

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path

def read_file(fileName, rmnl=True):
    with open(fileName, "r") as file:
        if rmnl:
            fileContent = file.read().splitlines()
        else:
            fileContent = file.readlines()
    return fileContent
    
    
if __name__ == "__main__":
    path = script_path()
    args = sys.argv[1:]
    try:
        file = args[0]
        content = read_file(file)
        # content = [item.split(":")[1] for item in content]
        content.sort()
        print("\n".join(content))
    except:
        print("-> failed to read file. Specify correct one.")
        
        
        