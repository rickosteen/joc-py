# mangle
def mangle():
    word = str(input("Type in your word to convert to all caps: "))
    wordup = word.upper()
    print(wordup)
    print(word[0:2] + word[3:])
    print(word[0:-3] + word[-2:])
mangle()
