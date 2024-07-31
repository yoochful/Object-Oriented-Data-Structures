# def pantip(k, n, arr, path):
    # Code Here
    # Chapter : 6 - item : 4 - ไปเที่ยวแบบชาว Pantip
# ****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 ) ******

# หลังจากที่กฤษฎาสอบมิดเทอมเสร็จ กำลังเดินทางกลับบ้านก็ได้หยิบโทรศัพท์ขึ้นมาเช็คข่าวสารต่างๆ แต่ก็ต้องสะดุดสิ่งที่เพื่อนของกฤษฎานั้นแชร์มาให้ นั่นคือกระทู้ที่มีหัวข้อว่า "ทริปไปเที่ยวโดยใช้ตังน้อยที่สุด" by Pantip กฤษฎาก็ได้เข้ากระทู้ไปอ่านจึงได้สะดุดกับบางประโยคของกระทู้นี้  นั่นคือการคำนวณว่าถ้าหากเรามีเงิน k บาท เราสามารถซื้อของให้เงินหมดพอดี (ไม่เหลือไม่ขาด) ได้หรือไม่ ถ้าได้จะได้สินค้าราคาเท่าใดบ้าง (หาทุกค่าที่ซื้อได้)  ถึงแม้ว่าของจะมีราคาเท่ากันก็ถือว่าเป็นของคนละชิ้นอยู่ดี  กฤษฎาจึงได้อยากไหว้วานน้องๆปีสอง วิศวกรรมคอมพิวเตอร์ ในการช่วยเขียนโปรแกรมแบบ Recursive ในการช่วยหาว่ากฤษฎาจะซื้อของได้ทั้งหมดกี่แบบและแต่ละแบบมีราคาของเท่าไหร่บ้าง

# ****** รายละเอียด Input ******
# โดย Input จะแบ่งเป้นทั้งหมด 2 ฝั่ง ได้แก่   ซ้าย : จำนวนเงินที่กฤษฎามี   |    ขวา : ราคาของสินค้าแต่ละชิ้น

# ****** Output ******
# รับประกันว่ากฤษฎาจะซื้อของได้อย่างน้อย 1 pattern

# def pantip(k, n, arr, path):
#     # Code Here

# inp = input('Enter Input (Money, Product) : ').split('/')
# arr = [int(i) for i in inp[1].split()]
# pattern = pantip(int(inp[0]), 0, arr, [])
# print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))

# Testcase : #1 1
# Enter Input (Money, Product) : 20/20 10 5 5 3 2 20 10
# 20
# 10 5 5
# 10 5 3 2
# 10 5 3 2
# 10 10
# 5 5 10
# 5 3 2 10
# 5 3 2 10
# 20
# Krisada can purchase Product: [20, 10, 5, 5, 3, 2, 20, 10] with: 20 Baht | 9 Pattern

# Testcase : #2 2
# Enter Input (Money, Product) : 3/3 1 1 4 1 2 2 3
# 3
# 1 1 1
# 1 2
# 1 2
# 1 2
# 1 2
# 1 2
# 1 2
# 3
# Krisada can purchase Product: [3, 1, 1, 4, 1, 2, 2, 3] with: 3 Baht | 9 Pattern

# Testcase : #3 3
# Enter Input (Money, Product) : 3/5 10 9 1 28 9 2 12 1 98 723 3
# 1 2
# 2 1
# 3
# Krisada can purchase Product: [5, 10, 9, 1, 28, 9, 2, 12, 1, 98, 723, 3] with: 3 Baht | 3 Pattern

# Testcase : #4 4
# Enter Input (Money, Product) : 99/216 67 59602 20 523 5 2545 2 97 99 32 515
# 67 32
# 2 97
# 99
# Krisada can purchase Product: [216, 67, 59602, 20, 523, 5, 2545, 2, 97, 99, 32, 515] with: 99 Baht | 3 Pattern

def pantip(k, n, arr, path):
    # Code Here
    if k == 0:  #พบชุดของเลขที่รวมกันแล้วได้ผลลัพธ์เท่ากับ k (คือ 0) print เลขที่เป็นผลลัพธ์ใน path แล้วก็คืนค่า 1
        print(*path, " ")
        return True
    elif n == len(arr):  #ไปถึงตัวสุดท้ายของ arr สร้างชุดที่ต้องการไม่ได้ คืนค่า 0
        return False

    size = pantip(k - arr[n], n + 1, arr, path + [arr[n]]) #ลดค่า k ลงด้วยค่า arr[n] แล้วเพิ่มเลขที่ n ไปยัง path (รวมเลขที่ n เข้าไปในชุด)
    size2 = pantip(k, n + 1, arr, path)
    
    return size + size2


input = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in input[1].split()]
pattern = pantip(int(input[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, input[0], pattern))