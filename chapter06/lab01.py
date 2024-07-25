# Chapter : 6 - item : 1 - Factorial
# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

# หา Factorial ของ input ที่รับมา โดยใช้ Recursive


# Testcase : #1 1
# Enter Number : 0
# 0! = 1

# Testcase : #2 2
# Enter Number : 1
# 1! = 1

# Testcase : #3 3
# Enter Number : 5
# 5! = 120

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter Number : "))
result = factorial(number)
print(f"{number}! = {result}")