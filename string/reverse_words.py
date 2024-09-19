# reverse words in given string
import re

def Reverse_Words(s):
    s=s.strip()
    li=re.split(r'\s+',s)
    res_li=[]
    length=len(li)-1

    while length>=0:
        res_li.append(li[length])
        length-=1
    res_li=" ".join(res_li)
    print(res_li)

# practice1
def reversew(s):
    res=[]
    s=s.strip()
    data=re.split(r'\s+',s)
    length=len(data)-1
    while(length>=0):
        res.append(data[length])
        length-=1
    print(' '.join(res))

reversew(" this    is an amazing program ")