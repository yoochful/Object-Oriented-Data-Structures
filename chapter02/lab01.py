# จงเขียน Overloading Function สำหรับ Calculator class โดยที่มีรูปแบบ Code ดังนี้ (สามารถเพิ่มพารามิเตอร์ได้)

# class Calculator :

#     ### Enter Your Code Here ###

#     def __add__(self):

#         ###Enter Your Code For Add Number###

#     def __sub__(self):

#         ###Enter Your Code For Sub Number### 

#     def __mul__(self):

#         ###Enter Your Code For Mul Number###

#     def __truediv__(self):

#         ###Enter Your Code For Div Number###

# x,y = input("Enter num1 y : ").split(",")

# x,y = Calculator(int(x)),Calculator(int(y))

# print(x+y,x-y,x*y,x/y,sep = "\n")

# Test case 1
# Enter num1 y : 5,5
# 10
# 0
# 25
# 1.0

# Test case 2
# Enter num1 y : 20,5
# 25
# 15
# 100
# 4.0

class Calculator :
    def __init__(self,num):
        self.num = num
        
    def __add__(self,out):
        return self.num + out.num

    def __sub__(self,out):

        return self.num - out.num
    def __mul__(self,out):

        return self.num * out.num
    def __truediv__(self,out):
        return self.num / out.num

x,y = input("Enter num1 num2 : ").split(",")

x,y = Calculator(int(x)),Calculator(int(y))

print(x+y,x-y,x*y,x/y,sep = "\n")