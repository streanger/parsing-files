import os
import sys

def script_path():
    '''change current path to script one'''
    path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(path)
    return path
    
def simple_read(file_name):
    '''simple_read data from specified file_name'''
    with open(file_name, "r", encoding="utf-8") as file:
        file_content = file.read().splitlines()
    return file_content
    
def justify(content, grid):
    ''' convert text to justified '''
    content = [item.strip().split(';') for item in content if item.strip()]
    # maxRow = max([len(max(item, key=len)) for item in content])
    maxRow = len(max(content, key=len))
    content = [item + [""]*(maxRow-len(item)) for item in content]
    transposed = list(map(list, zip(*content)))
    
    #signs
    horSign = '|'
    vertSign = ' ' # '_'
    lineLen = [max([len(part) for part in item]) for item in transposed]
    content = [horSign.join([(' '*1 + part).ljust(lineLen[key]+5, vertSign) if not key else part.center(lineLen[key]+5, vertSign) for key, part in enumerate(item)]) for item in content]
    line = "\n" + "-"*len(content[0]) + "\n"
    if grid:
        out = line.join(content)
    else:
        content.insert(1, line.strip())
        out = "\n".join(content)
    return out
    
    
if __name__ == "__main__":
    path = script_path()
    args = sys.argv[1:]
    if args:
        file = args[0]
        grid = int(args[1])
        content = simple_read(file)
        justified = justify(content, grid)
        print(justified)
    else:
        print("put file and grid arguments")
    
''' 
todo:
    -add delimiter option, for now: ';'
    -add newline sign, for now: '\n'
    -add horizontal sign as option
    -add vertical sign as option
    -add grid ass option
    -add reading from file or from cmd
'''
