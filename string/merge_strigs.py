def merge_strings(word1, word2):
    n=max(len(word1),len(word2))
    s=""
    for i in range(n):
        try:
            s+=word1[i]
        except:
            pass
        try:
            s+=word2[i]
        except:
            pass
    print(s)

merge_strings("abc","defgh")
