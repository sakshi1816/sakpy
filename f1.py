def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


num = int(input("Enter the number of terms: "))
if num <= 0:
    print("Please enter a positive integer")
else:
    fibonacci(num)
