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

def insert_all_positions(lst, item):
    result = []
    for i in range(len(lst) + 1):
        new_lst = lst[:]
        new_lst.insert(i, item)
        result.append(new_lst)
    return result

def permute(nums):
    if len(nums) == 1:
        return [nums]
    
    last_item = nums[-1]
    prev_permutations = permute(nums[:-1])
    result = []
    for perm in prev_permutations:
        result.extend(insert_all_positions(perm, last_item))
    return result

print("*** Fun with permute ***")
print("input : ", end="")
a = list(map(int, input().split(',')))
print("Original Cofllection: ", a)
result = permute(a)
print("Collection of distinct numbers:\n", result)


