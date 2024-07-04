# Chapter : 2 - item : 5 - funString

# จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้

# 1. หาความยาวของ String

# 2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)

# 3. Reverse String (ห้ามใช้คำสั่ง reversed)

# 4. ลบตัวอักษรที่ปรากฏมาก่อนใน String



# class funString():

#     def __init__(self,string = ""):

#         ### Enter Your Code Here ###

#     def __str__(self):

#         ### Enter Your Code Here ###

#     def size(self) :

#         ### Enter Your Code Here ###

#     def changeSize(self):

#         ### Enter Your Code Here ###

#     def reverse(self):

#         ### Enter Your Code Here ###

#     def deleteSame(self):

#        ### Enter Your Code Here ###


# str1,str2 = input("Enter String and Number of Function : ").split()

# res = funString(str1)

# if str2 == "1" :    print(res.size())

# elif str2 == "2":  print(res.changeSize())

# elif str2 == "3" : print(res.reverse())

# elif str2 == "4" : print(res.deleteSame())

# Test case 1
# Enter String and Number of Function : helloce 1
# 7

# Test case 2
# Enter String and Number of Function : aAaBbBccCDddd 2
# AaAbBbCCcdDDD

# Test case 3
# Enter String and Number of Function : IloveKMITL 3
# LTIMKevolI

# Test case 4
# Enter String and Number of Function : BananaBoat 4
# Banot

class funString():
    def __init__(self, string=""):
        self.string = string

    def __str__(self):
        return self.string

    def size(self):
        return len(self.string)

    def changeSize(self):
        result = []
        for char in self.string:
            if 'a' <= char <= 'z':
                result.append(chr(ord(char) - 32))
            elif 'A' <= char <= 'Z':
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return ''.join(result)

    def reverse(self):
        return self.string[::-1]

    def deleteSame(self):
        result = []
        seen_chars = set()
        for char in self.string:
            if char not in seen_chars:
                result.append(char)
                seen_chars.add(char)
        return ''.join(result)

str1, str2 = input("Enter String and Number of Function : ").split()
res = funString(str1)

if str2 == "1":
    print(res.size())
elif str2 == "2":
    print(res.changeSize())
elif str2 == "3":
    print(res.reverse())
elif str2 == "4":
    print(res.deleteSame())
