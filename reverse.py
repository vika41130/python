
# reverse word
def reverse_word(value: str) -> str:
    temp = []
    for i in range(1, len(value) + 1):
        temp.append(value[-i])
    return ''.join(temp)

# print(reverse_word('abcdef'))


# reverse sentence
# My name is Michele -> Michele is name My
def reverse_sentence(value: str) -> str:
    temp1 = []
    temp2 = []
    for i in range(0, len(value)):
        if value[i] != ' ':
            temp1.append(value[i])
        if value[i] == ' ' or i == len(value) - 1:
            temp2.insert(0, ''.join(temp1))
            temp1.clear()
    return ' '.join(temp2)

# print(reverse_sentence('My name is Michele'))

# short
def reverse_sentence_short(value: str) -> str:
    return ' '.join(value.split()[::-1])

print(reverse_sentence_short('My name is Michele'))