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
