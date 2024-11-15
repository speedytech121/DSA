def longest_palindromic_substring(s):
    max_substring = s[0]
    for i in range(len(s)-1):
        ss = s[i]
        for j in range(i+1, len(s)):
            ss += s[j]
            if ss == ss[::-1] and len(ss)>len(max_substring):
                max_substring = ss
    return max_substring