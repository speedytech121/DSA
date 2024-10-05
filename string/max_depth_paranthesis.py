# find maximum nesting depth of paranthesis

def max_depth(s):
    stack=[]
    count=0
    for elem in s:
        if elem=='(':
            stack.append('(')
            templen=len(stack)
        elif elem==')':
            if count<templen:
                count=templen
            stack.pop()
    return count

s1="(1+(2*3)+((8)/4))+1"
s2="8*((1*(5+6))*(8/6))"
print(max_depth(s1))
print(max_depth(s2))