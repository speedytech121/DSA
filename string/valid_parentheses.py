# check the valid parentheses

def valid_parentheses(s):
    hashmap = {'}':'{',')':'(',']':'['}
    stack=[]
    for elem in s:
        if elem not in hashmap.keys():
            stack.append(elem)
        elif stack and stack[-1]==hashmap[elem]:
            stack.pop()
    return False if stack else True

print(valid_parentheses('({[]})'))
print(valid_parentheses('({[)})'))
print(valid_parentheses('('))