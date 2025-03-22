class NumberToWords:
    def __init__(self):
        self.num_to_19 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                          "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        if num == 0:
            return "Zero"

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return self.num_to_19[n] + " "
            elif n < 100:
                return self.tens[n // 10] + " " + helper(n % 10)
            else:
                return self.num_to_19[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000
            i += 1

        return res.strip()

# Test Cases
converter = NumberToWords()
print(converter.numberToWords(123))       # "One Hundred Twenty Three"
print(converter.numberToWords(5080))      # "Five Thousand Eighty"
print(converter.numberToWords(1000010))   # "One Million Ten"
print(converter.numberToWords(0))         # "Zero"
print(converter.numberToWords(123456789)) # "One Hundred Twenty Three Million Four Hundred Fifty Six Thousand Seven Hundred Eighty Nine"
