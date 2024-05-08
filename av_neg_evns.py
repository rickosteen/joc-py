#average_neg_evens: print(average_neg_evens([0,1,2,-2,-3,-4,3,4]))
def avg_neg_evens(num_list):
    neg_nums=[]
    for n in num_list:
        if n < 0:
            neg_nums.append(n)
        else:
            if n == 0:
                print()
    result = (sum(neg_nums) / len(neg_nums))
    print(result)
avg_neg_evens([0, 1, 2, -2, -3, -4, 3, 4])
