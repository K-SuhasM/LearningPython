class parent:
    def parentfunc (self):
        print("PARENT")

class child (parent):
    def childfunc (self):
        print("CHILD")
        self.parentfunc()   

obj=child()
obj.childfunc()

