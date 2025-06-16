# chapter4_exercise.py
import math

def factorial_recursive(n):
    return 1 if n <= 1 else n * factorial_recursive(n-1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

num = int(input("Enter a non-negative integer: "))
print(f"Recursive: {factorial_recursive(num)}")
print(f"Iterative: {factorial_iterative(num)}")