import sys

# commandline variable a, b, c
a = float(sys.argv[1]) 
b = float(sys.argv[2]) 
c = float(sys.argv[3]) 

x1 = (-b + ((b**2 - 4*a*c)**0.5))/(2*a)
x2 = (-b - ((b**2 - 4*a*c)**0.5))/(2*a)

print(f'x1 = {x1:.4f}')
print(f'x2 = {x2:.4f}')

