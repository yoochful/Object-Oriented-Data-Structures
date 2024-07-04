# Chapter : 1 - item : 4 - function

# จงเขียนฟังก์ชัน 
# def odd_list(alist):
# โดยมีการทำงานดังนี้
#      # คืนlist ที่มีค่าเหมือนalist แต่มีเฉพาะตัวที่เป็นจำนวนคี่
#      # เช่นalist = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]

# โดยแก้ไขจากส่วนของคำสั่งต่อไปนี้


# def odd_list(al):
#     # เติมส่วนของคำสั่ง


# print(" ***Function Odd List***")
# ls = [int(e) for e in input("Enter list numbers : ").split()]
# print(ls)
# opls = odd_list(ls)
# print("Input list : ", ls, "\nOutput list : ", opls)


# แล้วแสดงผลดังตัวอย่าง

# Test case 1
#  ***Function Odd List***
# Enter list numbers : 1 2 3 4 5 6 7 8 9 10
# Input list :  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# Output list :  [1, 3, 5, 7, 9]

# Test case 2
#  ***Function Odd List***
# Enter list numbers : 10 11 13 24 25
# Input list :  [10, 11, 13, 24, 25] 
# Output list :  [11, 13, 25]

# Test case 3
#  ***Function Odd List***
# Enter list numbers : 1502 3203 23209 20309 922 239 2332 20 2920 3 2094
# Input list :  [1502, 3203, 23209, 20309, 922, 239, 2332, 20, 2920, 3, 2094] 
# Output list :  [3203, 23209, 20309, 239, 3]

def odd_list(al):
    for i in al :
        if i % 2 != 0 :
            yield i

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = list(odd_list(ls))
print("Input list : ", ls, "\nOutput list : ", opls)

