# Chapter : 2 - item : 3 - Odd And Even
# ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการหาตำแหน่ง คู่ กับ คี่ จาก List และ String

# def odd_even(type, data, mode):
#     //Code Here

# โดยที่รูปแบบการรับ Input ตำแหน่งแรกจะเป็นตัวบอกว่าเป็น String หรือ List ถ้าใส่ S = String ถ้าใส่ L = List

# Input ตำแหน่งที่สองเป็นค่าใน String หรือ List ที่นำเข้ามา

# Input ตำแหน่งที่สามเป็นการบอกว่าจะแสดงตำแหน่งคู่หรือคี่ ถ้าใส่ Odd = คี่ ถ้าใส่ Even = คู่

# Testcase : #1 
# *** Odd Even ***
# Enter Input : S,ABCDEF,Odd
# ACE

# Testcase : #2 
# *** Odd Even ***
# Enter Input : L,1 2 3 4 5,Even
# ['2', '4']

# Testcase : #3 
# *** Odd Even ***
# Enter Input : S,ABC12345DEF,Even
# B135E

# Testcase : #4 
# *** Odd Even ***
# Enter Input : S,ABC12345DEF,Odd
# AC24DF

# Testcase : #5 
# *** Odd Even ***
# Enter Input : L,ABC12345DEF,Even
# []

# Testcase : #6 
# *** Odd Even ***
# Enter Input : L,ABC12345DEF,Odd
# ['ABC12345DEF']

# Testcase : #7 
# *** Odd Even ***
# Enter Input : L,A B C 1 2 3 4 5 D E F,Odd
# ['A', 'C', '2', '4', 'D', 'F']

# Testcase : #8 
# *** Odd Even ***
# Enter Input : L,A B C 1 2 3 4 5 D E F,Even
# ['B', '1', '3', '5', 'E']


def odd_even(type, data, mode):
    result = []
    if type == 'S':
        if mode == 'Odd':
            result = data[::2]
        elif mode == 'Even':
            result = data[1::2]
    elif type == 'L':
        data = data.split()
        if mode == 'Odd':
            result = data[::2]
        elif mode == 'Even':
            result = data[1::2]
    return ''.join(result) if type == 'S' else result

print("*** Odd Even ***")
type, data, mode = input("Enter Input : ").split(',')
print(odd_even(type, data, mode))


