# longest substring without repeating character
def longest_substring(s):
    temp_arr = []
    length = 0
    maxlength = 0
    for j in range(len(s)):
        while s[j] in temp_arr:
            temp_arr.pop(0)
            length -= 1
        temp_arr.append(s[j])
        length+=1
        maxlength = max(maxlength, length)
    return maxlength

string = "abccdef"
string1 = "abcabcbb" 
print(longest_substring(string))
print(longest_substring(string1))
