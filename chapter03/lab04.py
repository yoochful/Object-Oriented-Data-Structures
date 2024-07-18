# Chapter : 3 - item : 4 - Stack Calculator

# ให้เขียน class calculator  ที่มีการทำงานผ่านฟังก์ชัน run(instructions) โดยมี instructions ดังนี้
# +: Pop 2 ค่าออกจาก stack, นำมาบวกกัน และ push ผลลัพธ์ลง stack
# -: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนลบด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# *: Pop 2 ค่าออกจาก stack, นำมาคูณกัน และ push ผลลัพธ์ลง stack
# /: Pop 2 ค่าออกจาก stack, นำค่าที่อยู่ข้างบนหารด้วยค่าที่อยู่ข้างล่าง และ push ผลลัพธ์ลง stack
# DUP: Duplicate (not double) ค่าบนสุดของ stack
# POP: Pop ค่าบนสุดออกจาก stack และ discard.
# PSH: ทำการ push ตัวเลขลง stack
# หมายเหตุ 1. คำสั่งอื่น ๆ (เช่นตัวอักษร) ควรทำให้เกิดค่า "Invalid instruction: [instruction]"
# 2. การนำค่าออกจาก stack สำหรับ calculator นี้ให้ การนำค่าออกจาก stack ครั้งแรกเป็น operand ด้านซ้าย และ การนำค่าออกจาก stack ครั้งที่ 2 เป็น operand ด้านขวา
# *************************************************
# print("* Stack Calculator *")
# arg = input("Enter arguments : ")
# machine = StackCalc()
# machine.run(arg)
# print(machine.getValue())

# Testcase : #1 1
# * Stack Calculator *
# Enter arguments : 5 6 +
# 11

# Testcase : #2 2
# * Stack Calculator *
# Enter arguments : 3 DUP +
# 6

# Testcase : #3 3
# * Stack Calculator *
# Enter arguments : 6 5 5 7 * - /
# 5

# Testcase : #4 4
# * Stack Calculator *
# Enter arguments : a b c +
# Invalid instruction: a

# Testcase : #5 5
# * Stack Calculator *
# Enter arguments : 12
# 12

# Testcase : #6 6
# * Stack Calculator *
# Enter arguments : 9 14 DUP + - 3 POP
# 19

# Testcase : #7 7
# * Stack Calculator *
# Enter arguments : 1 2 3 4 5 POP POP POP
# 2

# Testcase : #8 8
# * Stack Calculator *
# Enter arguments : 13 DUP 4 POP 5 DUP + DUP + -
# 7

# Testcase : #9 9
# * Stack Calculator *
# Enter arguments : 4 POP
# 0

class StackCalc:
    def __init__(self):
        self.stack = []
        self.error = None

    def run(self, instructions):
        for instruction in instructions.split():
            if instruction.isdigit() or (instruction[0] == '-' and instruction[1:].isdigit()):  # Handling negative numbers
                self.stack.append(int(instruction))
            elif instruction == '+':
                self._add()
            elif instruction == '-':
                self._subtract()
            elif instruction == '*':
                self._multiply()
            elif instruction == '/':
                self._divide()
            elif instruction == 'DUP':
                self._duplicate()
            elif instruction == 'POP':
                self._pop()
            else:
                self.error = f"Invalid instruction: {instruction}"
                break

    def _add(self):
        if len(self.stack) >= 2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a + b)
        else:
            self.error = "Invalid instruction: +"

    def _subtract(self):
        if len(self.stack) >= 2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a - b)
        else:
            self.error = "Invalid instruction: -"

    def _multiply(self):
        if len(self.stack) >= 2:
            a = self.stack.pop()
            b = self.stack.pop()
            self.stack.append(a * b)
        else:
            self.error = "Invalid instruction: *"

    def _divide(self):
        if len(self.stack) >= 2:
            a = self.stack.pop()
            b = self.stack.pop()
            if b == 0:
                self.error = "Invalid instruction: division by zero"
            else:
                self.stack.append(int(a / b))
        else:
            self.error = "Invalid instruction: /"

    def _duplicate(self):
        if len(self.stack) >= 1:
            self.stack.append(self.stack[-1])
        else:
            self.error = "Invalid instruction: DUP"

    def _pop(self):
        if len(self.stack) >= 1:
            self.stack.pop()
        else:
            self.error = "Invalid instruction: POP"

    def getValue(self):
        if self.error:
            return self.error
        if self.stack:
            return self.stack[-1]
        else:
            return 0

# Example usage:
print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())