import csv

def open_csv(fileName):
    with open(fileName, newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for key,row in enumerate(spamreader):
            #print(' '.join(row))
            #print(type(row), len(row))
            if key%1000000 == 0:
                print(key)

file = 'some.csv'
open_csv(file)
