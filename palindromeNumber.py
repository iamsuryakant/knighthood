x = int(input("enter a number::"))
cpy = x
rev = 0
while (x > 0):
    rev = rev*10+(x % 10)
    x = int(x/10)
if rev == cpy:
    print("palindrome")
else:
    print("not palindrome")
