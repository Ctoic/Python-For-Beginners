strng = input("Enter a string: ")
length = len(strng)

# method 1
for i in range(length):
    print(strng[length - i - 1], end = "")

# method 2
for i in range(length - 1, -1, -1):
    print(strng[i], end = "")

# method 3
print(strng[::-1])

# method 4
print("".join(reversed(strng)))

# method 5
print("".join(strng[length - i - 1] for i in range(length)))

# method 6
print("".join(strng[i] for i in range(length - 1, -1, -1)))

# method 7
print("".join(strng[i] for i in reversed(range(length))))

# method 8
print("".join(strng[i] for i in range(length))[::-1])




