#average_neg_evens: print(average_neg_evens([0,1,2,-2,-3,-4,3,4]))
def avg_neg_evens(num_list):
    neg_nums=[]
    for n in num_list:
        if n < 0 and n %2 == 0:
            neg_nums.append(n)
    result = (sum(neg_nums) / len(neg_nums))
    print(result)
avg_neg_evens([0, 1, 2, -2, -3, -4, 3, 4])
