#one through three
#1a
x = 1
while x < 6:
    print("x is  :", x)
    x += 1
print("done")

#1b
x = 2
while x < 12:
    print("x is  :", x)
    x += 3
print("done")

#1c
x = -10
while x <= 0:
    print("x is:", x, "", end="  " )
    x += 2
print("done")

#1d
x = 0
while x < 4:
    print("****")
    x += 1
print("done")

#2
word = 'CSCI 150'
char=[]
while char != '0':
    for char in word:
        print(char)
print("done")

#3
num = []
numlist=[]
numavg=[]
while num != 0:
    num = int(input("type in numbers. zero '0' when finished :"))
    numlist.append(num)
    numavg = sum(numlist) / len(numlist)
print(sorted(numlist))
print("The total is: ", sum(numlist))
print("The average is : ", numavg)

      