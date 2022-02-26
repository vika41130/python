# 1 1 2 3 5 8

# recursion
def getFibonaciN(nTh: int) -> int:
    if nTh == 1 or nTh == 2:
        return 1
    return getFibonaciN(nTh - 1) + getFibonaciN(nTh - 2)

nTh = int(input('Enter the N Th: '))

print(getFibonaciN(nTh))

def generateFibonaciListN(nTh: int) -> list[int]:
    temp: list[int] = [0] * nTh
    if nTh == 1:
        temp[0] = 1
    if nTh >= 2:
        temp[0] = 1
        temp[1] = 1
    for index in range(2, nTh):
        temp[index] = temp[index - 1] + temp[index - 2]
    return temp

nTh = int(input('Enter the N Th: '))

print(generateFibonaciListN(nTh))

    