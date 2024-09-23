'''
Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true
'''

def isomorphic(s,t):
    if len(s) != len(t):
        return False
    d = {}
    for i in range(len(s)):
        if s[i] in d and  d[s[i]] != t[i]:
            return False
        else:
            d[s[i]] = t[i]
    return True

s = "egg"
t = "add"
print(isomorphic(s,t))

s = "paper"
t = "title"
print(isomorphic(s,t))


s = "foo"
t = "bar"
print(isomorphic(s,t))
