# print("Hello world")
# # Junious Barnes
# a = 4
# b = 3
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(6 / 2)
# print(3 ** 2)
#
# print()
# print("try to figure out how this works")
# print(10 % 5)
# # the "%" sign is a modulus. It finds the remainder.
# car_name = "The Wiebe Mobile"
# car_type = "BMW"
# car_cylinder = 8
# car_mpg = 5000.9
#
# print("I have a car Called %s. It's pretty nice." % (car_name)) # watch the order
#
# # Here is where we get a little fancy
# print("What is your name")
# name =input(">_")
# print("Hello %s."% name)
# age = input("How old are you?")
# print("%s?! Thats really old.You belong in a retirement home."%age)

# Functions


def  print_hw():
    print("Hello World")
    print ("Enjoy the day.")


print_hw()


def say_hi (name):  # Name is a "parameter"
    print("Hello %s" % name)
    print("Coding is great!")


say_hi("Junious")


def print_age(name,age):
    print("%s is %d years old" % (name, age))
    age = age + 1 # age = age + 1
    print ("Next year, %s will be %d years old" % (name, age))


print_age("Junious",14)



def algebra_hw (x):
    return x**3 + 4*x**2 + 7 * x -4

print(algebra_hw(3))

# if statements


def grade_calc (percentage):
    if percentage >=90:
        return "A"
    elif percentage >= 80 and percentage < 90: # else if
      return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

print(grade_calc(100))


def happy_bday(name) :
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear"+ name)
    print("Happy Birthday to you")

happy_bday("Junious")

# Loops

for num in range(10):
    print (num + 1)
a = 1
while a < 10:
    print(a)
    a += 1

# Random Numbers
import random  # This should be on line 1
print(random.randint(0, 1000))


c = '1'
print(c == 1)


# Recasting
c = '1'
print (c == 1)  # we have a string and an integer
print(int(c) == 1)
print (c == str(1))

# Comparisons

print(1 == 1)  # Use a double eqaul sign
print (1 !=2)  # 1 is not eqaul to 2
print (not False)

(Does number match guess
add "higher" and "lower"
add 5 guesses)
