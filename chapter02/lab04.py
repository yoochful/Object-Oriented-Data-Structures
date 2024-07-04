# Chapter : 2 - item : 4 - nong saimai

# หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล

# เช่น

# hbd(65) = "saimai is just 21, in base 32!"

# hdb(21) = "saimai is just 21, in base 10!"

# hdb(8888) = "saimai is just 20, in base 4444!"

# def hbd(age):

#     ### Enter Your Code Here ###

# year = input("Enter year : ")

# print(hbd(int(year)))

# Testcase : #1
# Enter year : 555
# saimai is just 21, in base 277!

# Testcase : #2
# Enter year : 6
# saimai is just 20, in base 3!

# Testcase : #3
# Enter year : 320
# saimai is just 20, in base 160!

def hbd(year):
    base = year // 2  
    if year % 2 == 0:
        age = 20
    else:
        age = 21
    return f"saimai is just {age}, in base {base}!"

year = input("Enter year : ")
print(hbd(int(year)))
