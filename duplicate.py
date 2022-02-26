a = [1, 2, 3, 2, 5, 7, 6, 5, 6, 9]

# temp list
def remove_duplicate(a: list[int]):
    b: list[int] = []
    for value in a:
        if value not in b:
            b.append(value)
    return b

# print(remove_duplicate(a))

# set
def remove_duplicate_v2(a: list[int]):
    return list(set(a))

print(remove_duplicate_v2(a))