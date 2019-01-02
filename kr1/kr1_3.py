def input_n():
    try:
        num = int(input("Please enter N: "))

        if num <= 0:
            print("Value must be a greater than 0")
            return input_n()
        return num

    except ValueError:
        print("No.. input string is not an Integer. It's a string")
        return input_n()


def input_x():
    try:
        return int(input("Please enter x: "))

    except ValueError:
        print("No.. input string is not an Number. It's a string")
        return input_x()


n = input_n()
x = input_x()

sum = 1
xmul = 1

for i in range(1, n):
    xmul *= x
    sum += xmul / i

print(sum)
