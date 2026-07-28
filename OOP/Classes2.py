class Father:
    def __init__(self, name, occu):
        self.name = name
        self.occu = occu
    def greet(self, father):
        print(f"Hello son {self.name}, I am {father.name}")
f1 = Father("DAD", "Teach")
f2 = Father("BOB", "Learn")
f1.greet(f2)