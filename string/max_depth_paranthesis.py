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

# optimized solution
def optimized(s):
    max_depth=0
    current_depth=0
    for e in s:
        if e=='(':
            current_depth+=1
            max_depth=max(max_depth,current_depth)
        elif e==')':
            current_depth-=1
    return max_depth

s1="(1+(2*3)+((8)/4))+1"
s2="8*((1*(5+6))*(8/6))"

print(max_depth(s1))
print(max_depth(s2))

print(optimized(s1))
print(optimized(s2))