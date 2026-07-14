# class person:
#     def __init__(self,n,s,no):
#         self.name=n
#         self.number=no
#         self.surname=s
#     # name = "koustubh"
#     # surname = "Mandle"
#     # number = 9893948036
#     def info(self):
#         print(f"{self.name}'s surname is {self.surname}, number is {self.number}")

# # print(person.name)
# # person.age=12
# a=person("Koustubh","Mandle", 9893948036)
# b=person("Sneha", "Mandle", 7041007606)
# c=person("Chiku", "Khandagale", 8889809185)

# # a.name="Koustubh"
# # a.surname="Mandle"
# # a.number=9893948036

# # b.name="Sneha"
# # b.surname="Mandle"
# # b.number=7041007606

# # c.name="chiku"
# # c.surname="Khandagale"
# # c.number=8889809185

# # print(a.name)
# # print(b.name)
# # print(c.name)

# a.info()
# b.info()
# c.info()



def greet(fx):
    def main():
        print("###########################################################")
        fx()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    return main

@greet
def add():
    num=input("Enter your numbers: ")
    numb=[]
    for i in num:
        i=int(i)
        numb.append(i)
    print(sum(numb))

add()