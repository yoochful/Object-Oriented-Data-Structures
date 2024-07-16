# Chapter : 4 - item : 2 - คอยนาน

# จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

# โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

# แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

# แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

# ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

# จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด

# Testcase : #1 1
# Enter people : Lorem_Ipsum
# 1 ['o', 'r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L'] []
# 2 ['r', 'e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o'] []
# 3 ['e', 'm', '_', 'I', 'p', 's', 'u', 'm'] ['L', 'o', 'r'] []
# 4 ['m', '_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e'] []
# 5 ['_', 'I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm'] []
# 6 ['I', 'p', 's', 'u', 'm'] ['o', 'r', 'e', 'm', '_'] []
# 7 ['p', 's', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] []
# 8 ['s', 'u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p']
# 9 ['u', 'm'] ['r', 'e', 'm', '_', 'I'] ['p', 's']
# 10 ['m'] ['e', 'm', '_', 'I', 'u'] ['s']
# 11 [] ['e', 'm', '_', 'I', 'u'] ['s', 'm']

# Testcase : #2 2
# Enter people : JUST_DO_IT!!!!
# 1 ['U', 'S', 'T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J'] []
# 2 ['S', 'T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J', 'U'] []
# 3 ['T', '_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['J', 'U', 'S'] []
# 4 ['_', 'D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T'] []
# 5 ['D', 'O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T', '_'] []
# 6 ['O', '_', 'I', 'T', '!', '!', '!', '!'] ['U', 'S', 'T', '_', 'D'] []
# 7 ['_', 'I', 'T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] []
# 8 ['I', 'T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] ['_']
# 9 ['T', '!', '!', '!', '!'] ['S', 'T', '_', 'D', 'O'] ['_', 'I']
# 10 ['!', '!', '!', '!'] ['T', '_', 'D', 'O', 'T'] ['I']
# 11 ['!', '!', '!'] ['T', '_', 'D', 'O', 'T'] ['I', '!']
# 12 ['!', '!'] ['T', '_', 'D', 'O', 'T'] ['!', '!']
# 13 ['!'] ['_', 'D', 'O', 'T', '!'] ['!', '!']
# 14 [] ['_', 'D', 'O', 'T', '!'] ['!', '!']

# Testcase : #3 3
# Enter people : A_is_stand_for_amazing
# 1 ['_', 'i', 's', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A'] []
# 2 ['i', 's', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A', '_'] []
# 3 ['s', '_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['A', '_', 'i'] []
# 4 ['_', 's', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's'] []
# 5 ['s', 't', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's', '_'] []
# 6 ['t', 'a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 'i', 's', '_', 's'] []
# 7 ['a', 'n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] []
# 8 ['n', 'd', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] ['a']
# 9 ['d', '_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['i', 's', '_', 's', 't'] ['a', 'n']
# 10 ['_', 'f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['n']
# 11 ['f', 'o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['n', '_']
# 12 ['o', 'r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['s', '_', 's', 't', 'd'] ['_', 'f']
# 13 ['r', '_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['_', 'f']
# 14 ['_', 'a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['f', 'r']
# 15 ['a', 'm', 'a', 'z', 'i', 'n', 'g'] ['_', 's', 't', 'd', 'o'] ['f', 'r', '_']
# 16 ['m', 'a', 'z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['r', '_']
# 17 ['a', 'z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['r', '_', 'm']
# 18 ['z', 'i', 'n', 'g'] ['s', 't', 'd', 'o', 'a'] ['_', 'm', 'a']
# 19 ['i', 'n', 'g'] ['t', 'd', 'o', 'a', 'z'] ['_', 'm', 'a']
# 20 ['n', 'g'] ['t', 'd', 'o', 'a', 'z'] ['m', 'a', 'i']
# 21 ['g'] ['t', 'd', 'o', 'a', 'z'] ['m', 'a', 'i', 'n']
# 22 [] ['d', 'o', 'a', 'z', 'g'] ['a', 'i', 'n']

class CashierQueue:
    def __init__(self, time_per_customer):
        self.queue = []
        self.time_per_customer = time_per_customer
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def add_customer(self, customer):
        self.queue.append(customer)
    
    def remove_customer(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def process_time(self):
        return self.time_per_customer


def simulate_queues(customers):
    cashier1 = CashierQueue(3)  # Time per customer for cashier 1
    cashier2 = CashierQueue(2)  # Time per customer for cashier 2
    main_queue = list(customers)  # Convert string of customers to list of characters
    
    minute = 1
    result = []
    while main_queue or not cashier1.is_empty() or not cashier2.is_empty():
        result.append(f"{minute} {main_queue} {cashier1.queue} {cashier2.queue}")
        
        if not cashier1.is_empty():
            cashier1.time_per_customer -= 1
            if cashier1.time_per_customer == 0:
                cashier1.remove_customer()
        
        if not cashier2.is_empty():
            cashier2.time_per_customer -= 1
            if cashier2.time_per_customer == 0:
                cashier2.remove_customer()
        
        if main_queue:
            customer = main_queue.pop(0)
            if not cashier1.is_empty():
                cashier1.add_customer(customer)
            elif not cashier2.is_empty():
                cashier2.add_customer(customer)
            else:
                cashier1.add_customer(customer)
        
        minute += 1
    
    return result

# Input
inputs = [
    "Lorem_Ipsum",
    "JUST_DO_IT!!!!",
    "A_is_stand_for_amazing"
]

for input_str in inputs:
    output = simulate_queues(input_str)
    for line in output:
        print(line)
    print()

