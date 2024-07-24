# Chapter : 5 - item : 4 - หา loop ใน linked list
# ให้ตรวจสอบว่า linked list มีการวนซ้ำหรือไม่ และ แสดงผลลัพธ์ตามตัวอย่าง

# โดยมีการรับ input ดังนี้

# 1. append ->   A <int> คือ เพิ่มข้อมูลต่อท้าย linked list

# 2. set_next -> S <index1(int):index2(str)> คือการ set node.next ของ node index ที่1 ให้ชี้ไป node index ที่2

# ซึ่งหากไม่มี  node index ที่1 ใน linked list ให้แสดง error และหากไม่มี node index ที่2 ใน linked list ให้ทำการ append nodeใหม่เข้าไปใน linked list โดยมี value = index2


# Testcase : #1 1
# Enter input : A 0,A 1,S 2:0
# 0
# 0->1
# Error! {index not in length}: 2
# No Loop
# 0->1

# Testcase : #2 2
# Enter input : A 0,A 1,S 0:2
# 0
# 0->1
# index not in length, append : 2
# No Loop
# 0->1->2

# Testcase : #3 3
# Enter input : A 0,A 1,S 1:0
# 0
# 0->1
# Set node.next complete!, index:value = 1:1 -> 0:0
# Found Loop

# Testcase : #4 4
# Enter input : S 0:0
# Error! {list is empty}
# No Loop
# Empty

# Testcase : #5 5
# Enter input : A 0,A 3,A 5,A 7,A 9,S 2:0
# 0
# 0->3
# 0->3->5
# 0->3->5->7
# 0->3->5->7->9
# Set node.next complete!, index:value = 2:5 -> 0:0
# Found Loop

# Testcase : #6 6
# Enter input : A 0,A 1,A 2,S 0:2
# 0
# 0->1
# 0->1->2
# Set node.next complete!, index:value = 0:0 -> 2:2
# No Loop
# 0->2

# Testcase : #7 7
# Enter input : S 0:0,A 0,A 0,A 0,S 0:5,S 0:3,A 5,S 2:1
# Error! {list is empty}
# 0
# 0->0
# 0->0->0
# index not in length, append : 5
# Set node.next complete!, index:value = 0:0 -> 3:5
# 0->5->5
# Set node.next complete!, index:value = 2:5 -> 1:5
# Found Loop

# Testcase : #8 8
# Enter input : S 0:0,A 0
# Error! {list is empty}
# 0
# No Loop
# 0
class Node:
    def __init__(self,data, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def append(self, data):
        data = int(data)
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.size += 1
        
        return node
    
    def find_loop(self):
        slow = self.head
        fast = self.head
        found = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True
                break
        
        if found:
            print('Found Loop')
        else:
            print('No Loop')
            print(self)


    
    def __str__(self) -> str:
        log = ''
        current_node = self.head
        while current_node != None and current_node.next != None:
            log += f'{str(current_node.data)}->'
            current_node = current_node.next
        if current_node != None:
            log += str(current_node.data)
        log = log if log else 'Empty'
        return log 
    
    def set_next(self, node1, node2):
        self.head = node1
        node1.next = node2

    def S(self, index1, index2):
        index1 = int(index1)
        index2 = int(index2)
        if self.size == 0:
            print('Error! {list is empty}')
        elif index1 > self.size - 1:
            print('Error! {index not in length}: ' + str(index1))
        elif index2 > self.size - 1:
            self.append(index2)
            print('index not in length, append : ' + str(index2))
        else:
            node1 =  self.get_node_by_index(index1)
            node2 = self.get_node_by_index(index2)
            self.set_next(node1=node1,node2=node2)
            print(f'Set node.next complete!, index:value = {str(index1)}:{str(node1.data)} -> {str(index2)}:{str(node2.data)}')
            

    def get_node_by_index(self, index: int):
        current_node = self.head
        if self.size == 0:
            return None
        
        for i in range(index):
            current_node = current_node.next
        return current_node

    def run(self, user_input : str):
        commands = user_input.split(',')
        for command in commands:
            parts = command.strip().split()
            action = parts[0]
            if action == 'A':
                data = parts[1]
                self.append(data)
                print(self)
            elif action == 'S':
                index1, index2 = parts[1].split(':')
                self.S(index1,index2)
        self.find_loop()
    

user_input = input('Enter input : ')
ls = LinkedList()
ls.run(user_input=user_input)