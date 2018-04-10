#!/usr/bin/python3
#to read metadata from images
from PIL import Image
from termcolor import colored
import sys
import os

def script_path():
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)  #it seems to be quite important
    return path

def read_meta(filename):
    #from png files
    image = Image.open(filename)
    info = image.info
    return info

#from jpeg, etc files

def main():
    args = sys.argv[1:]
    if args:
        files = [args[0]]
    else:
        path = script_path()
        files = [item for  item in os.listdir(path) if item[-4:] == ".png"]
    #print(files)
    #sys.exit()
    for item in files:
        metadata = read_meta(item)
        print("{0}: {1}".format(colored(item, "cyan"), metadata))

if __name__ == "__main__":
    main()
