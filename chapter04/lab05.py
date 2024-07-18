# Chapter : 4 - item : 5 - Search Portal
# พี่ซันฟงได้รับคำสั่งจากอาจารย์ให้ออกโจทย์เขียนโปรแกรมให้แก่น้องๆ พี่จึงกลับไปนอนคิดที่บ้าน รู้สึกตัวอีกทีก็อยู่ในห้องมืดๆ พี่สามารถมองเห็นและเดินไปยังพื้นที่ที่อยู่ติดกันได้ (4 ทิศ เหนือ ใต้ ออก ตก) พี่จะต้องหาประตูทางออกจากฝันเพื่อไปส่งโจทย์ให้กับอาจารย์ ต่อมาพี่ก็คิดวิธีในการเดินหาประตูทางออกได้โดยใช้วิธีหาแบบ Breadth First Search โดยพี่จะเริ่มยืนในจุดเริ่มต้นแล้วมองหาและจำทางเริ่มจากทิศเหนือ ทิศตะวันออก ทิศใต้ ทิศตะวันตก ตามลำดับ แล้วเดินไปยังช่องถัดไปแล้วหาใหม่ ในเมื่อคิดวิธีออกแล้วพี่จึงต้องการโปรแกรมที่จะบอกพี่ว่าสามารถไปถึงทางออกได้หรือพี่จะต้องติดอยู่ในฝันไปตลอดกาล ปัญหาคือพี่ขี้เกียจเขียนโค้ด พี่เลยอยากให้น้องๆเขียนโค้ดให้พี่หน่อย เขียนสวยๆกะทัดรัด ไม่งั้นจะส่งกลับไปเขียนใหม่
# โดยรายละเอียดโปรแกรมจะมีดังนี้
# Input
# รับความกว้าง ความสูง และแผนที่ โดยแผนที่แต่ละบรรทัดจะขั้นด้วย ','
# ตัวอย่าง input: 3 3 F__,##_,O__
# จะมีความหมายว่าแผนที่กว้าง 3 สูง 3 และแผนที่จะเป็นแบบนี้
# F__
# ##_
# O__
# ภายในแผนที่
# 'F' แทนตำแหน่งเริ่มต้นของพี่
# 'O' แทนประตูทางออก
# '_' แทนพื้นที่ที่สามารถเดินได้
# ตัวอักษรอื่นๆทั้งหมดแทนกำแพง ไม่สามารถเดินไปที่ช่องนั้นได้
# Output
# หากไม่มีพี่ (F) อยู่ในห้องหรือแผนที่ที่ใส่เข้ามาไม่ตรงกับขนาดของ width ให้แสดงว่า "Invalid map input."
# แสดง queue ระหว่างหาทางออก
# ถ้าหาทางออกเจอให้แสดงว่า "Found the exit portal."
# ถ้าหาไม่เจอให้แสดงว่า "Cannot reach the exit portal."

# Testcase : #1 1
# Enter width, height, and room: 6 4 F__###,##_###,##__##,###__O
# Queue: [(0, 0)]
# Queue: [(1, 0)]
# Queue: [(2, 0)]
# Queue: [(2, 1)]
# Queue: [(2, 2)]
# Queue: [(3, 2)]
# Queue: [(3, 3)]
# Queue: [(4, 3)]
# Found the exit portal.

# Testcase : #2 Bigger Area
# Enter width, height, and room: 8 6 ########,##___###,##_F_###,##____##,##_##_O_,##______
# Queue: [(3, 2)]
# Queue: [(3, 1), (4, 2), (3, 3), (2, 2)]
# Queue: [(4, 2), (3, 3), (2, 2), (4, 1), (2, 1)]
# Queue: [(3, 3), (2, 2), (4, 1), (2, 1), (4, 3)]
# Queue: [(2, 2), (4, 1), (2, 1), (4, 3), (2, 3)]
# Queue: [(4, 1), (2, 1), (4, 3), (2, 3)]
# Queue: [(2, 1), (4, 3), (2, 3)]
# Queue: [(4, 3), (2, 3)]
# Queue: [(4, 3), (2, 3)]
# Queue: [(2, 3), (5, 3)]
# Queue: [(5, 3), (2, 4)]
# Queue: [(2, 4), (5, 4)]
# Queue: [(5, 4), (2, 5)]
# Found the exit portal.

# Testcase : #3 Mid Fing
# Enter width, height, and room: 3 3 ###,######F,###
# Invalid map input.

# Testcase : #4 Less Path
# Enter width, height, and room: 3 3 F__,##_,O_
# Invalid map input.

# Testcase : #5 Only One
# Enter width, height, and room: 1 1 F
# Queue: [(0, 0)]
# Cannot reach the exit portal.

# Testcase : #6 There
# Enter width, height, and room: 2 1 FO
# Queue: [(0, 0)]
# Found the exit portal.

# Testcase : #7 Barrier
# Enter width, height, and room: 5 3 __|__,F_|_O,__|__
# Queue: [(0, 1)]
# Queue: [(0, 0), (1, 1), (0, 2)]
# Queue: [(1, 1), (0, 2), (1, 0)]
# Queue: [(0, 2), (1, 0), (1, 2)]
# Queue: [(1, 0), (1, 2)]
# Queue: [(1, 2)]
# Cannot reach the exit portal.

# Testcase : #8 Bridge
# Enter width, height, and room: 10 7 F_____\...,===\___\..,...#\___\.,....#|___|,...#/___/.,===/___/..,O_____/...
# Queue: [(0, 0)]
# Queue: [(1, 0)]
# Queue: [(2, 0)]
# Queue: [(3, 0)]
# Queue: [(4, 0)]
# Queue: [(5, 0), (4, 1)]
# Queue: [(4, 1), (5, 1)]
# Queue: [(5, 1)]
# Queue: [(6, 1), (5, 2)]
# Queue: [(5, 2), (6, 2)]
# Queue: [(6, 2)]
# Queue: [(7, 2), (6, 3)]
# Queue: [(6, 3), (7, 3)]
# Queue: [(7, 3), (6, 4)]
# Queue: [(6, 4), (8, 3), (7, 4)]
# Queue: [(8, 3), (7, 4), (6, 5), (5, 4)]
# Queue: [(7, 4), (6, 5), (5, 4)]
# Queue: [(6, 5), (5, 4)]
# Queue: [(5, 4), (5, 5)]
# Queue: [(5, 5)]
# Queue: [(5, 6), (4, 5)]
# Queue: [(4, 5), (4, 6)]
# Queue: [(4, 6)]
# Queue: [(3, 6)]
# Queue: [(2, 6)]
# Queue: [(1, 6)]
# Found the exit portal.


class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    return self.queue.pop(0)

  def is_empty(self):
    return self.queue == []

  def size(self):
    return len(self.queue)

  def first(self):
    return self.queue[0]

  def last(self):
    return self.queue[-1]


def search_portal(width, height, room):
  queue = Queue()
  visited = []

  if len(room) != height:
    print("Invalid map input.")
    return

  for i in room:
    if len(i) != width:
      print("Invalid map input.")
      return

  for i, floor in enumerate(room):
    for j, tile in enumerate(floor):
      if tile == 'F':
        queue.enqueue((j, i))
        visited.append((j, i))

  if queue.is_empty():
    print("Invalid map input.")
    return

  while True:
    if queue.is_empty():
      print('Cannot reach the exit portal.')
      break

    print(f'Queue: {queue.queue}')

    currentX, currentY = queue.first()[0], queue.first()[1]

    if currentY > 0 and room[currentY-1][currentX] == '_' and (currentX, currentY-1) not in visited:
      queue.enqueue((currentX, currentY-1))
      visited.append((currentX, currentY-1))

    if currentX < width - 1 and room[currentY][currentX+1] == '_' and (currentX+1, currentY) not in visited:
      queue.enqueue((currentX+1, currentY))
      visited.append((currentX+1, currentY))

    if currentY < height - 1 and room[currentY+1][currentX] == '_' and (currentX, currentY+1) not in visited:
      queue.enqueue((currentX, currentY+1))
      visited.append((currentX, currentY+1))

    if currentX > 0 and room[currentY][currentX-1] == '_' and (currentX-1, currentY) not in visited:
      queue.enqueue((currentX-1, currentY))
      visited.append((currentX-1, currentY))

    if currentY > 0 and room[currentY-1][currentX] == 'O' and (currentX, currentY-1) not in visited:
      print('Found the exit portal.')
      break

    if currentX < width - 1 and room[currentY][currentX+1] == 'O' and (currentX+1, currentY) not in visited:
      print('Found the exit portal.')
      break

    if currentY < height - 1 and room[currentY+1][currentX] == 'O' and (currentX, currentY+1) not in visited:
      print('Found the exit portal.')
      break

    if currentX > 0 and room[currentY][currentX-1] == 'O' and (currentX-1, currentY) not in visited:
      print('Found the exit portal.')
      break

    queue.dequeue()


if __name__ == '__main__':
  width, height, room = input('Enter width, height, and room: ').split()

  search_portal(int(width), int(height), room.split(','))