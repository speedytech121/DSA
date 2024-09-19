def longestCommonPrefix(strs):
        if not strs:
            return ""

        shortword = min(strs, key=len)

        for i in range(len(shortword)):
            for word in strs:
                if word[i] != shortword[i]:
                    return shortword[:i]

        return shortword

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))