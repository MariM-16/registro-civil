class Person:
    def __init__(self,name, age):
        self.__name = name
        self.__age = age

    @property
    def name (self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        if value > 0:
            self.__age = value


p1 = Person("Juan",18)
print(p1.name)
p1.name = "Carlos"
print(p1.name)
