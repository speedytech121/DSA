# important medium level question


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        taken = {chr(i): False for i in range(ord('a'), ord('z') + 1)}
        lastindex = {chr(i): None for i in range(ord('a'), ord('z') + 1)}

        # Populate the last occurrence index for each character
        for i in range(n):
            ch = s[i]
            lastindex[ch] = i  # No need to use - 'a'

        result = []

        for i in range(n):
            ch = s[i]
            if taken[ch]:  # Use character directly as the key
                continue

            # Remove characters from the result if they are lexicographically larger
            # and still appear later in the string
            while result and result[-1] > ch and lastindex[result[-1]] > i:
                taken[result.pop()] = False  # Remove from result and mark as not taken

            result.append(ch)  # Add the current character to the result
            taken[ch] = True   # Mark as taken

        return ''.join(result)  # Convert the result list to a string

obj = Solution()
print(obj.removeDuplicateLetters('bcabc'))
print(obj.removeDuplicateLetters('cbacdcbc'))