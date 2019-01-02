num_array = list()
size = input("Enter how many elements you want:")
print('Enter numbers in array: ')

def double_num(prompt):
    num = input(prompt)

    if len(num) == 2:
        try:
            return int(num)
        except ValueError:
            print("Error, you must enter a number")
    else:
        print('Try again, now with a two-digit number')
        return double_num(prompt)


for i in range(int(size)):
    n = double_num("two-digit number' :")
    num_array.append(int(n))

sum_array = list(map(lambda el: el % 100 // 10 + el % 10, num_array))

print('List of sum: {0}'.format(sum_array))
