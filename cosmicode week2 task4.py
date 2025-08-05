def prime_factors(n):
    """Find all prime factors of a number"""
    factors = []
    # Handle 2 separately
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # Check odd divisors up to sqrt(n)
    i = 3
    max_factor = n**0.5
    while i <= max_factor:
        while n % i == 0:
            factors.append(i)
            n = n // i
            max_factor = n**0.5
        i += 2
    if n > 1:
        factors.append(n)
    return factors

# Example usage:
number = 315
print(f"Prime factors of {number}: {prime_factors(number)}")