print('TurtleDraw Starting...')


tddata = open("turtledraw.txt", "r")

line = tddata.readline()

while line:   
        print(line, end='')
        parts = line.split(' ')
        print (parts)
        line = tddata.readline()