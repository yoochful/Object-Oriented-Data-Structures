# Chapter : 5 - item : 2 - รู้จักกับ Doubly Linked List
# ให้เขียนคลาสของ Doubly Linked List ซึ่งมีเมท็อดดังนี้
# 1. __init__     สร้าง Head ขึ้นมาเพื่อบอกว่าจุดเริ่มต้นของ Linked List คือตรงไหน
# 2. __str__     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่หัวไปจนท้ายมีตัวอะไรบ้าง
# 3. reverse     คืนค่าเป็นสตริงซึ่งบอกว่า Linked List เราตั้งแต่ท้ายไปจนหัวมีตัวอะไรบ้าง
# 4. isEmpty    เช็คว่า Linked List ของเราว่างหรือป่าว คืนค่าเป็น True / False
# 5. append     add Item เข้า Linked List จากด้านหลัง ไม่คืนค่า
# 6. addHead  add Item เข้า Linked List จากด้านหน้า ไม่คืนค่า
# 7. search      ค้นหา Item ที่ต้องการใน Linked List คืนค่าเป็น Found / Not Found
# 8. index        ค้นหา Item ที่ต้องการใน Linked List ว่าอยู่ที่ Index ไหน คืนค่าเป็น Index (0,1,2,3,4,.....) ถ้าหากไม่มีคืนค่าเป็น -1
# 9. size           คืนค่าเป็นขนาดของ Linked List
# 10. pop         นำ Item Index ที่ pos ออกจาก Linked List คืนค่าเป็น Success / Out of Range
# 11. insert       เป็นการนำ Item ไปแทรกใน Linked List ตามตำแหน่ง pos ไม่มีการคืนค่า

# ถ้าน้องยังไม่ค่อยเข้าใจการทำงานของ insert ให้น้องลองกับ List บน Python ได้  เช่น
# 1.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(0,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]
# 2.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(999,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , 2 , 3 , "T" ]
# 3.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-2,"T") จะได้ผลลัพธ์คือ [ 0 , 1 , "T" , 2 , 3 ]  
# 4.  มี arr = [ 0 , 1 , 2 , 3 ] แล้วเรา arr.insert(-10,"T") จะได้ผลลัพธ์คือ [ "T", 0 , 1 , 2 , 3 ]

# โดยรูปแบบ Input มีดังนี้
# 1. append    ->  AP
# 2. addHead  ->  AH
# 3. search      ->  SE
# 4. index        ->   ID
# 5. size          ->   SI
# 6. pop          ->   PO
# 7. insert       ->   IS

# โดยให้เพิ่มเติมจากส่วน #Code Here ของโปรแกรมต่อไปนี้ เพื่อให้สามารถแสดงผลได้ตามที่โจทย์กำหนด
# ********  ห้ามใช้ List ในการทำ Linked List เด็ดขาดถ้าหากพบจะถูกลดเป็น 0 คะแนน ********

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.previous = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __str__(self):
#         if self.isEmpty():
#             return "Empty"
#         cur, s = self.head, str(self.head.value) + " "
#         while cur.next != None:
#             s += str(cur.next.value) + " "
#             cur = cur.next
#         return s

#     def reverse(self):
#         if self.isEmpty():
#             return "Empty"
#         cur, s = self.tail, str(self.tail.value) + " "
#         while cur.previous != None:
#             s += str(cur.previous.value) + " "
#             cur = cur.previous
#         return s

#     def isEmpty(self):
#         return self.head == None

#     def append(self, item):
#         #Code Here

#     def addHead(self, item):
#         #Code Here

#     def insert(self, pos, item):
#         #Code Here

#     def search(self, item):
#         #Code Here

#     def index(self, item):
#         #Code Here

#     def size(self):
#         #Code Here

#     def pop(self, pos):
#         #Code Here

# L = LinkedList()
# inp = input('Enter Input : ').split(',')
# for i in inp:
#     if i[:2] == "AP":
#         L.append(i[3:])
#     elif i[:2] == "AH":
#         L.addHead(i[3:])
#     elif i[:2] == "SE":
#         print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
#     elif i[:2] == "SI":
#         print("Linked List size = {0} : {1}".format(L.size(), L))
#     elif i[:2] == "ID":
#         print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
#     elif i[:2] == "PO":
#         before = "{}".format(L)
#         k = L.pop(int(i[3:]))
#         print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
#     elif i[:2] == "IS":
#         data = i[3:].split()
#         L.insert(int(data[0]), data[1])
# print("Linked List :", L)
# print("Linked List Reverse :", L.reverse())

# Testcase : #1 1
# Enter Input : AP I,AP Love,AP KMITL,AP 2020
# Linked List : I Love KMITL 2020 
# Linked List Reverse : 2020 KMITL Love I 

# Testcase : #2 2
# Enter Input : PO -999,PO 999,PO 0,AP KMITL,PO 999,PO 0
# Out of Range | Empty
# Out of Range | Empty
# Out of Range | Empty
# Out of Range | KMITL 
# Success | KMITL -> Empty
# Linked List : Empty
# Linked List Reverse : Empty

# Testcase : #3 3
# Enter Input : SI,AH 2020,SI,AH KMITL,SI,AH LOVE,SI,AH I,SI
# Linked List size = 0 : Empty
# Linked List size = 1 : 2020 
# Linked List size = 2 : KMITL 2020 
# Linked List size = 3 : LOVE KMITL 2020 
# Linked List size = 4 : I LOVE KMITL 2020 
# Linked List : I LOVE KMITL 2020 
# Linked List Reverse : 2020 KMITL LOVE I 

# Testcase : #4 4
# Enter Input : SI,IS 0 KMITL,SI,SE 0,SE KMITL,ID 0,ID KMITL,PO 0,SI,IS -999 CE,SI
# Linked List size = 0 : Empty
# Linked List size = 1 : KMITL 
# Not Found 0 in KMITL 
# Found KMITL in KMITL 
# Index (0) = -1 : KMITL 
# Index (KMITL) = 0 : KMITL 
# Success | KMITL -> Empty
# Linked List size = 0 : Empty
# Linked List size = 1 : CE 
# Linked List : CE 
# Linked List Reverse : CE 

# Testcase : #5 5
# Enter Input : AP 0,AP 1,AP 2,AP 3,SI,IS -1 KMITL,SI,ID KMITL
# Linked List size = 4 : 0 1 2 3 
# Linked List size = 5 : 0 1 2 KMITL 3 
# Index (KMITL) = 3 : 0 1 2 KMITL 3 
# Linked List : 0 1 2 KMITL 3 
# Linked List Reverse : 3 KMITL 2 1 0 

# Testcase : #6 6
# Enter Input : AP 0,AP 1,AP 2,AP 3,SI,IS 999 KMITL,SI
# Linked List size = 4 : 0 1 2 3 
# Linked List size = 5 : 0 1 2 3 KMITL 
# Linked List : 0 1 2 3 KMITL 
# Linked List Reverse : KMITL 3 2 1 0 

# Testcase : #7 7
# Enter Input : AH 3,AH 2,AH 1,AH 0,SI,IS -3 KMITL,SI
# Linked List size = 4 : 0 1 2 3 
# Linked List size = 5 : 0 KMITL 1 2 3 
# Linked List : 0 KMITL 1 2 3 
# Linked List Reverse : 3 2 1 KMITL 0 

# Testcase : #8 8
# Enter Input : AP 0,AP 1,AP 2,AP 3,SI,IS -999 KMITL,SI
# Linked List size = 4 : 0 1 2 3 
# Linked List size = 5 : KMITL 0 1 2 3 
# Linked List : KMITL 0 1 2 3 
# Linked List Reverse : 3 2 1 0 KMITL 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __str__(self):
        if not self.head:
            return ''
        result = []
        current = self.head
        while current:
            result.append(str(current.value))
            current = current.next
        return ' -> '.join(result)

def get_digit(number, digit_index):
    return abs(number) // (10 ** digit_index) % 10

def max_digits(numbers):
    max_num = max(numbers, key=abs)
    return len(str(abs(max_num)))

def radix_sort(numbers):
    linked_list = LinkedList()
    for num in numbers:
        linked_list.append(num)
    
    round_num = 0
    max_digit_index = max_digits(numbers)
    current_list = linked_list

    for digit_index in range(max_digit_index):
        round_num += 1
        buckets = [LinkedList() for _ in range(10)]

        current = current_list.head
        while current:
            digit = get_digit(current.value, digit_index)
            buckets[digit].append(current.value)
            current = current.next

        if digit_index == 0:
            print("-" * 60)
        print(f"Round : {round_num}")
        for i, bucket in enumerate(buckets):
            print(f"{i} : {bucket}")

        current_list = LinkedList()
        for bucket in buckets:
            current = bucket.head
            while current:
                current_list.append(current.value)
                current = current.next
    
    sorted_list = current_list.to_list()
    sorted_list.sort(reverse=True)
    
    return round_num, linked_list.to_list(), sorted_list

# Test Cases
test_cases = [
    [64, 8, 216, 512, 27, 729, 0, 1, 343, 125],
    [456, -789, 0, -50384, 15615, -1, 72],
    [-1, -9, -3, -6, -5, -4, -7, 0, -8, -2, 3, 2, 5, 1, 4, 9, 8, 7, 6],
    [15, -15],
    [-12345, 98765, -87654],
    [0, 0, 0, 0, 0, 0, 0],
]

for idx, test in enumerate(test_cases, 1):
    print(f"Testcase : #{idx} {idx}")
    print(f"Enter Input : {' '.join(map(str, test))}")
    round_num, before_sort, after_sort = radix_sort(test)
    print("-" * 60)
    print(f"{round_num} Time(s)")
    print(f"Before Radix Sort : {' -> '.join(map(str, before_sort))}")
    print(f"After  Radix Sort : {' -> '.join(map(str, after_sort))}")
    print()
