#starting while loops
#1a

j = 4
while j >= -4:
    print(j)
    j -=1

#1b
string = "Hello"
builder = ""
i = 0
while i < len(string):
    builder += string[i].swapcase()
    print(i, builder)
    i += 1
print(string, "->", builder)

#1c
x = 0
i = 1
while x < 20:
    if x > 5:
        x += 15
    else:
        x += 1
    print(i, x)
    i += 1

#2a
string = "HELLO"
x = 0
while string[x] != 'L':
    print(string[x], end=" ...  ")
    x += 1
print("\n", string, "first L is at", x)

#2b 
# Assume the user enters the following:
# hello goodbye cat dog DONE done
list = []
prompt = "Please entr word, 'done' to finish "
response = input(prompt)
while response != "done":
    list.append(response)
    response = input(prompt)
print(sorted(list))

#2c
x = 0
while x < 20:
    print("x1 is: ", x)
    if x > 5:
        print("x2 is: ", x)
        if x % 2 == 0:
            x *= 2
            print("x3 is: ", x)
        else:
            x *= -1
            print("x4 is: ", x)
    else:
        x += 10
        print("x5 is: ", x)
    x += 1
    print("x6 is: ", x)
print(x)

