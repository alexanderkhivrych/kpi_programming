LAST_DIGIT_CONDITION = 3


def input_val():
    try:
        num = int(input("Please enter a natural number: "))

        if num < 1:
            print("Value must be a natural number!")
            return input_val()
        return num

    except ValueError:
        print("No.. input string is not an Integer. It's a string")
        return input_val()


number = input_val()

print(
    f'It is pair number: {number % 2 == 0},'
    f'Is las digit = {LAST_DIGIT_CONDITION}:{number % 10 == LAST_DIGIT_CONDITION:}'
)
