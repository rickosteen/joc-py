#count letter from list
def count_letter(list,ltr):
    lowered=[]
    for ltt_r in list:
        if ltt_r == ltr:
            lowered = ltr.lower().count()
        print(lowered)
list = ["HELLO", "goodbye", "1234 Oooh!"]
print(count_letter(list, "o"))
