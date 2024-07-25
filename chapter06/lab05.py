# Chapter : 6 - item : 5 - วาดภาพแสนสุข

# เขียนโปรแกรมที่แสดงผลดังตัวอย่าง

# ****ห้ามใช้คำสั่ง for, while, do while*****

# หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว

# def staircase(n):
#     #code here

# print(staircase(int(input("Enter Input : "))))

# Testcase : #1
# Enter Input : 3
# __#
# _##
# ###

# Testcase : #2
# Enter Input : 7
# ______#
# _____##
# ____###
# ___####
# __#####
# _######
# #######

# Testcase : #3
# Enter Input : -8
# ########
# _#######
# __######
# ___#####
# ____####
# _____###
# ______##
# _______#

# Testcase : #4
# Enter Input : 2
# _#
# ##

# Testcase : #5
# Enter Input : 0
# Not Draw!

def staircase(n):
    if n == 0:
        return "Not Draw!"
    if n < 0:
        size = -n  
    else:
        size = n  
    print_stair(size, n)
    return ""  

def print_stair(size, n):
    if n > 0:
        str = "_"*(size-n) + "#"*n  
        print_stair(size, n-1)  # บรรทัดถัดไปลดค่า n ลง 1
        print(str) 
    elif n < 0:
        str = "_"*(size+n) + "#"*-n  
        print(str) 
        print_stair(size, n+1)  # บรรทัดถัดไปเพิ่มค่า n ขึ้น 1

print(staircase(int(input("Enter Input : "))))
