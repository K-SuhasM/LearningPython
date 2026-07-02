# def average(*numbers):
#     sum=0
#     for i in numbers:
#      sum=sum + (i)
#     return int(sum/len(numbers))

# c= average(5,5)
# print("The average is:", c)
#######################################################
# list= [1,2,3,4,5]
# print(list)
# l=[]
# while True:
#     x=int(input("Enter your number:  "))
#     if x==99:
#         break
#     l.append(x)
#     print(l)

#method1
# list=list+l      
# print(list)

#method2
# list.extend(l)
# print(list)

#####################################################

# list=[]
# while True:
#     x=int(input("Enter your number:  "))
#     if x==999:
#         break
#     list.append(x)
# print("Your numbers are:  ", list)

# list.sort(reverse=False)
# print("Your sorted numbers are:", list)
# list.sort(reverse=True)
# print("Your reverse sorted numbers are:", list)

tupe=("IND", "FRA", "USA")
print(tupe)

tup2list=list(tupe)
# print(type(tup2list))
tup2list.append("CHI")
print(tup2list)
tup2list.pop(3)
print(tup2list)
tup2list.insert(2, "BRAZ")
print(tup2list)
tupe=tuple(tup2list)
print("updates tuple  ", tupe)