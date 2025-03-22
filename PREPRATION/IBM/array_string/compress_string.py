# Implement a function to perform basic string compression.


def compress_string(s):
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1]+str(count))
            count = 1
    # add last character and count
    compressed.append(s[-1]+str(count))
    compressed_str = "".join(compressed)

    return compressed_str if len(compressed_str) < len(s) else s




# Test cases
print(compress_string("aabcccccaaa"))  # Expected: "a2b1c5a3"
print(compress_string("abcd"))         # Expected: "abcd" (since compression is longer)
print(compress_string("aaabb"))        # Expected: "a3b2"
print(compress_string("a"))            # Expected: "a"
print(compress_string(""))             # Expected: ""