def add_two_numbers(num1, num2):
    print(int(num1) + int(num2))

add_two_numbers(10,20)


nums = [1,2,3,4,5,6]

def filter_odd_numbers(num):
    return num % 2 ==1

odd_numbers = list(filter(filter_odd_numbers,nums))
odd_numbers = list(filter(lambda num: num %2 == 1,nums))

print(odd_numbers)

def double_number(num):
    return num*2

doubled_numbers = list(map(lambda num : num*2 , nums))
print(doubled_numbers)


def something(student, *args):
    print(student)
    print(args[1])

something("Ali",4,"Mohammad",8)


# (normal parameters, *args, **kwargs)
def second_function(**kwargs):
    print(kwargs["last_name"])

second_function(first_name="Omar",last_name="Kamal")


def last_function(first_name, *args,**kwargs):
    print(first_name)
    print(args)
    print(kwargs)

last_function("Ali",1,2,5,8,course="SEB",teacher="Omar")


print(max(1,5,8))

print(sum([1,2,3]))