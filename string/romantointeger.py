'''
1. Purpose:
The function converts a Roman numeral string into an integer by handling both individual symbols (like "I" = 1) and special subtractive combinations (like "IV" = 4, "IX" = 9).

2. Translation:
It uses a dictionary to map each Roman numeral character (I, V, X, etc.) to its corresponding integer value.

3. Handling Subtractive Pairs:
Before summing values, the function replaces subtractive pairs (like "IV" and "IX") with their equivalent additive forms (e.g., "IV" becomes "IIII"). This simplifies the process by converting everything into basic additions.

4. Summing:
After modifying the string, it loops through each character and adds up their corresponding values using the dictionary.

5. Result:
Finally, the function returns the total, which is the integer representation of the given Roman numeral. For instance, "VX" would return 15.
'''
def RomanToInteger(s):
    translation = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")

    num = 0
    for i in s:
        num += translation[i]
    return num


print(RomanToInteger("VX"))
