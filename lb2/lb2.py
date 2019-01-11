import re

baseFile = open("11.txt", "r", encoding="utf‐8")
text = baseFile.read()

baseFile.close()

sentences = re.split(r' *[\.\?!][\'"\)\]]* *', text)

with open('111.txt', 'w', encoding="utf‐8") as file1:
    file1.write(''.join(filter(lambda sentence: re.match(r'^[A-Z].*[A-Z].*', sentence), sentences)))

with open('112.txt', 'w', encoding="utf‐8") as file2:
    file2.write(''.join(filter(lambda sentence: re.match(r'^.*(\w*[^aeiouAEIOU\W]){5}\w*', sentence), sentences)))
