# Chapter : 5 - item : 3 - MergeOrderList
# จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้

# createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist

# printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว

# mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว

# ****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****

# ****ห้ามสร้าง Class LinkList****

# class node:
#     def __init__(self,data,next = None ):
#         ### Code Here ###
#     def __str__(self):
#         ### Code Here ###

# def createList(l=[]):
#     ### Code Here ###

# def printList(H):
#     ### Code Here ###

# def mergeOrderesList(p,q):
#     ### Code Here ###

# #################### FIX comand ####################   
# # input only a number save in L1,L2
# LL1 = createList(L1)
# LL2 = createList(L2)
# print('LL1 : ',end='')
# printList(LL1)
# print('LL2 : ',end='')
# printList(LL2)
# m = mergeOrderesList(LL1,LL2)
# print('Merge Result : ',end='')
# printList(m)


# Testcase : #1 1
# Enter 2 Lists : 1,3,5,7,10,20,22 4,6,7,8,15
# LL1 : 1 3 5 7 10 20 22 
# LL2 : 4 6 7 8 15 
# Merge Result : 1 3 4 5 6 7 7 8 10 15 20 22 

# Testcase : #2 2
# Enter 2 Lists : 1,4,5,5,6,7 2,3,6,9,10
# LL1 : 1 4 5 5 6 7 
# LL2 : 2 3 6 9 10 
# Merge Result : 1 2 3 4 5 5 6 6 7 9 10 

# Testcase : #3 3
# Enter 2 Lists : 2,2,2,10 1,1,1,1,5,5,5,6,7,8
# LL1 : 2 2 2 10 
# LL2 : 1 1 1 1 5 5 5 6 7 8 
# Merge Result : 1 1 1 1 2 2 2 5 5 5 6 7 8 10
  
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

def createList(values):
    if not values:
        return None
    head = Node(int(values[0]))
    current = head
    for value in values[1:]:
        current.next = Node(int(value))
        current = current.next
    return head

def printList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

def mergeOrderedList(p, q):
    if not p:
        return q
    if not q:
        return p
    
    result_head = Node()
    current = result_head
    
    while p and q:
        if p.data <= q.data:
            current.next = p
            p = p.next
        else:
            current.next = q
            q = q.next
        current = current.next
    
    if p:
        current.next = p
    if q:
        current.next = q
    
    return result_head.next

if __name__ == "__main__":
    # Reading input from user
    l1, l2 = input("Enter 2 Lists : ").split()
    l1 = list(map(int, l1.split(",")))
    l2 = list(map(int, l2.split(",")))
    
    # Create linked lists
    LL1 = createList(l1)
    LL2 = createList(l2)
    
    # Print original lists
    print("LL1 :", end=" ")
    printList(LL1)
    print("LL2 :", end=" ")
    printList(LL2)
    
    # Merge and print result
    merged = mergeOrderedList(LL1, LL2)
    print("Merge Result :", end=" ")
    printList(merged)
