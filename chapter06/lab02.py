# Chapter : 6 - item : 2 - Palindrome
# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# เขียน Recursive เพื่อหาว่า String ที่รับเข้ามาเป็น Palindrome หรือไม่

# Testcase : #1 1
# Enter Input : abba
# 'abba' is palindrome

# Testcase : #2 2
# Enter Input : abgba
# 'abgba' is palindrome

# Testcase : #3 3
# Enter Input : abcdefkgfedfe
# 'abcdefkgfedfe' is not palindrome

def Palindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    return Palindrome(s[1:-1])

input = input("Enter Input : ")
result = Palindrome(input)
if result:
    print(f"'{input}' is palindrome")
else:
    print(f"'{input}' is not palindrome")

