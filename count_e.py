#count-e to count the number of e's in a string
def count_e():
    char1_in = str(input("Type in your word or phrase: "))
    lwr=[]
    lwr = char1_in.lower()
    char1_count = int(lwr.count("e"))
    print("There are ", char1_count, "quantity of e's")
count_e()

def count_ee(list):
    num_ee = 0
    for string in list:
        num_ee += string.lower().count("e")
    return num_ee

print("Count of e's is ", count_ee(["hi", "hello", "EEK!"]))