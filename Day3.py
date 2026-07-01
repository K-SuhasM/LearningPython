# a = "hey"
# b = input("Find: ")

# for i in a:
#     if i == b:
#         print("Found")
#         break
# else:
#     print("Not found")

# s = "hello mmy name is abcd"
# a = input("Find: ")
# b = s.find(a)
# print("The index is ", b)

# age = int(input("Enter your age: "))
# print("Your age is:", age)

# if 18<age<21:
#     print("You can drive!" )
# elif age==100:
#     print("yes")
# elif age==99:
#     print("100 after 1 year")

# else:
#     print("You cannot drive!!", )

# if age>21:
#     print("you can drink, but dont")
# else:
#     print("You cannot drink, dont drink")

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = time.strftime('%H')
print(hour)
if 00>int(hour)>12:
    print("Good morning")
if hour==00:
    print("Good night")
elif 12<=int(hour)<18:
    print("Good afternoon")
elif 18<=int(hour)<20:
    print("Good evening")
else:
    print("Good night")


# time = int(input("Enter the time in 24 hour format: "))
# print("The time is", time)

# if 00<time<12:
#     print("Good morning")
# elif 12<time<18:
#     print("Good afternoon")
# elif 18<time<20:
#     print("Good evening")
# else:
#     print("Good night")
