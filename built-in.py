'''
    not duplicate elements
'''
from collections import Counter

test = 'geekforgeek'
dict_fre = Counter(test)
not_duplicate_set = set(dict_fre.keys())

print(dict_fre)
print(not_duplicate_set)