def is_prime_recursive(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor + 1)

print(is_prime_recursive(7))
print(is_prime_recursive(12))
