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


s="rteee"
frequencysort(s)