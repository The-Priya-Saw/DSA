a  = int(input("enter any positive integer: "))
factorial = 1
if a < 0:
    print("factorial of ", a , "is invalid" )
elif a == 0:
    print("factorial of ", a , "is", factorial)
else:
    while (a>0):
        factorial = factorial*a
        a -= 1
print("factorial is", factorial)

