
s = input("Enter a string: ")
res = ""
for ch in s:
    res = ch+res
if res == s:
    print("Valid Palindrome")
else:
    print("Not a palindrome")
