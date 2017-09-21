n = int(input("Enter number till you want to create dictionary set of squares"))
#diction is used to generate a dictionary of squares of numbers
def diction(n):
    #it checks whether given input is valid or greater than 1 or not
    if (n>=1):
        y = {k: k * k for k in range(1, n + 1)}
        print(y)
    else:
        print("Enter valid input")
        n = int(input("Enter number till you want to create dictionary set of squares"))
        diction(n)
diction(n)