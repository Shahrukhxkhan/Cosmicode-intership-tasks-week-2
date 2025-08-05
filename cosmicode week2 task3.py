def gcd(a, b):
    """Calculate greatest common divisor using Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Calculate least common multiple"""
    return a * b // gcd(a, b)

# Get input from user
try:
    num1 = int(input("Enter first positive integer: "))
    num2 = int(input("Enter second positive integer: "))
    
    if num1 <= 0 or num2 <= 0:
        print("Please enter positive integers greater than 0.")
    else:
        print(f"GCD of {num1} and {num2}: {gcd(num1, num2)}")
        print(f"LCM of {num1} and {num2}: {lcm(num1, num2)}")
except ValueError:
    print("Invalid input. Please enter valid integers.")