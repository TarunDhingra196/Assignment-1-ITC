a=int(input("Enter Income: "))
b = int(input("Enter number of dependents: "))
c = (a - 10000 - (3000 * b))
d = (c*.2)
if c < 0:
    print("NoTax")

else:


    print (c, "is the taxable income and" , d , "is the tax to be paid")