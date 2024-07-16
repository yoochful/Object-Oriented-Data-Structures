# Chapter : 4 - item : 4 - เดาใจไว้แล้วว่าเธอรักฉันแบบที่ฉันรัก

# สมมติว่านักศึกษาแอบชอบคนๆหนึ่งอยู่ โดยที่นักศึกษาและคนๆนั้นจะมีกิจกรรมและสถานที่ที่ไปแตกต่างกันในแต่ละวัน
# ให้นักศึกษาเขียนโปรแกรมที่จะหาว่าสิ่งที่นักศึกษาและคนๆนั้นทำในแต่ละวันจะทำให้ได้คบกันหรือไม่ โดยใช้ Queue

# กิจกรรม                                       สถานที่
# 0 = กินข้าว(Eat)                           0 = ร้านอาหาร(Res.)
# 1 = เล่นเกม(Game)                          1 = ห้องเรียน(ClassR.)
# 2 = ทำโจทย์ datastruc(Learn)              2 = ห้างสรรพสินค้า(SuperM.)
# 3 = ดูหนัง(Movie)                          3 = บ้าน(Home)

# โดยการรับ Input จะประกอบด้วย

# กิจกรรม:สถานที่(ของนักศึกษาและของคนๆนั้น) โดยในแต่ละวันจะคั่นด้วยเครื่องหมาย ,

# เช่น วันที่ 1 นักศึกษาไปกินข้าวที่ร้านอาหาร และ คนๆนั้นไปนั่งทำโจทย์ datastruc ที่ร้านอาหาร 
#        วันที่ 2 นักศึกษาไปเล่นเกมที่บ้าน และ คนๆนั้นไปดูหนังที่ห้างสรรพสินค้า
# จะได้ว่า 0:0 2:0,1:3 3:2

# ***มีการคิดคะแนนดังนี้***

# ·       กิจกรรมเดียวกันแต่คนละสถานที่      +1

# ·       สถานที่เดียวกันแต่ทำกิจกรรมต่างกัน   +2

# ·       กิจกรรมเดียวกันและสถานที่เดียวกัน    +4

# ·       ไม่เหมือนกันเลย                  - 5

# หากมีคะแนนมากกว่าหรือเท่ากับ 7 จะถือว่าได้คบกัน แต่ถ้าคะแนนน้อยกว่า 7 แต่มากกว่า 0 เป็นคนคุย น้อยกว่านั้นถือว่าเป็นได้แค่เพื่อน

# โดยในแต่ละขั้นตอนให้แสดงผลดังตัวอย่าง

# Testcase : #1
# Enter Input : 0:0 2:0,1:3 3:3,2:1 2:1
# My   Queue = 0:0, 1:3, 2:1
# Your Queue = 2:0, 3:3, 2:1
# My   Activity:Location = Eat:Res., Game:Home, Learn:ClassR.
# Your Activity:Location = Learn:Res., Movie:Home, Learn:ClassR.
# Yes! You're my love! : Score is 8.

# Testcase : #2
# Enter Input : 2:1 2:1
# My   Queue = 2:1
# Your Queue = 2:1
# My   Activity:Location = Learn:ClassR.
# Your Activity:Location = Learn:ClassR.
# Umm.. It's complicated relationship! : Score is 4.

# Testcase : #3
# Enter Input : 0:1 2:3,3:2 3:2
# My   Queue = 0:1, 3:2
# Your Queue = 2:3, 3:2
# My   Activity:Location = Eat:ClassR., Movie:SuperM.
# Your Activity:Location = Learn:Home, Movie:SuperM.
# No! We're just friends. : Score is -1.

# Testcase : #4
# Enter Input : 3:3 1:3,0:0 1:1,2:2 3:3,0:3 0:1
# My   Queue = 3:3, 0:0, 2:2, 0:3
# Your Queue = 1:3, 1:1, 3:3, 0:1
# My   Activity:Location = Movie:Home, Eat:Res., Learn:SuperM., Eat:Home
# Your Activity:Location = Game:Home, Game:ClassR., Movie:Home, Eat:ClassR.
# No! We're just friends. : Score is -7.

def about_input(input_str):
    days = input_str.split(',')
    my_activities = []
    your_activities = []
    for day in days:
        my_activity, your_activity = day.split()
        my_activities.append(my_activity)
        your_activities.append(your_activity)
    return my_activities, your_activities

def get_activity_name(activity):
    activity_map = {0: "Eat", 1: "Game", 2: "Learn", 3: "Movie"}
    return activity_map[int(activity)]

def get_location_name(location):
    location_map = {0: "Res.", 1: "ClassR.", 2: "SuperM.", 3: "Home"}
    return location_map[int(location)]

def calculate_score(my_activities, your_activities):
    score = 0
    result_details = []
    
    for my_activity, your_activity in zip(my_activities, your_activities):
        my_act, my_loc = map(int, my_activity.split(':'))
        your_act, your_loc = map(int, your_activity.split(':'))
        
        if my_act == your_act and my_loc == your_loc:
            score += 4
            result_details.append("4")
        elif my_act == your_act:
            score += 1
            result_details.append("1")
        elif my_loc == your_loc:
            score += 2
            result_details.append("2")
        else:
            score -= 5
            result_details.append("-5")
    
    return score, result_details

def relationship(score):
    if score >= 7:
        return "Yes! You're my love!"
    elif 0 < score < 7:
        return "Umm.. It's complicated relationship!"
    else:
        return "No! We're just friends."

input_str = input("Enter Input : ")
my_activities, your_activities = about_input(input_str)

my_queue_str = ", ".join(my_activities)
your_queue_str = ", ".join(your_activities)

my_activity_loc_str = ", ".join([f"{get_activity_name(act)}:{get_location_name(loc)}" for act, loc in [act.split(':') for act in my_activities]])
your_activity_loc_str = ", ".join([f"{get_activity_name(act)}:{get_location_name(loc)}" for act, loc in [act.split(':') for act in your_activities]])

score, result_details = calculate_score(my_activities, your_activities)
relationship_status = relationship(score)

print(f"My   Queue = {my_queue_str}")
print(f"Your Queue = {your_queue_str}")
print(f"My   Activity:Location = {my_activity_loc_str}")
print(f"Your Activity:Location = {your_activity_loc_str}")
print(f"{relationship_status} : Score is {score}.")
