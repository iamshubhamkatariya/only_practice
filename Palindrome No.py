# Palindrome No.

num = int(input("Enter a number: "))
original = num 
rev = 0

while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if rev == original:
    print(original , "is a pailndrome No. ")
else:
    print(original, "is NOT a pailndrome")