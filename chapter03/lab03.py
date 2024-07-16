# Chapter : 3 - item : 3 - Color_Crush

# หลังจากกฤษฎาล้างจานเสร็จ ก็ได้มาเล่นเกมส์ที่กำลังเป็นที่นิยมทั่วโลกในตอนนี้   Microsoft Flight Simulator ?  Fall Guys ?  Valorant ?  "ผิดทั้งหมด!" กฤษฎาได้กล่าวไว้  เกมที่กำลังเป็นที่นิยมคือ Color Crush ต่างหาก   
# โดยเกมนี้จะเป็นการนำสีมาเรียงต่อกัน โดยสีจะหายไปก็ต่อเมื่อมีการเรียงสีเหมือนกันครบ 3 อัน เช่น  A B B B A  -> A A เนื่องจาก B เรียงติดกัน 3 ตัวทำให้ระเบิดหายไปโดยที่สีจะมีทั้งหมด 26 สี และจะถูกแทนด้วย A - Z  โดยถ้าหากมีการระเบิดตั้งแต่ 2 ครั้งขึ้นไปจะแสดง Combo ขึ้นมา

#     โดยเมื่อการระเบิดสิ้นสุดลงให้แสดงจำนวนและลำดับของสีที่เหลือจากขวาไปซ้าย


# class Stack:

#     def __init__(self):

#     def push(self, value):

#     def pop(self):

#     def size(self):

#     def isEmpty(self):



# inp = input('Enter Input : ').split()

# S = Stack()

# ### Enter Your Code Here ###

# print(S.size())

# ### Enter Your Code Here ###


# Testcase : #1 
# Enter Input : G H H H H P
# 3
# PHG

# Testcase : #2 
# Enter Input : L C C X X X C D
# 2
# DL
# Combo : 2 ! ! !

# Testcase : #3 
# Enter Input : C C C
# 0
# Empty

# Testcase : #4 
# Enter Input : A
# 1
# A

# Testcase : #5 
# Enter Input : A B B A
# 4
# ABBA

# Testcase : #6 
# Enter Input : O O P Y Y E R R R E E Y P P K K K O
# 0
# Empty
# Combo : 6 ! ! !


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

def color_crush(inp):
    S = Stack()
    combo = 0

    for color in inp:
        S.push(color)
        
        while True:
            if S.size() < 3:
                break
            
            top = []
            for i in range(3):
                if S.size() > i:
                    top.append(S.items[-(i + 1)])
                else:
                    break

            if len(top) == 3 and top[0] == top[1] == top[2]:
                for _ in range(3):
                    S.pop()
                combo += 1
            else:
                break

    remaining_colors = []
    while not S.isEmpty():
        remaining_colors.append(S.pop())

    print(len(remaining_colors))
    if len(remaining_colors) > 0:
        print(''.join(remaining_colors))
    else:
        print('Empty')

    if combo >= 2:
        print(f'Combo : {combo} ! ! !')

inp = input('Enter Input : ').split()
color_crush(inp)
