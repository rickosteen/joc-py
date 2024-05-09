#read in text file & print all lines back out with a dash in front
def dash():
    file = open("read_file.txt")
    for line in file:
        print("-",line, end='')
dash()