
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b


terms = int(input("Enter number of terms: "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci(terms)
