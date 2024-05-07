# take in 20 numbers then print average
qnum=[]
for i in range(20):
    number = int(input("Type in number"))
    qnum.append(number) 
    print(qnum)
average = sum(qnum) / 20
print(average)