#write to new file "out.txt" from user's input. zero "0" when finished
def out_to_file():
    file = open("out.txt", 'a')
    while True:
        line = input("Type in number, zero when done: ")
        if line == '0':
            break
        file.write(line + '\n')
        
    file.close()

out_to_file()