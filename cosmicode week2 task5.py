def max_subarray_sum(numbers):
    if not numbers:  # Edge case: empty list
        return 0
    
    max_current = max_global = numbers[0]  # Initialize with first element
    
    for num in numbers[1:]:  # Start from the second element
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    
    return max_global

# Get input from the user
input_str = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(float, input_str.split()))  # Convert input string to list of numbers

# Calculate and print the result
result = max_subarray_sum(numbers)
print(f"The maximum subarray sum is: {result}")