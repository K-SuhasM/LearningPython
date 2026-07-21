class Animal:
    def __init__(self, name, species):
      self.name=name
      self.species=species

    def info(self):
        return(f"The animal's name is {self.name} of {self.species} species")

class Cat (Animal):
    def __init__(self, name, species, whiskers, height):
        super().__init__(name, species)
        self.whiskers=whiskers
        self.height=height
    
    def info(self):
       return f"{super().info()} It has {self.whiskers} whiskers and height is {self.height}"

a= Cat("billi", "Manzar", "6", "20cm")

print(Cat.info(a))