# Chapter : 6 - item : 3 - GCD
# เขียนโปรแกรมสำหรับหา หรม. ของเลข 2 ตัว

# ****ห้ามใช้คำสั่ง len, for, while, do while หรือ *****

# หมายเหตุ ฟังก์ชันต้องมี parameter แค่เพียง 2 ตัว

# บทนิยาม

# ตัวหารร่วมมาก หรือ ห.ร.ม. (อังกฤษ: greatest common divisor: gcd) ของจำนวนเต็มสองจำนวนซึ่งไม่เป็นศูนย์พร้อมกัน คือจำนวนเต็มที่มากที่สุดที่หารทั้งสองจำนวนลงตัว

# Testcase : #1
# Enter Input : 8 4
# The gcd of 8 and 4 is : 4

# Testcase : #2
# Enter Input : 10 20
# The gcd of 20 and 10 is : 10

# Testcase : #3
# Enter Input : 12 18
# The gcd of 18 and 12 is : 6

# Testcase : #4
# Enter Input : 9 7
# The gcd of 9 and 7 is : 1

# Testcase : #5
# Enter Input : 0 5
# The gcd of 5 and 0 is : 5

# Testcase : #6
# Enter Input : -6 9
# The gcd of 9 and -6 is : 3

# Testcase : #7
# Enter Input : -24 -36
# The gcd of -24 and -36 is : 12

# Testcase : #8
# Enter Input : 0 0
# Error! must be not all zero.

# Testcase : #9
# Enter Input : -11 -45
# The gcd of -11 and -45 is : 1

def gcd(x, y):
    if x == 0 and y == 0:
        return None
    if y == 0:
        return abs(x)  #ถ้า y เป็น 0 รีเทิร์น |x| เพราะ หรม. คือ 0 หรือ x (ตัวมันเองของอีกค่า)
    return gcd(y, x % y)  #เรียกตัวเองซ้ำด้วย y และ x % y 

    
x, y = map(int, input("Enter Input : ").split())

result = gcd(x, y)
if x < y:
    x, y = y, x
    
if result is None:
    print("Error! must be not all zero.")
else:
    print(f"The gcd of {x} and {y} is : {result}")


