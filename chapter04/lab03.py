# Chapter : 4 - item : 3 - Concept Queue

# รับ input 1 บรรทัด โดย แต่ละลำดับ จะมีอักษรกำกับไว้และตามด้วยจำนวนครั้งที่ต้องทำตามตัวอักษรนั้น E คือ การ enqueue และ D คือการ dequeue แต่หากเป็นตัวอักษรอื่นให้นับเป็น error input

# ต้องบอกว่า มีการ dequeue ที่ไม่เกิดผลกี่ครั้งตามลำดับ และแต่ละครั้งที่มีการเกิดขึ้นใน Queue มีการเปลี่ยนแปลงอย่างไรตามขั้นตอน

# Testcase : #1 
# input : D3,E2,E3,D9,E2,ff
# Step : D3
# Dequeue : []
# Error Dequeue : 3
# Error input : 0
# --------------------
# Step : E2
# Enqueue : ['*0', '*1']
# Error Dequeue : 3
# Error input : 0
# --------------------
# Step : E3
# Enqueue : ['*0', '*1', '*2', '*3', '*4']
# Error Dequeue : 3
# Error input : 0
# --------------------
# Step : D9
# Dequeue : []
# Error Dequeue : 7
# Error input : 0
# --------------------
# Step : E2
# Enqueue : ['*5', '*6']
# Error Dequeue : 7
# Error input : 0
# --------------------
# Step : ff
# ['*5', '*6']
# Error Dequeue : 7
# Error input : 1
# --------------------

# Testcase : #2 
# input : D3,D5,D9,D3,E12
# Step : D3
# Dequeue : []
# Error Dequeue : 3
# Error input : 0
# --------------------
# Step : D5
# Dequeue : []
# Error Dequeue : 8
# Error input : 0
# --------------------
# Step : D9
# Dequeue : []
# Error Dequeue : 17
# Error input : 0
# --------------------
# Step : D3
# Dequeue : []
# Error Dequeue : 20
# Error input : 0
# --------------------
# Step : E12
# Enqueue : ['*0', '*1', '*2', '*3', '*4', '*5', '*6', '*7', '*8', '*9', '*10', '*11']
# Error Dequeue : 20
# Error input : 0
# --------------------

# Testcase : #3 
# input : df,fs,E0,E2,D2,D3,ff,fd
# Step : df
# []
# Error Dequeue : 0
# Error input : 1
# --------------------
# Step : fs
# []
# Error Dequeue : 0
# Error input : 2
# --------------------
# Step : E0
# Enqueue : []
# Error Dequeue : 0
# Error input : 2
# --------------------
# Step : E2
# Enqueue : ['*0', '*1']
# Error Dequeue : 0
# Error input : 2
# --------------------
# Step : D2
# Dequeue : []
# Error Dequeue : 0
# Error input : 2
# --------------------
# Step : D3
# Dequeue : []
# Error Dequeue : 3
# Error input : 2
# --------------------
# Step : ff
# []
# Error Dequeue : 3
# Error input : 3
# --------------------
# Step : fd
# []
# Error Dequeue : 3
# Error input : 4
# --------------------

class Queue:
    def __init__(self, lst=None):
        self.items = lst if lst is not None else []

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def push(self, item):
        self.items.append(item)

    def top(self):
        return self.items[0] if not self.is_empty() else None

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def reverse(self):
        self.items.reverse()

    def has(self, item):
        return item in self.items

    def index(self, item):
        return self.items.index(item) if item in self.items else -1

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def sort(self):
        self.items.sort()

    def dequeue(self):
        return self.pop()

    def enqueue(self, item):
        self.push(item)

    def peek(self):
        return self.top()

    def size(self):
        return len(self.items)

    def front(self):
        return self.top()

def solve(q,text, num):
    if not (isinstance(text, str) and isinstance(num , int)):
        return -2
    if text == "D":
        if q.is_empty():
            return -1
        else:
            return 1
    elif text == "E":
        return 2

q = Queue()
inp = input("input : ").split(",")
errorDequeCount = 0
errorInputCount = 0
itr = 0
# modified_list = [f"*{x}" for x in original_list]

for item in inp:
    text, num = item[0] ,item[1:]
    print(f"Step : {text}{num}")
    if not ((text == "E" or text =="D") and (num >= "0" and num <= "9")):
        """input error"""
        print(f"{q.items}")
        errorInputCount+=1
    elif text == "D":
        num = int(num)
        for i in range(num):
            if not q.is_empty():
                q.dequeue()
            else:
                errorDequeCount+=(num-i)
                break
        print(f"Dequeue : {q.items}")
    elif text == "E":
        num = int(num)
        for _ in range(num):
            q.enqueue("*"+str(itr))
            itr += 1
        print(f"Enqueue : {q.items}")
    print(f"Error Dequeue : {errorDequeCount}")
    print(f"Error input : {errorInputCount}")
    print(f"--------------------")
