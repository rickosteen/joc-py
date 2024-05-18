#read three files test1, text2, text3 dot txt , count number of lines per file recorded in a file counts.txt
def read3_files():
    count=int(0) 
    file = []
    for i in range(1,4):
        file = open(f"text{i}.txt")
        for line in file:
            count +=1
    print(f"total for text{i}.txt is {count}")
    count = int(0)
    print("I don't know...")    
    read3_files()