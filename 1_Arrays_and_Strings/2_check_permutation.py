from collections import defaultdict

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = defaultdict(int)
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True

result = check_permutation('abcd', 'dacb')
print(result)
result = check_permutation('abcd', 'dace')
print(result)
