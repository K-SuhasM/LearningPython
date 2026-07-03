# import time

# x = time.strftime('%H')
# print(x)

# print("The time is", time.strftime('%H:' '%M:' '%S'))

# if 00<=int(x)<12:
#         print("Good Morning")
# elif 12<=int(x)<17:
#         print("Good Afternoon")
# elif 17<=int(x)<20:
#         print("Good Evening")
# elif 20<=int(x)<00:
#         print("Good Night")
# else:
#     print("Have a nice day")
####################################################################################################
# ques= ["What is the capital of France? ", 
#        "Which planet is known as the Red Planet? ", 
#        "How many days are there in a leap year? ", 
#        "Which animal is known as the King of the Jungle? "]
# ans1= ['A. Madrid ', "B. Berlin ", "C. Paris ", "D. Rome "]
# ans2= ["A. Venus ", "B. Jupiter ", "C. Saturn ", "D. Mars "]
# ans3= ["A. 365 ", "B. 364 ", "C. 360 ", "D. 366 "]
# ans4= ["A. Tiger ", "B. Elephant ", "C. Bear ", "D. Lion "]

# prize=[]
# answers=[]

# #Question 1
# print("Question 1. ", ques[0])
# for i in ans1:
#     print(i)

# inp1=int(input("Enter your answer: "))
# if inp1==3:
#     answers.append(1)
#     prize.append(500)
#     print("correct!!", "You won ", "Rs.", prize[0] )
# else:
#     prize.append(00)
#     print("Sorry, you lost", "Your winning amount is Rs.", prize[0]),

# #Question 2
# if 1 in answers:
#     print("Question 2. ", ques[1])
#     for i in ans2:
#       print(i)

#     inp2=int(input("Enter your answer: "))
#     if inp2==4:
#         answers.append(1)
#         prize.append(500)
#         print("correct!!", "You won ", "Rs.", sum(prize))
#     else:
#         answers.pop()
#         prize.append(00)
#         print("Sorry, you lost", "Your winning amount is Rs.", sum(prize))

# #Question 3
# if 1 in answers:
#     print("Question 3. ", ques[2])
#     for i in ans3:
#       print(i)

#     inp3=int(input("Enter your answer: "))
#     if inp3==4:
#         answers.append(1)
#         prize.append(500)
#         print("correct!!", "You won ", "Rs.", sum(prize))
#     else:
#         answers.pop()
#         answers.pop()
#         prize.append(00)
#         print("Sorry, you lost", "Your winning amount is Rs.", sum(prize))

# #Question 4
# if 1 in answers:
#     print("Question 4. ", ques[3])
#     for i in ans4:
#       print(i)

#     inp4=int(input("Enter your answer: "))
#     if inp4==4:
#         answers.append(1)
#         prize.append(500)
#         print("correct!!", "You won ", "Rs.", sum(prize))
#     else:
#         answers.pop()
#         answers.pop()
#         answers.pop()
#         prize.append(00)
#         print("Sorry, you lost", "Your winning amount is Rs.", sum(prize))
###################################################################################################

# x=input("Enter name:  ")
# y=input("Enter name:  ")
# mname=x+y
# cntry=input("Enter country:  ")
# inc=float(input("Enter income:  "))

# name=f"Hello my name is '{mname}'. I am from {cntry}. My income is Rs.{inc: .3f}. "


# print(name)
###################################################################################################

# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
###################################################################################################

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (n-1) + (n-2)
    
print(fibo(5))







