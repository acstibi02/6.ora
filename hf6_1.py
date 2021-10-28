a = int(input("Add meg 'a' értékét: "))
b = int(input("Add meg 'b' értékét: "))
c = int(input("Add meg 'c' értékét: "))
x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)


if  (b**2-4*a*c)< 0:
    print("Nincs valós megoldás! ")
else:
    print("x1 =",x1,"\nx2 =",x2)
