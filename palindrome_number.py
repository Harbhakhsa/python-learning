num = 1331
originalnum = 1331
rev = 0
while num != 0:
    digit = num%10
    rev = rev*10 + digit
    num = num//10
if rev == originalnum:
    print("is a palindrome")
else:
    print("is not a palindrome")