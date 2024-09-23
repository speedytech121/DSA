'''
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false
'''

def wordpattern(pattern, s):
    s=s.split(' ')
    pi,si=[],[]
    if len(pattern)!=len(s): return False

    for ch, word in zip(pattern, s):
        pi.append(pattern.index(ch))
        si.append(s.index(word))
    
    return True if pi==si else False

pattern="abba"
s="dog cat cat dog"
print(wordpattern(pattern,s))

pattern="abba"
s="dog cat cat fish"
print(wordpattern(pattern,s))