inputString = str(input("Please, enter a string: "))

prevChar = ""
currentString = ""
longestString = ""

for char in inputString:
    if char.isalpha():
        currentString += char
        if len(currentString) > len(longestString):
            longestString = currentString
    else:
        currentString = char
    prevChar = char

print('Longest substring with latters is: {0}'.format(longestString))
