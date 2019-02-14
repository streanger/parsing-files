import sys
import os

def script_path():
    current_path = os.path.realpath(os.path.dirname(sys.argv[0]))
    os.chdir(current_path)
    return current_path
    
    
def simple_read(file):
    with open(file, 'r') as f:
        out = f.read()
    return out
    
    
def replace_leading_tabs(data):
    '''
        -replace leading tabs to spaces, and detect if number of spaces is divided by 4 
        -whitesign-lines are converted to newlines
    '''
    wrong = [('------', '------'*4), ('wrong'.rjust(12), ' lines'), ('------', '------'*4)]
    out = []
    for key, line in enumerate(data.splitlines()):
        if not line.lstrip():
            out.append('')
            continue
        index = line.index(line.lstrip())
        leftSide = line[:index].replace('\t', ' '*4)
        if leftSide.count(' ') % 4:
            wrong.append(((str(key) + ' | ').rjust(14), repr(line)))
            number = leftSide.count(' ') // 4
            leftSide = ' '*4*number
        rightSide = line[index:]
        new = leftSide + rightSide
        out.append(new)
    strOut = '\n'.join(out)
    strWrong = '\n'.join([''.join(item) for item in wrong])
    return strOut, strWrong
    
    
if __name__ == "__main__":
    args = sys.argv[1:]
    if args:
        file = args[0]
    else:
        print("--> put file as argument\n")
        sys.exit()
        
    script_path()
    data = simple_read(file)
    strOut, strWrong = replace_leading_tabs(data)
    print(strOut)
    # print(strWrong)           # print lines with errors
    