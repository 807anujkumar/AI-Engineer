
class Person:
    def __init__(self,name,age):
        self.name=name,
        self.age=age
        
    def Anuj_kumar(self):
        print(self)
        print( self.name, self.age)

p1=Person("anuj",30)
p1.Anuj_kumar()

class anuj(Person):
    def __init__(self,name,age,gender):
        super().__init__(name,age)
        self.gender=gender


p2=anuj("Anuj Kumar",30,"Male")
print(p2.name,p2.age,p2.gender)
