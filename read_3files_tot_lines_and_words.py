#read three files test1, text2, text3 dot txt , count number of lines per file recorded in a file counts.txt
#total the number of lines all together and the number of words per file plus its sum
def read3_files():
    file = []
    tot_lines = int(0)
    all_words = int(0)
    for i in range(1,4):
        file = open(f"text{i}.txt")
        count=int(0)
        tot_words = int(0)
        for line in file:
            #for words in line:
            words = line.split()
            tot_words += len(words)
            count +=1
        tot_lines +=count
        all_words +=tot_words
        print(f"total lines for text{i}.txt is {count} , {tot_words} total")
    print(f"TOTAL: {tot_lines} lines,  {all_words} words")
read3_files()