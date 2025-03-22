# determine if a string has all unique characters.

def checkUnique(s):
    # unique= [] list will results O(n^2) time complexity, use set(), set allows  O(1) average time complexity for membership checks.
    unique = set()

    for c in s:
        if c in unique:
            return False
        unique.add(c)
    return True


s = "abcd"
print(checkUnique(s))

s = "abcdc"
print(checkUnique(s))

s = "abcda"
print(checkUnique(s))

s = "abc"
print(checkUnique(s))
