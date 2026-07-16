# class employee:
#     def __init__(self, name, id, age):
#         self.__name = name
#         self.id = id
#         self.age = age

#     def details(self):
#         print(f"The id of {self.name}, {self.age} is {self.id}  ")

# class workers (employee):
#     def __init__(self, date):
#         self.date=date
    
#     def detailsw(self):
#         print(f"Joining date of worker is {self.date}")

# e = employee("Rohan", 2354, 32)
# f = employee("Sam", 4734, 98)
# g = employee("Karan", 7364, 51) 
# h = employee("Ritesh", 8955, 36) 
# h = workers(2019)
# h.detailsw()
# print(f._employee__name)


class k:
    def __init__(self,num):
        self.num=num
    def addto(self,n):
        self.num=self.num+n
    @staticmethod
    def add(a,b):
        return a+b

a = k(5)
print (a.num)
a.addto(6)
print (add(9,9))