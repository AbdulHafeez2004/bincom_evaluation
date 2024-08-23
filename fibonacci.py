

def fibonacci_sum(n):
    a, b = 0, 1
    total_sum = 0
    for no in range(n):
        total_sum += a
        a, b = b, a + b
    return total_sum

# Number of Fibonacci terms to sum
n = 50


result = fibonacci_sum(n)
print(f"The sum of the first {n} Fibonacci numbers is: {result}")
