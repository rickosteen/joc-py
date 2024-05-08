#count letter from list
def count_letter(list,ltr):
    lowered=[]
    ltr_count= int(0)
    for wrd in list:
        lowered = wrd.lower()
        for char in lowered:
            if char == ltr:
                ltr_count += 1
    return ltr_count
list = ["HELLO", "goodbye", "1234 Oooh!"]
print(count_letter(list, "o"))