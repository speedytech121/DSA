def RemoveOutermost(s):
    count = 0
    final_result = []
    current = []

    for char in s:
        if char == '(':
            if count > 0:
                current.append(char)
            count += 1
        elif char == ')':
            count -= 1
            if count > 0:  
                current.append(char)
            if count == 0:
                final_result.append(''.join(current))
                current = []

    result_string = ''.join(final_result)
    print(result_string)


# practice1
def removeoutermost(s):
    count=0
    current=[]
    finalresult=[]

    for char in s:
        if char=='(':
            if count>0:
                current.append(char)
            count+=1
        elif char==')':
            count-=1
            if count>0:
                current.append(')')
            if count==0:
                finalresult.append(''.join(current))
                current=[]
            # count-=1
            
    final_result=''.join(finalresult)
    print(final_result)

s = '((()))(())'
removeoutermost(s)
