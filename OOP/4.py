class Father:
    count = 0
    def __init__(self, name, occu):
        self._name = name
        self.occu = occu
        Father.count =+ 1

    @property
    def name(self):
        print("NAME ACCESSED")
        return (self._name)

    @name.setter
    def name(self, newname):
        self._name = newname


f1 = Father("Dad", "Teacher")

print(Father.count)
f1.name = "ddddddddddddd"
print(f1.name)