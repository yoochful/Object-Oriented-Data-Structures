# Chapter : 5 - item : 5 - Radix Sort (มากไปน้อย)
# ให้น้องๆใช้ Linked List (เขียนเป็น class)  ในการทำ Radix Sort  (มีอยู่ในสไลด์เรียน 2 หน้าสุดท้าย)  ในรูปแบบมากไปน้อย

# โดยผลลัพธ์ให้ออกมาเป็นการทำ Radix Sort แบบจำนวนรอบน้อยที่สุด และแสดงผลในแต่ละรอบว่าได้ผลลัพธ์เป็นอย่างไร  3 บรรทัดสุดท้ายจะเป็น ( จำนวนรอบที่น้อยที่สุด , Data ก่อนทำ Radix Sort และ Data หลังทำ Radix Sort )

# Testcase : #1 1
# Enter Input : 64 8 216 512 27 729 0 1 343 125
# ------------------------------------------------------------
# Round : 1
# 0 : 0 
# 1 : 1 
# 2 : 512 
# 3 : 343 
# 4 : 64 
# 5 : 125 
# 6 : 216 
# 7 : 27 
# 8 : 8 
# 9 : 729 
# ------------------------------------------------------------
# Round : 2
# 0 : 8 1 0 
# 1 : 216 512 
# 2 : 729 27 125 
# 3 : 
# 4 : 343 
# 5 : 
# 6 : 64 
# 7 : 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# Round : 3
# 0 : 64 27 8 1 0 
# 1 : 125 
# 2 : 216 
# 3 : 343 
# 4 : 
# 5 : 512 
# 6 : 
# 7 : 729 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# 3 Time(s)
# Before Radix Sort : 64 -> 8 -> 216 -> 512 -> 27 -> 729 -> 0 -> 1 -> 343 -> 125
# After  Radix Sort : 729 -> 512 -> 343 -> 216 -> 125 -> 64 -> 27 -> 8 -> 1 -> 0

# Testcase : #2 2
# Enter Input : 456 -789 0 -50384 15615 -1 72
# ------------------------------------------------------------
# Round : 1
# 0 : 0 
# 1 : -1 
# 2 : 72 
# 3 : 
# 4 : -50384 
# 5 : 15615 
# 6 : 456 
# 7 : 
# 8 : 
# 9 : -789 
# ------------------------------------------------------------
# Round : 2
# 0 : 0 -1 
# 1 : 15615 
# 2 : 
# 3 : 
# 4 : 
# 5 : 456 
# 6 : 
# 7 : 72 
# 8 : -50384 -789 
# 9 : 
# ------------------------------------------------------------
# Round : 3
# 0 : 72 0 -1 
# 1 : 
# 2 : 
# 3 : -50384 
# 4 : 456 
# 5 : 
# 6 : 15615 
# 7 : -789 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# Round : 4
# 0 : 456 72 0 -1 -50384 -789 
# 1 : 
# 2 : 
# 3 : 
# 4 : 
# 5 : 15615 
# 6 : 
# 7 : 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# Round : 5
# 0 : 456 72 0 -1 -789 
# 1 : 15615 
# 2 : 
# 3 : 
# 4 : 
# 5 : -50384 
# 6 : 
# 7 : 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# 5 Time(s)
# Before Radix Sort : 456 -> -789 -> 0 -> -50384 -> 15615 -> -1 -> 72
# After  Radix Sort : 15615 -> 456 -> 72 -> 0 -> -1 -> -789 -> -50384

# Testcase : #3 3
# Enter Input : -1 -9 -3 -6 -5 -4 -7 0 -8 -2 3 2 5 1 4 9 8 7 6
# ------------------------------------------------------------
# Round : 1
# 0 : 0 
# 1 : 1 -1 
# 2 : 2 -2 
# 3 : 3 -3 
# 4 : 4 -4 
# 5 : 5 -5 
# 6 : 6 -6 
# 7 : 7 -7 
# 8 : 8 -8 
# 9 : 9 -9 
# ------------------------------------------------------------
# 1 Time(s)
# Before Radix Sort : -1 -> -9 -> -3 -> -6 -> -5 -> -4 -> -7 -> 0 -> -8 -> -2 -> 3 -> 2 -> 5 -> 1 -> 4 -> 9 -> 8 -> 7 -> 6
# After  Radix Sort : 9 -> 8 -> 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> -1 -> -2 -> -3 -> -4 -> -5 -> -6 -> -7 -> -8 -> -9

# Testcase : #4 4
# Enter Input : 15 -15
# ------------------------------------------------------------
# Round : 1
# 0 : 
# 1 : 
# 2 : 
# 3 : 
# 4 : 
# 5 : 15 -15 
# 6 : 
# 7 : 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# Round : 2
# 0 : 
# 1 : 15 -15 
# 2 : 
# 3 : 
# 4 : 
# 5 : 
# 6 : 
# 7 : 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# 2 Time(s)
# Before Radix Sort : 15 -> -15
# After  Radix Sort : 15 -> -15

# Testcase : #5 5
# Enter Input : -12345 98765 -87654
# ------------------------------------------------------------
# Round : 1
# 0 : 
# 1 : 
# 2 : 
# 3 : 
# 4 : -87654 
# 5 : 98765 -12345 
# 6 : 
# 7 : 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# Round : 2
# 0 : 
# 1 : 
# 2 : 
# 3 : 
# 4 : -12345 
# 5 : -87654 
# 6 : 98765 
# 7 : 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# Round : 3
# 0 : 
# 1 : 
# 2 : 
# 3 : -12345 
# 4 : 
# 5 : 
# 6 : -87654 
# 7 : 98765 
# 8 : 
# 9 : 
# ------------------------------------------------------------
# Round : 4
# 0 : 
# 1 : 
# 2 : -12345 
# 3 : 
# 4 : 
# 5 : 
# 6 : 
# 7 : -87654 
# 8 : 98765 
# 9 : 
# ------------------------------------------------------------
# Round : 5
# 0 : 
# 1 : -12345 
# 2 : 
# 3 : 
# 4 : 
# 5 : 
# 6 : 
# 7 : 
# 8 : -87654 
# 9 : 98765 
# ------------------------------------------------------------
# 5 Time(s)
# Before Radix Sort : -12345 -> 98765 -> -87654
# After  Radix Sort : 98765 -> -12345 -> -87654

# Testcase : #6 6
# Enter Input : 0 0 0 0 0 0 0
# ------------------------------------------------------------
# 0 Time(s)
# Before Radix Sort : 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0
# After  Radix Sort : 0 -> 0 -> 0 -> 0 -> 0 -> 0 -> 0

class node:
    def __init__(self,data,next = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

class linked_list:
    def __init__(self,data,head = None) -> None:
        self.head = head
        self.number = data

    def append(self,data):
        data_node = node(data=data)
        if self.head == None :
            self.head = data_node
        else:
            currnode = self.head
            while currnode.next != None:
                currnode = currnode.next
            currnode.next = data_node

    def addHead(self,data):
        newnode = node(data=data)
        if self.head == None:
            self.head = newnode
            return
        
        newnode.next = self.head
        self.head = newnode
    
    def pop_head(self):
        if self.head == None:
            return None
        
        delnode = self.head
        self.head = self.head.next
        return delnode.data

    def pop_back(self):
        if self.head == None:
            return None
        
        if self.head.next == None:
            node = self.head
            self.head = None
            return node.data

        prevnode = None        
        currnode = self.head
        while currnode.next != None:
            prevnode = currnode
            currnode = currnode.next
        if prevnode != None:
            prevnode.next = None
        return currnode.data
    
    def __str__(self) -> str:
        return_string = ""
        return_string += str(self.number) + " : "
        if self.head == None:
            return return_string
        
        currnode = self.head
        while currnode.next != None:
            return_string += str(currnode.data) + " "
            currnode = currnode.next
        return_string += str(currnode.data) + " "
        return return_string
        
    def isEmpty(self):
        return self.head == None
    
    def print_radix(self):
        return_string = "Radix Sort :"
        currnode = self.head
        while currnode.next != None:
            return_string += " " + str(currnode.data) + " ->"
            currnode = currnode.next
        return_string += " " + str(currnode.data)
        return return_string
    
    def front(self):
        if self.head == None:
            return None
        else:
            return self.head.data
        
    def insert(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
        
        elif self.head.data <= data:
            self.addHead(data)
        
        else:
            prevnode = None
            currnode = self.head
            while currnode.next != None:
                if currnode.data <= data:
                    prevnode.next = newnode
                    newnode.next = currnode
                    return
                prevnode = currnode
                currnode = currnode.next
            self.append(data)

def get_digits(num,d):
    for i in range(d-1):
        num //= 10
    return num % 10

inp = input("Enter Input : ").split()
before = linked_list("B")
result = linked_list("R")
mx = 0
for i in inp:
    i = int(i)
    result.insert(i)
    before.append(i)
    if i < 0:
        i = -i
    if mx < i:
        mx = i

digits = 0
while(mx > 0):
    digits += 1
    mx = int(mx / 10)

round = 1
# print(digits)


digit_list = [linked_list(0),linked_list(1),linked_list(2),linked_list(3),
              linked_list(4),linked_list(5),linked_list(6),linked_list(7),
              linked_list(8),linked_list(9)]

print("------------------------------------------------------------")
for i in range(1,digits + 1):
    # print(result)
    print(f"Round : {i}")
    while not result.isEmpty():
        data = result.pop_head()
        if data < 0:
            data_digit = get_digits(-data,i)
            # digit_list[data_digit].append(data)
        else:
            data_digit = get_digits(data,i)
            # digit_list[data_digit].addHead(data)
        digit_list[data_digit].append(data)
    for j in digit_list:
        print(j)
    for i in range(9,-1,-1):
        while not digit_list[i].isEmpty():
            data = digit_list[i].front()
            if data < 0:
                break
            digit_list[i].pop_head()
            result.append(data)

    for i in range(10):
        while not digit_list[i].isEmpty():
            data = digit_list[i].pop_head()
            result.append(data)
    print("------------------------------------------------------------")

print(f"{digits} Time(s)")
print("Before ",end="")
print(before.print_radix())
print("After  ",end="")
print(result.print_radix())