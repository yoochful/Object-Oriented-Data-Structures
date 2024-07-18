# Chapter : 5 - item : 1 - I LOVE SINGING

# วันหนึ่งนายที่มาก่อน y แต่หลัง w อยากลองทดสอบเสียงจึงไล่คีย์โน้ต โด เร มี ฟา ซอน ลา ที แต่เขาไม่ชอบที่ร้องซ้ำคีย์เดิม และมีคีย์อยู่ในหัวใจ แต่คนอื่นในจักรวาลมักจะให้คีย์ที่ไม่ถูกใจเขา 
# เขาจึงอยากวอนขอให้โปรแกรมเมอร์ระดับจักรวาลช่วยเขียนโปรแกรมนี้ขึ้นมา โดยการทำงานมีดังนี้

# อินพุทแรก จะรับคีย์โน้ตโดยสามารถซ้ำกันได้ และคั่นด้วยช่องว่าง

# อินพุทที่สอง จะรับ serie of operation และจะคั่นด้วยคอมม่า โดยมี 3 รูปแบบดังนี้

# D(Delete) : ให้ทำการลบตัวหลังสุดของ LinkedList

# R(Rename) : ให้เปลี่ยนคีย์โน้ตตัวหลังสุดของ LinkedList ตามที่ป้อนมา เช่น R mi แปลว่า เปลี่ยนจาก … เป็น mi

# A(Add) : ให้เพิ่มคีย์โน้ตตามที่ป้อมมา เช่น A mi แปลว่า เพิ่มโน้ต mi ต่อท้าย LinkedList



# ด้วยการรับมาในครั้งเดียว แบ่ง อินพุททั้ง 2 ด้วยเครื่องหมาย / 

# ให้แสดงผล LinkedList 3 ครั้ง โดยมีรูปแบบเป็นไปตาม Test Case

# ก่อนจะทำตาม operation ต่างๆที่ป้อนมา

# หลังจากทำตาม operation

# LinkedList ที่ไม่มีข้อมูลซ้ำกัน


# สามารถเพิ่มโค้ดในบรรทัดที่เขียนว่า #CODE HERE หรือเพิ่ม method ในคลาส LinkedList ได้


# ****Note****

# -หากมี Error เกิดขึ้นในระหว่างที่ทำ operation ให้แสดงคำว่า Error!!! ทันที

# -ถ้า LinkedList ว่าง ให้แสดงคำว่า LinkedList is empty!




# *******ห้ามใช้ List! ให้ใช้ class Node ในการทำ Linked List เท่านั้น*********

# class Node:

#     def __init__(self,value=None,next=None):

#         self.value = value

#         self.next = next


# class LinkList:

#     def __init__(self):

#         self.head = None

    

#     def appendHead(self,value):

#         node = Node(value,self.head)

#         self.head = node


#     def appendLast(self,value):

#         if self.head is None:

#             self.appendHead(value)

#             return

#         #CODE HERE

    

#     def removeLast(self):

#         #CODE HERE


#     def rename(self, newName):

#         #CODE HERE

            


#     def printList(self):

#         #CODE HERE

    

#     def printListWithNoDuplicate(self):

#         #CODE HERE


# def convertToLinkList(ls):

#     #CODE HERE

    


# print("*** My Favourite Keynote ***")

# listSong = input("Enter Input : ").split(' ')

# operations = input("Enter list of operation : ").split(", ")

# print(operations)

# myLinkList = convertToLinkList(listSong)

# myLinkList.printList()

# #CODE HERE

# myLinkList.printList()

# myLinkList.printListWithNoDuplicate()



# Testcase : #1 1
# *** My Favourite Keynote ***
# Enter Input / List of operation : doh re mi fa so la ti / A doh, A re, D, R fa
# doh -> re -> mi -> fa -> so -> la -> ti
# doh -> re -> mi -> fa -> so -> la -> ti -> fa
# doh -> re -> mi -> fa -> so -> la -> ti

# Testcase : #2 2
# *** My Favourite Keynote ***
# Enter Input / List of operation : doh re fa so ti / D, D, D, A mi
# doh -> re -> fa -> so -> ti
# doh -> re -> mi
# doh -> re -> mi

# Testcase : #3 3
# *** My Favourite Keynote ***
# Enter Input / List of operation : re doh so / D, D, R doh, A re, R mi
# re -> doh -> so
# doh -> mi
# doh -> mi

# Testcase : #4 4
# *** My Favourite Keynote ***
# Enter Input / List of operation : doh re fa so ti / D, D, D, D, D, D, D
# doh -> re -> fa -> so -> ti
# Error!!!
# Error!!!
# Linklist is empty!
# Linklist is empty!

# Testcase : #5 5
# *** My Favourite Keynote ***
# Enter Input / List of operation : doh / R mi
# doh
# mi
# mi

# Testcase : #6 6
# *** My Favourite Keynote ***
# Enter Input / List of operation : doh / D, R mi, R fa
# doh
# Error!!!
# Error!!!
# Linklist is empty!
# Linklist is empty!

# Testcase : #7 7
# *** My Favourite Keynote ***
# Enter Input / List of operation : doh re so la ti / A ti, A ti, R mi
# doh -> re -> so -> la -> ti
# doh -> re -> so -> la -> ti -> ti -> mi
# doh -> re -> so -> la -> ti -> mi

# Testcase : #8 8
# *** My Favourite Keynote ***
# Enter Input / List of operation : doh doh re / A re, R doh
# doh -> doh -> re
# doh -> doh -> re -> doh
# doh -> re



class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Linklist:
    def __init__(self):
        self.head = None

    def appendHead(self, value):
        node = Node(value, self.head) 
        self.head = node

    def appendLast(self, value):
        if self.head is None:
            self.appendHead(value)  #ถ้าว่างเปล่าให้เพิ่มเป็นตัวแรก
            return
        current = self.head
        while current.next is not None:   #ถ้าไม่ได้ว่างเปล่าให้เพิ่มเป็นตัวแรก
            current = current.next        #เปลี่ยน current ไปเป็นโหนดถัดไป
        current.next = Node(value)        #เอา Value มาสร้าง Node ใหม่ แล้วให้ next ของ current ชี้ไปโหนดใหม่ สรุปคือ Node ใหม่กลายเป็น Node สุดท้าย

    def removeLast(self):
        if self.head is None:
            raise Exception("Linklist is empty!")       #ถ้าว่างเปล่า ให้แสดง LinkedList is empty!
        if self.head.next is None:                  
            self.head = None                            #ถ้ามี Node ตัวเดียว ให้ Head เป็น None
            return
        current = self.head
        while current.next.next is not None:            #ถ้าไม่ใช่ Node ตัวเดียว ให้วนลูปไปยังโหนดก่อนโหนดสุดท้าย
            current = current.next                      #เปลี่ยน current ไปเป็นโหนดถัดไป
        current.next = None                             #แล้วตั้ง next ของโหนดนั้นเป็น None (ลบการต่อกับโหนดสุดท้าย)

    def rename(self, newName):
        if self.head is None:
            raise Exception("Linklist is empty!")       #ถ้าว่างเปล่า ให้แสดง LinkedList is empty!
        current = self.head
        while current.next is not None:                 #ถ้าไม่ได้ว่างเปล่า
            current = current.next                      #เปลี่ยน Current ไปเป็นโหนดถัดไป
        current.value = newName                         #แล้วเปลี่ยน Value ของโหนดเป็น newName

    def printList(self):
        if self.head is None:
            print("Linklist is empty!")                 #ถ้าว่างเปล่า ให้แสดง LinkedList is empty!
            return
        current = self.head
        result = []
        while current is not None:
            result.append(current.value)
            current = current.next
        print(" -> ".join(result))

    def printListWithNoDuplicate(self):
        if self.head is None:
            print("Linklist is empty!")
            return
        current = self.head
        result = []
        seen = set()
        while current is not None:
            if current.value not in seen:
                result.append(current.value)
                seen.add(current.value)
            current = current.next
        print(" -> ".join(result))

def convertToLinklist(ls):
    ll = Linklist()
    for item in ls:
        ll.appendLast(item)
    return ll

print("*** My Favourite Keynote ***")

input_data = input("Enter Input / List of operation : ")
listSong, operations = input_data.split(' / ')
listSong = listSong.split()
operations = operations.split(", ")

myLinklist = convertToLinklist(listSong)

myLinklist.printList()

# Processing operations
for operation in operations:
    try:
        if operation.startswith('D'):
            myLinklist.removeLast()
        elif operation.startswith('R'):
            _, newName = operation.split()
            myLinklist.rename(newName)
        elif operation.startswith('A'):
            _, newName = operation.split()
            myLinklist.appendLast(newName)
    except Exception as e:
        print("Error!!!")

myLinklist.printList()
myLinklist.printListWithNoDuplicate()

