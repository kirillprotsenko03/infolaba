ALPHABET = {'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ж': 7, 'З': 8, 'И': 9, 'Й': 10, 'К': 11, 'Л': 12, 'М': 13,
            'Н': 14, 'О': 15, 'П': 16, 'Р': 17, 'С': 18, 'Т': 19, 'У': 20, 'Ф': 21, 'Х': 22, 'Ц': 23, 'Ч': 24, 'Ш': 25,
            'Щ': 26, 'Ъ': 27, 'Ы': 28, 'Ь': 29, 'Э': 30, 'Ю': 31, 'Я': 32}

WARNING_MESSAGE = "пожалуйста, введите слово на РУССКОМ языке без пробелов"


def convert(number, old_base, new_base):
    number = str(number)
    amount = 0
    res = []
    for i in range(len(number)):
        amount += int(number[i]) * (old_base ** (len(number) - i - 1))
    while amount:
        res.append(amount % new_base)
        amount //= new_base
    return res[::-1]


def permutation(number, position):
    key = 1
    for i in range(1, len(number), 2 * position):
        for j in range(i, i + position):
            if i + 2 * position >= len(number):
                key = 0
                break
            number[j], number[j + position] = number[j + position], number[j]
        if i + 2 * position >= len(number) or key == 0:
            break
    return number


def ders_crypt(word):
    word = word.upper()
    letters_position = []
    result = []
    temp1 = []
    temp2 = []
    for letter in word:
        try:
            letters_position.append(ALPHABET[letter])
        except KeyError:
            return WARNING_MESSAGE

    for i in range(len(letters_position)):
        if letters_position[i] % 2 == 0:
            temp1.append(permutation(convert(letters_position[i] + 1306, 10, 2), i + 1))
        else:
            temp1.append(permutation(convert(letters_position[i] + 1306, 10, 3), i + 1))

    for i in range(len(temp1)):
        temp2.append(int(''.join(map(str, temp1[i]))))

    for i in range(len(temp1)):
        if letters_position[i] % 2 == 0:
            temp1[i] = convert(temp2[i], 2, 10)
        else:
            temp1[i] = convert(temp2[i], 3, 10)

    for i in range(len(temp1)):
        result.append(int(''.join(map(str, temp1[i]))) - 1306)

    result = ''.join(map(str, result))
    return result
