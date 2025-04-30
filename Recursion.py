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

#for numbers in range(int(input("Which number are you fibing??: "))):
#       print(f'{numbers}: {fibonacci(numbers)} ')

#
# A function is independent of an object/variable but a method tends to depend on one
fcache = {} #dictionary
def fib(n):
    if n in fcache:
        return fcache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n>2:
        value = fib(n-1)+fib(n-2)

    fcache[n] = value
    return value

for n in range(1, int(input("What value is your maximum: "))):
        print(f"{fib(n)}\n")
