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




if __name__ == "__main__":
    print(42)


#todo
#search over dirs and subdirs
#create dirs tree with files inside
