import sys
import os

def script_path(fileName=""):
    pathOut = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(pathOut)
    if fileName:
        pathOut = os.path.join(pathOut, fileName)
    return pathOut

def get_files(rmScriptName=True):
    pathAbs = script_path()
    files = os.listdir()
    if rmScriptName:
        scriptName = sys.argv[0]
        files.remove(scriptName)
    return files

def is_dir(file=""):
    return os.path.isdir(file)  #isfile

def make_tree(files):
    print(42)
    #subDir = os.path.join(path, sub)
    #os.chdir(subDir)
    #fileName, extension = os.path.splitext(file)


if __name__ == "__main__":
    #currentFiles = get_files()
    #print(currentFiles)

    scriptPath = script_path()
    for files in os.walk(scriptPath):
        head, tail = os.path.split(files[0])
        print(head, tail)
        #print(files)

#todo
#search over dirs and subdirs
#create dirs tree with files inside
#mark files on green and folders on blue
