import re


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def get_latter():
    letter = str(input("Please, enter cyrillic letter :"))
    if len(letter) and has_cyrillic(letter):
        return letter
    print("Incorrect string, it must be a cyrillic latter")
    return get_latter()


def get_word(letter):
    word = str(input(f'Please, enter the word starts with "{letter}" latter'))
    if word[0] != letter:
        print(f'Incorrect word, it must starts with "{letter}" latter')
        return get_word(letter)
    return word


vocabulary = dict()

while True:
    valid_latter = get_latter()
    valid_word = get_word(valid_latter)
    words = vocabulary.get(valid_latter) or []
    words.append(valid_word)
    vocabulary.update({valid_latter: words})

    for item in vocabulary.keys():
        print('{0}: {1}'.format(item, ', '.join(vocabulary.get(item))))
