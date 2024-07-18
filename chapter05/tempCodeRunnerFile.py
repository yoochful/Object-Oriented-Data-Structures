
# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next

# class LinkList:
#     def __init__(self):
#         self.head = None

#     def appendHead(self, value):
#         node = Node(value, self.head)
#         self.head = node

#     def appendLast(self, value):
#         if self.head is None:  
#             self.appendHead(value)  #ถ้าว่างเปล่าให้เพิ่มเป็นตัวแรก
#             return
#         #CODE HERE
#         current = self.head
#         while current.next is not None:   #ถ้าไม่ได้ว่างเปล่าให้เพิ่มเป็นตัวแรก
#             current = current.next        #เปลี่ยน current ไปเป็นโหนดถัดไป
#         current.next = Node(value)        #เอา Value มาสร้าง Node ใหม่ แล้วให้ next ของ current ชี้ไปโหนดใหม่ สรุปคือ Node ใหม่กลายเป็น Node สุดท้าย
        
#     def removeLast(self):
#         #CODE HERE
#         if self.head is None:
#             return Exception("LinkedList is empty!")   #ถ้าว่างเปล่า ให้แสดง LinkedList is empty!
#         if self.head.next is None:                     
#             self.head = None                            #ถ้ามี Node ตัวเดียว ให้ Head เป็น None
#             return                                      
#         current = self.head                             
#         while current.next.next is not None:            #ถ้าไม่ใช่ Node ตัวเดียว ให้วนลูปไปยังโหนดก่อนโหนดสุดท้าย 
#             current = current.next                      #เปลี่ยน current ไปเป็นโหนดถัดไป
#         current.next = None                             #แล้วตั้ง next ของโหนดนั้นเป็น None (ลบการต่อกับโหนดสุดท้าย)

#     def rename(self, newName):
#         #CODE HERE
#         if self.head is None:
#             return Exception("LinkedList is empty!")    #ถ้าว่างเปล่า ให้แสดง LinkedList is empty!
#         current = self.head
#         while current.next is not None:                 #ถ้าไม่ได้ว่างเปล่า
#             current = current.next                      #เปลี่ยน Current ไปเป็นโหนดถัดไป
#         current.value = newName                         #แล้วเปลี่ยน Value ของโหนดเป็น newName

#     def printList(self):
#         #CODE HERE
#         if self.head is None:
#             print("LinkedList is empty!")               #ถ้าว่างเปล่า ให้แสดง LinkedList is empty!
#             return
#         current = self.head
#         result = []
#         while current is not None:
#             result.append(current.value)
#             current = current.next
#         print(" -> ".join(result))

#     def printListWithNoDuplicate(self):
#         #CODE HERE
#         if self.head is None:
#             print("LinkedList is empty!")
#             return
#         current = self.head
#         result = []
#         seen = set()
#         while current is not None:
#             if current.value not in seen:
#                 result.append(current.value)
#                 seen.add(current.value)
#             current = current.next
#         print(" -> ".join(result))

# def convertToLinkList(ls):
#     #CODE HERE
#     ll = LinkList()
#     for item in ls:
#         ll.appendLast(item)
#     return ll

# print("*** My Favourite Keynote ***")
# user_input = input("Enter Input / List of operation : ")
# input_data, operations = user_input.split(" / ")
# listSong = input_data.split()
# operations = operations.split(", ")


# try:
#     myLinkList = convertToLinkList(listSong)
#     myLinkList.printList()

#     for operation in operations:
#         op_parts = operation.split()
#         if op_parts[0] == 'A':
#             myLinkList.appendLast(op_parts[1])
#         elif op_parts[0] == 'D':
#             myLinkList.removeLast()
#         elif op_parts[0] == 'R':
#             myLinkList.rename(op_parts[1])
#         else:
#             raise Exception("Unknown operation")
#     myLinkList.printList()
#     myLinkList.printListWithNoDuplicate()
# except Exception as e:
#     print("Error!!!")
