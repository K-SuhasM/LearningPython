# x = int(input("Number 1 "))
# y = int(input("Number 2 "))

# z = (x,y)
# print(z)
# match z:
#     case (1,3):
#         print("The number is 0")
#     case (x,4):
#         print("The number is 1")
#     case (_) if z==(6,7):
#         print("67")

# x= int(input("Enter the number: "))
# print("You chose the number ", x)
# match x:
#     case 1:
#         print("The first month of an year is January.")
#     case 2:
#         print("The second month of an year is February.")
#     case 3:
#         print("The third month of an year is March.")

#     case 4:
#         print("The fourth month of an year is April.")
#     case 5:
#         print("The fifth month of an year is May.")
#     case 6:
#         print("The sixth month of an year is June.")
#     case 7:
#         print("The seventh month of an year is July.")
#     case 8:
#         print("The eighth month of an year is August.")
#     case 9:
#         print("The ninth month of an year is September.")
#     case 10:
#         print("The tenth month of an year is October.")
#     case 11:
#         print("The eleventh month of an year is November.")
#     case 12:
#         print("The twelfth month of an year is December.")
#     case _:
#         print("Please enter a number from 1-12.")

# if x==9:
#     print("Congratulations, its your birthmonth")

# name=input("Enter your name: ")
# print("Your name is", name)
# print("The letters in your name are")
# for i in name:
#     seppp=", "
#     endd="and "
#     if i==name[len(name)-1]:
#         endd="and " 
#     else: 
#         endd=" "
#     print(i, end=seppp, sep=endd)

# for i in range(0, 10, 1):
#     print(i)

# colors=["red", "pink", "blue"]
# for i in colors:
#     print(i)

# i-5
# while (i>0):
#     i=i-1
#     print(i)

# i=int(input("Enter your number: "))
# while i!=7:
#     print("Sorry pleasee try again")
#     i=int(input("Enter your number: "))
# else: print("Congratulations you won")  

i=1
for i in range(20):
    print(i)
    i=i+1
    if i==10:
        break
    # else:
    #     continue