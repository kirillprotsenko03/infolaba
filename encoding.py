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
    letters_code = []
    result = []
    temp1 = []
    temp2 = []
    for letter in word:
        letters_code.append(ord(letter))

    for i in range(len(letters_code)):
        if i % 2 == 1:
            temp1.append(permutation(convert(letters_code[i] + 1306, 10, 2), i + 1))
        else:
            temp1.append(permutation(convert(letters_code[i] + 1306, 10, 3), i + 1))

    for i in range(len(temp1)):
        temp2.append(int(''.join(map(str, temp1[i]))))

    for i in range(len(temp1)):
        if i % 2 == 1:
            temp1[i] = convert(temp2[i], 2, 10)
        else:
            temp1[i] = convert(temp2[i], 3, 10)

    for i in range(len(temp1)):
        result.append(int(''.join(map(str, temp1[i]))) - 1306)
        result.append('.')

    result = ''.join(map(str, result))

    return result


def decoding(string):
    letter = []
    letter_num = []
    temp1 = []
    temp2 = []
    letter_num_temp = (string.split('.'))
    letter_num_temp.remove(letter_num_temp[len(letter_num_temp) - 1])

    for i in range(len(letter_num_temp)):
        letter_num.append(int(letter_num_temp[i]))

    for i in range(len(letter_num)):
        letter_num[i] = letter_num[i] + 1306
        if i % 2 == 1:
            temp1.append(permutation(convert(letter_num[i], 10, 2), i + 1))
        else:
            temp1.append(permutation(convert(letter_num[i], 10, 3), i + 1))

    for i in range(len(temp1)):
        temp1[i] = int(''.join(map(str, temp1[i])))

    for i in range(len(temp1)):
        if i % 2 == 1:
            temp2.append(convert(temp1[i], 2, 10))
        else:
            temp2.append(convert(temp1[i], 3, 10))

    for i in range(len(temp1)):
        temp2[i] = int(''.join(map(str, temp2[i]))) - 1306
        letter.append(chr(temp2[i]))

    result = ''.join(map(str, letter))

    return result


print(ders_crypt("aaaa"))