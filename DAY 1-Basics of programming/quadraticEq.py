a = float(input("Enter the coeffiecent of x2 : "))
b = float(input("Enter the coeffiecent of x : "))
c = float(input("Enter the constant term : "))

result = b*b - 4*a*c
dis = result**1/2


if dis > 0:
        print(" real and different roots ")
        print((-b + result)/(2 * a))
        print((-b - result)/(2 * a))

elif dis == 0: 
        print(" real and same roots") 
        print(-b / (2 * a)) 
      
    # when discriminant is less than 0
else:
        print("Complex Roots") 
        print(- b / (2 * a), " + i", result) 
        print(- b / (2 * a), " - i", result) 

