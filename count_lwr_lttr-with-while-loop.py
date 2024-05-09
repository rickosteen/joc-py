#count letter from list - with while loop instead
def count_letter(list,ltr):
    lowered=[]
    index = 0
    ltr_count= int(0)
    lowered = [word.lower() for word in list]
    while index < len(lowered):
        currentWord = lowered[index]
        for char in currentWord:
            if char == ltr:
                ltr_count += 1
        index += 1
    return ltr_count
list = ["HELLO", "goodbye", "1234 Oooh!"]
print(count_letter(list, "o"))