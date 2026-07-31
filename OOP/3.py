from datetime import datetime

class Father:
    def __init__(self, name, occu):
        self._name = name
        self.occu = occu
    def infof(self):
        print(f"{self.name} and {self.occu}")

    # def get_name(self):
    #     print(f"Email accessed at {datetime.now()}")
    #     return(self._name)
    
    @property
    def name(self):
        print(f"Email accessed at {datetime.now()}")
        return(self._name)
    
    @name.setter
    def name(self, newname):
        self._name = newname

    # def set_name(self, newname):
    #     self._name = newname

# class Child(Father):
#     def __init__(self, name, age, Father):
#         self.name = name
#         self.age = age
#         self.father = Father
#     def infoc(self):
#         print(f"father name {self.father.name}, father occu {self.father.occu}")
#     def greet(self, user):
#         print(f"{self.name} greets {user.name}")

fat1 = Father("Dad", "teacher")
# ch1 = Child("sid", 21, fat1)
# ch2 = Child("sam", 22, fat1)

# print(fat1.get_name())
# fat1.set_name("Papa")
print(fat1.name)
fat1.name = "newdadname"
print(fat1.name)
# ch1.greet(ch2)
# fat1.infof()
# ch1.infoc()