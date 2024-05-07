#pyramid
def pyramid(text, n):
    for i in range(1,(n+1)):
        print(text * i )
pyramid("*", 2)
pyramid("+", 5)
pyramid("x", 10)
