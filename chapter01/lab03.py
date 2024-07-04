# เขียนโปรแกรม Python เพื่อสร้างวิธีเรียงสับเปลี่ยนที่เป็นไปได้ทั้งหมดจากชุดตัวเลขที่กำหนด

# Test case 1
# *** Fun with permute ***
# input : 1,2,3
# Original Cofllection:  [1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]]

# Test case 2
# *** Fun with permute ***
# input : 1,1,2,3
# Original Cofllection:  [1, 1, 2, 3]
# Collection of distinct numbers:
#  [[3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3], [3, 2, 1, 1], [2, 3, 1, 1], [2, 1, 3, 1], [2, 1, 1, 3], [3, 1, 2, 1], [1, 3, 2, 1], [1, 2, 3, 1], [1, 2, 1, 3], [3, 1, 1, 2], [1, 3, 1, 2], [1, 1, 3, 2], [1, 1, 2, 3]]


input = input("Input: ")
input_list = list(map(int, input.split(',')))

def permute(num):
    result = []

    if len(num) == 0:
        return []
    
    if len(num) == 1:
        return [num]
    
    for i in range(len(num)):
        current_num = num[i]
        remaining_num = num[:i] + num[i+1:]
        for p in permute(remaining_num):
            result.append([current_num] + p)
    
    return result

permuted_list = permute(input_list)

print("Original Collection: ",input_list)
print("Collection of distinct numbers:")
print(permuted_list)