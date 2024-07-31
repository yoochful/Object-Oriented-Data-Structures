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
        self.items = []
        self.broken = []
    
    def push(self, weight, frequency):
        self.items.append((weight, frequency))
        self.check_break()

        
    def check_break(self):
        while len(self.items) > 1:
            top = self.items[-1]
            below = self.items[-2]
            if top[0] > below[0]:
                self.broken.append(below[1])
                self.items.pop(-2)
            else:
                break
    
    def get_broken(self):
        return self.broken
    
def process_input(input):
    plates = input.split(",")
    items = Stack()
    
    for plate in plates:
        weight, frequency = map(int, plate.split())
        items.push(weight, frequency)
        
    broken_fre = items.get_broken()
    for fre in broken_fre:
        print(fre)
    
input = input("Enter Input : ")
process_input(input)