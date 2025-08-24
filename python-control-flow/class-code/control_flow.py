print(7!=7)
print(7>7)

print(7>=7)

# and, or
print(True or False)
print(False or False)
print(True and False)
print(True and True)



# ! is the same as not in python

my_name = "Sayed"
print(not my_name == "Youseph")


# if statements

age = 105

if age < 18:
    print("You are too young to drive")
elif age >99:
    print("You are too old sir sorry. no car")
else:
    print("You are good to drive")


# my_country = input("Please give your country").lower()
# print(f"Wow what a great country {my_country}")

# color = input('Enter "green", "yellow", "red": ').lower()
# print(f'The user entered {color}')


# if color == "green":
#     print("Go")
# elif color == "red":
#     print("stop")
# elif color == "yellow":
#     print("Slow down")
# else:
#     print("Bogus")






# Looping

students = ["Sayed","Youseph","Isra","Malak"]

for one_student in students:
    print(one_student)


num = 1
while num <=10:
    print(num)
    num+= 1

students = ["Sayed","Youseph","Isra","Malak"]

for one_student in students:
    if one_student == "Isra":
        break
    elif one_student == "Sayed":
        continue
    print(one_student + " Is here")




# ranges:

# start at 0 end at 5
for num in range(5):
    print(num)

print("-----------")
#  start at 1 and end at 5 (not including)
for num in range(1,5):
    print(num)
print("-----------")


# (start, stop, step)
for num in range(1,10,4):
    print(num)

# going from end to start
for num in range(10,1,-3):
    print(num)


