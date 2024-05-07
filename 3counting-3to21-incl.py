#3 counting from -3 to 21 incl
for i in range(-3, 22, 3):
    if i == 21:
        print(i, end=" ") #print w/out comma
    else:
        print(i, end=", ") #print w comma's if not equal to 21
print()