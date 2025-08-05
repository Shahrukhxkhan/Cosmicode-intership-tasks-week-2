def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def list_primes_up_to(n):
    """List all prime numbers up to n"""
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Get input from user
try:
    number = int(input("Enter a positive integer: "))
    if number < 1:
        print("Please enter a positive integer greater than 0.")
    else:
        print(f"Is {number} prime? {is_prime(number)}")
        print(f"Primes up to {number}: {list_primes_up_to(number)}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")