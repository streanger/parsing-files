#copied from stack with some changes
import sys
import os

def script_path(fileName=""):
    pathOut = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(pathOut)
    if fileName:
        pathOut = os.path.join(pathOut, fileName)
    return pathOut

def list_files(startpath):
    fullTree = ""
    for root, dirs, files in os.walk(startpath):
        if ".git" in root:
            continue
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        dirLine = '{}{}/'.format(indent, os.path.basename(root))
        fullTree += dirLine + "\n"
        #print(dirLine)
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            fileLine = '{}{}'.format(subindent, f)
            fullTree += fileLine + "\n"
            #print(fileLine)
    return fullTree[:-2]

if __name__ == "__main__":
    absPath = script_path()
    fullTree = list_files(absPath)
    print(fullTree)
