# Chapter : 3 - item : 2 - แ ต ก ดั ง เ พ ล้ ง ! ! !

# กฤษฎาได้ถูกคุณแม่ไหว้วานให้ล้างจานกองเป็นภูเขา  แต่ทว่ากฤษฎาก็ได้สังเกตเห็นว่าจานแต่ละใบนั้นมีน้ำหนักที่แตกต่างกัน และบนจานยังมีตัวเลขอีกด้วย  กฤษฎาได้เหม่อลอยเนื่องจากครุ่นคริสว่าตัวเลขนั้นหมายถึงอะไร  กฤษฎาก็ได้ทำจานหลุดมือจนจานแตก  และเมื่อจานแตกได้มีเสียงที่มีความถี่ตามเลขบนจาน  กฤษฎาจึงนึกสนุกได้นำจานขนาดต่างๆและมีความถี่ต่างกันมาวางซ้อนๆกัน  โดยถ้าหากนำจานที่มีน้ำหนักมากกว่ามาวางบนจานที่มีน้ำหนักน้อยกว่า จะทำให้จานที่มีน้ำหนักน้อยกว่า แตก !!! และจะแตกไปเรื่อยๆจนกว่าจานใบด้านล่างจะมีน้ำหนักเท่ากันหรือมากกว่า หรือจนกว่าจะไม่มีจานด้านล่างมารองรับแล้ว

# ให้น้องๆเขียนโปรแกรมอ่านลำดับของจานที่กฤษฎาได้วางลงไปโดยให้ใส่จานทีละใบ  ซึ่งรวมถึงขนาดของจานและความถี่ของจาน  จากนั้นให้หาว่าลำดับของความถี่ของจานที่ได้ยินเมื่อวางจานลงไปตามนั้นแล้วจะเป็นเช่นใด

# อธิบาย Input : จะมีแค่รูปแบบเดียวคือ   < a  b >  โดยที่  a = น้ำหนักของจาน  ,  b = ความถี่ของจาน

# Testcase : #1
# Enter Input : 1 10,5 20,3 30,3 40,4 50
# 10
# 40
# 30

# Testcase : #2
# Enter Input : 90 8,68 99,44 3,44 102,50 2
# 102
# 3

class Stack:
    def __init__(self):
        self.stack = []
        self.broken_frequencies = []
    
    def push(self, weight, frequency):
        self.stack.append((weight, frequency))
        self.check_for_breaks()
    
    def check_for_breaks(self):
        while len(self.stack) > 1:
            top = self.stack[-1]
            below = self.stack[-2]
            if top[0] > below[0]:
                self.broken_frequencies.append(below[1])
                self.stack.pop(-2) 
            else:
                break
    
    def get_broken_frequencies(self):
        return self.broken_frequencies

def process_input(input_string):
    plates_info = input_string.split(',')
    stack = Stack()
    
    for plate_info in plates_info:
        weight, frequency = map(int, plate_info.split())
        stack.push(weight, frequency)
    
    broken_frequencies = stack.get_broken_frequencies()
    for freq in broken_frequencies:
        print(freq)

input_string = input("Enter Input : ")
process_input(input_string)


