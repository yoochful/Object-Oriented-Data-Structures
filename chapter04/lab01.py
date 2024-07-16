# Chapter : 4 - item : 1 - รู้จักกับ QUEUE

# ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ QUEUE ในการแก้ปัญหา



# E  <value>  ให้นำ value ไปใส่ใน QUEUE และทำการแสดงผล Size ปัจจุบันของ QUEUE

# D                 ให้ทำการแสดงผลของvalueที่อยู่หน้าสุดและindexของvalueนั้นจากนั้นทำการ De_QUEUE ถ้าหากไม่มี value อยู่ใน Queue ให้แสดงผลเป็น  -1

# *** ในตอนสุดท้ยถ้าหากใน Queue ยังมี Value อยู่ให้แสดงผลออกมา  ถ้าหากไม่มีแล้วให้แสดงคำว่า  Empty

# Testcase : #1 
# Enter Input : E 10,E 20,E 30,E 40,D,D
# 1
# 2
# 3
# 4
# 10 0
# 20 0
# 30 40

# Testcase : #2 
# Enter Input : E 10,E 20,E 30,E 40,D,E 50,E 60,D,D,D,D,D,D
# 1
# 2
# 3
# 4
# 10 0
# 4
# 5
# 20 0
# 30 0
# 40 0
# 50 0
# 60 0
# -1
# Empty

def queue_operations():
    queue = []
    results = []
    
    input_strings = input("Enter Input : ").split(',')
    
    for input_string in input_strings:
        if input_string.startswith('E'):
            _, value = input_string.split()
            queue.append(value)
            results.append(str(len(queue)))
        elif input_string == 'D':
            if queue:
                value = queue.pop(0)
                results.append(f"{value} 0")
            else:
                results.append("-1")
    
    if queue:
        results.append(' '.join(queue))
    else:
        results.append("Empty")
    
    print('\n'.join(results))

queue_operations()
