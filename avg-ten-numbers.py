#avg.py prints average of ten numbers
#numbers=[]
sum = 0
for i in range(10):
    num = int(input("Enter number # "))
    sum = sum + num
    #numbers.append(num)
average = sum / 10
#average = sum(numbers) / len(numbers)
print("Average is ", average)
