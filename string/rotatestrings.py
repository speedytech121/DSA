def rotateString(s, goal):
    s=list(s)
    for i in range(len(s)):
        ch=s.pop(0)
        s.append(ch)
        if(''.join(s)==goal):
            return True
    return False

s = "abcde"
goal = "cdeab"
print(rotateString(s,goal))

s = "abcde"
goal = "caeab"
print(rotateString(s,goal))