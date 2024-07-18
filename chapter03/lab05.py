# Chapter : 3 - item : 5 - วันหนึ่งฉันเดินเข้าป่า (ต่อ)
# <<<  กฤษฎาจำเป็นต้องเดินทางไกลเข้าไปในป่าเนื่องจากเป็นหลักสูตรของลูกเสือสามัญ  แต่กฤษฎาได้หลงทางเข้ามาในป่าลึก (เดินยังไงให้หลงครับเนี่ยย - -") หลังจากเดินไปสักพักกฤษฎาก็ได้สังเกตเห็นเลขบนต้นไม้แต่ละต้น ซึ่งเป็นตัวเลขที่แสดงความสูงของต้นไม้แต่ละต้น (มีหน่วยเป็นเมตร) กฤษฎาจึงคิดอะไรสนุกๆทำเพื่อแก้เบื่อโดยการเดินไปเรื่อยๆ และจำความสูงของต้นไม้แต่ละต้น และจะหันกลับมามอง ต้นไม้ที่เคยเดินผ่านไป >>>

# ****  ด้านบนจะเป็นเนื้อหาของ  < วันหนึ่งฉันเดินเข้าป่า   version  1 >  เผื่อบางคน Random ไม่ได้ครับ


# หลังจากกฤษฎาเดินหลงป่ามาได้สักพักก็ได้ไปเจอเห็ดสีสันสวยงามจึงได้หยิบขึ้นมากิน  หลังจากกินเข้าไปทำให้กฤษฎามีอาการแปลกๆเกิดขึ้น  เนื่องจากเห็ดที่กินเข้าไปเป็นเห็ดพิษ  แต่กฤษฎาก็ยังคอยนับความสูงต้นไม้ไปเรื่อยๆเหมือนเดิม  ผลข้างเคียงจากเห็ดพิษก็ได้ส่งผลกระทบต่อการนับต้นไม้ของกฤษฎาเนื่องจากอาการหลอนประสาท ทำให้ต้นไม้ที่มีความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร ความสูงที่น้อยที่สุดคือ 1 เมตร

# ให้น้องๆเขียนโปรแกรมเพื่อรับความสูงของต้นไม้ที่กฤาฎาได้เดินผ่าน  แล้วหาว่าเมื่อกฤษฎาหันหลังกลับมามองจะเห็นต้นไม้กี่ต้น

# อธิบาย Input :  A  <Heights>  แสดงถึงความสูงของต้นไม้  ,  B  คือการหันหลังกลับมามอง , S  คือการโดนผลกระทบจากเห็ดพิษ

# อธิบาย Test Case แรก : กฤษฎาจะเดินผ่านต้นไม้ความสูง  4   ก่อนแล้วตามด้วย  3   แล้วหันหลังกลับมามองจะเห็นต้นไม้ 2 ต้น ต่อมาเดินไปเจอต้นไม้สูง  5  กับ ต้นไม้สูง 8 ตามลำดับ  แล้วหันหลังกลับมามองจะเห็นแค่ต้นไม้ต้นเดียว  เนื่องจากต้น 8 เมตรบังต้นไม้ความสูง  4  3  และ  5 

# โดยจะรับประกันว่าจะมีต้นไม้อย่างน้อย 1 ต้นและมีการหันกลับมาอย่างน้อย 1 ครั้ง

# ไม่ได้เลือกไฟล์ใด

# Testcase : #1 1
# Enter Input : A 4,A 3,B,A 5,A 8,B
# 2
# 1

# Testcase : #2 2
# Enter Input : A 4,A 3,B,S,B,A 5,A 8,B
# 2
# 1
# 1

# Testcase : #3 3
# Enter Input : A 4,A 3,B,S,B,A 5,A 8,B,S,B
# 2
# 1
# 1
# 1

# Testcase : #4 5
# Enter Input : A 4,A 3,B,S,B,A 5,A 6,B,S,B
# 2
# 1
# 1
# 2

# Testcase : #5 7
# Enter Input : S,S,S,B,B,A 6,S,S,S,S,S,S,S,S,B
# 0
# 0
# 1

# Testcase : #6 9
# Enter Input : A 10,A 9,A 8,A 7,B,S,B,A 7,A 1,B,A 50,A 31,S,S,S,S,B
# 4
# 2
# 4
# 2

# Testcase : #7 ติด s มากกว่า 1 ครั้ง
# Enter Input : A 5,A 4,B,S,S,A 4,B
# 2
# 3

# Testcase : #8
# Enter Input : A 3,A 4,B,S,S,S,S,S,B
# 1
# 2

def process_inputs(inputs):
    heights = []
    results = []
    
    for command in inputs:
        if command.startswith("A"):
            height = int(command.split()[1])
            heights.append(height)
        elif command == "B":
            results.append(count_visible_trees(heights))
        elif command == "S":
            apply_mushroom_effect(heights)
    
    return results

def count_visible_trees(heights):
    max_height = 0
    visible_count = 0
    
    for height in reversed(heights):
        if height > max_height:
            visible_count += 1
            max_height = height
            
    return visible_count

def apply_mushroom_effect(heights):
    for i in range(len(heights)):
        if heights[i] % 2 == 1:
            heights[i] = max(1, heights[i] + 2)
        else:
            heights[i] = max(1, heights[i] - 1)

# Read input from user
input_string = input("Enter Input : ")
inputs = input_string.split(",")

# Process the inputs and get the results
results = process_inputs(inputs)

# Print the results
for result in results:
    print(result)

