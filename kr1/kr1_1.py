import math

try:
    x = float(input("Please enter x: "))
    y = float(input("Please enter y: "))

    R = pow(x, 2) + (0.5 * y + 4.8) / math.sin(x)
    print(f'R={str(R)}')

except ZeroDivisionError:
    print("cant / on 0")
except ValueError:
    print("Value must be a natural number!")
