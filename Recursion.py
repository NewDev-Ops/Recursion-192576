print("This is recursion")

# Factorial numbering

print("\n")
print("Factorials")
def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n - 1)

result = Factorial(int(input('What number are we factorialing??(┬┬﹏┬┬):  ')))
print(f'Your answer is: {result}')


print("\n")
print("Fibonacci series")
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for numbers in range(12):
        print(f'{numbers}: {fibonacci(numbers)} ')
