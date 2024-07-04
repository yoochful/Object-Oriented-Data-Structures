# โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้

# 		Speed (km/h)		ระดับพายุ
# 			0-51.99			Breeze
# 			52.00-55.99		Depression
# 			56.00-101.99	Tropical Storm
# 			102.00-208.99	Typhoon
# 			>= 209			Super Typhoon

# โดยแสดงผลตามตัวอย่างการแสดงผล

# Test case 1 
#  *** Wind classification ***
# Enter wind speed (km/h) : 50
# Wind classification is Breeze.

# Test case 2 
#  *** Wind classification ***
# Enter wind speed (km/h) : 56.2
# Wind classification is Tropical Storm.

# Test case 3
#  *** Wind classification ***
# Enter wind speed (km/h) : 99.89
# Wind classification is Tropical Storm.

# Test case 4
#  *** Wind classification ***
# Enter wind speed (km/h) : 212
# Wind classification is Super Typhoon.

# Test case 5
#  *** Wind classification ***
# Enter wind speed (km/h) : 254.23
# Wind classification is Super Typhoon.

    
print(" *** Wind classification ***")
input = float(input("Enter wind speed (km/h) : "))

if input < 52.00 :
    print("Wind classification is Breeze.")
elif input < 56.00 :
    print("Wind classification is Depression")
elif input < 102.00 :
    print("Wind classification is Tropical Storm.")
elif input < 209 :
    print("Wind classification is Typhoon.")
else : 
    print("Wind classification is Super Typhoon.")