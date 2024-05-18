#read three files test1, text2, text3 dot txt , count number of lines per file recorded in a file counts.txt
#total the number of lines all together and the number of words per file plus its sum
def read3_files():
    count=int(0) 
    file = []
    tot_words = []
    for i in range(1,4):
        file = open(f"text{i}.txt")
        for line in file:
            for words in line:
                tot_words += len(words)
            count +=1
        print(f"total for text{i}.txt is {count}")
    count = int(0)
    
    
    read3_files()