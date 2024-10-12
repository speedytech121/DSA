def countGoodNumbers(n):
    num_of_even_index = (n+1)//2
    num_of_odd_index = n//2
    even_num_count = 5
    prime_num_count = 4
    MOD = 10 ** 9 + 7
    total = pow(even_num_count, num_of_even_index, MOD) * pow(prime_num_count, num_of_odd_index, MOD) % MOD
    return total

print(countGoodNumbers(1))
print(countGoodNumbers(4))
print(countGoodNumbers(50))