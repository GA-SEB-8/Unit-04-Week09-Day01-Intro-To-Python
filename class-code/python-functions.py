def add_two_numbers(num1, num2):
    print(int(num1) + int(num2))

add_two_numbers(10,20)


nums = [1,2,3,4,5,6]

def filter_odd_numbers(num):
    return num % 2 ==1

odd_numbers = list(filter(filter_odd_numbers,nums))

print(odd_numbers)

def double_number(num):
    return num*2

doubled_numbers = list(map(double_number,nums))
print(doubled_numbers)