def frequencysort(s):
    d={}
    for i in s:
        if i not in d.keys():
            d[i]=1
        else:
            d[i]+=1

    sorted_dict=dict(sorted(d.items(), key=lambda item:item[1], reverse=True))
    s1=""
    for key, value in sorted_dict.items():
        for i in range(value):
            s1+=key

    print(s1)

# optimized version
def frequencysort1(s):
    d={}
    s1=""
    for e in list(s):
        if e in d.keys():
            d[e]+=1
        else:
            d[e]=1
    li=sorted(d.items(), key=lambda item:item[1], reverse=True)

    for ele in li:
        s1+=ele[0]*ele[1]
    print(s1)

s="Aabb"
frequencysort1(s)