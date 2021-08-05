
def hello(name, age):
    print("Hello " + name + " you are " + str(age) + " years old\n\n")

hello("Jakov", 23)
hello("Filip", 22)

def cube(num):
    number = num*num*num
    return number


def squared(num):
    number = num*num
    return number


my_cubed_num = cube(3)
print(my_cubed_num)

my_squared_num = squared(9)
print(my_squared_num)
