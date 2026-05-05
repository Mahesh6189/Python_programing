class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name=",self.name)
        print("age=",self.age)
s1=student("Mahesh",21)
s1.show()