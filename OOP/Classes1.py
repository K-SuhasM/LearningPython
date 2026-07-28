

class Friend:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Dog:
    def __init__(self, name, breed, color, Friend):
        self.name = name
        self.breed = breed
        self.color = color
        self.friend = Friend
    def intro(self):
        print(f"Doggy's name is {self.name}, he is a {self.color} {self.breed}. His friend is {self.friend.name} living in {self.friend.address}")
    def bark(self):
        print(f"{self.name} barks Woof woof.")
    def sit(self):
        print(f"{self.name} sat down.\n")

fr1 = Friend("Koustubh", ("Maharashtra, India"))
dog1 = Dog("Oggy", "German", "Black", fr1)
fr2 = Friend("Sneha", ("Gujarat, India"))
dog2 = Dog("Tommy", "Neri", "White", fr2)

dog1.intro()
dog2.intro()
# print(dog1.friend.name)
# print(dog1.name, dog1.breed, dog1.color)
# dog1.intro()
# dog1.bark()
# dog1.sit()
# print(dog2.name, dog2.breed, dog2.color)
# dog2.intro()
# dog2.bark()
# dog2.sit()


    
