#calculate_total
def calculate_total(meal,tax,tip):
    total = (tax * meal) + (tip * meal) + meal
    print("The total for the meal plus tax & tip is  $", total)

calculate_total(53.48, .07, .18)