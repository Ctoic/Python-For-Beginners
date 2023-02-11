# checking ehweather a string is a palindrome or not
check_palindrome = input("Enter a string: ")
length = len(check_palindrome)
for i in range(length):
    if check_palindrome[i] != check_palindrome[length - i - 1]:
        print("Not a palindrome")
        break
else:
    print("Palindrome")

def check_palindrome(string):
    length = len(string)
    for i in range(length):
        if string[i] != string[length - i - 1]:
            return False
    return True

print(check_palindrome("madam"))
print(check_palindrome("madam1"))