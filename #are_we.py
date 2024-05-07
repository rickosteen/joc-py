#are_we
def calls():
    call1 = input("Are we ___ yet? ")
    call2 = int(input("How many times to print quesiton? "))
    for i in range(call2):
        print(f"Are we {call1} yet?", end=" ")


calls()
