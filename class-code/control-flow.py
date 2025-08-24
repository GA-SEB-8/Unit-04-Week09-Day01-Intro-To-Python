
# equality
print(7 == 7)

# not equal
print(7 != 7)



print(9 > 3 and 5 < 6)

# ! == not
# || == or
# && == and
print( not 5 > 4)



# if Statements in Python
# my_teacher = input("Enter Teacher Name: ").lower()
my_teacher = "omar"

if my_teacher == "omar":
    print("You are teaching Unit 2 and 4")
elif my_teacher == "george":
    print("You are teaching Unit 1 and 3")
else:
    print("You dont have to teach any Units :)")

print("Something")



# Loops

# start at 3 and stop at 10
for i in range(3,10):
    print(i)


# Go up by 2 every time
for i in range(3,10,2):
    print(i)


# Go down by 2 every time
for i in range(10,3,-2):
    print(i)


# looping through a list (array in js)
my_students = ["yaqoob","maryam","jamal",'abdullah','ali']

print(my_students)

for student in my_students:
    if student == "jamal":
        break
    print(f"{student} is in software engineering")




