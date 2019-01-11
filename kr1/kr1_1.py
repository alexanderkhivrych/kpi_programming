import math

x = float(input("Please enter x: "))
y = float(input("Please enter y: "))

try:
    R = pow(x, 2) + (0.5 * y + 4.8) / math.sin(x)
    print(f'R={str(R)}')

except ZeroDivisionError as error:
    print("cant / on 0")
