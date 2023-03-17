num = int(input("Enter a number: "))

# initialize first two terms of the series
a, b = 0, 1
fib_sum = 0

print("Fibonacci series up to", num, ":")
while a <= num:
    print(a, end=" ")
    fib_sum += a
    a, b = b, a+b
    
print("\nSum of the Fibonacci series up to", num, ":", fib_sum)
