# Incapsilation
class Person:

    # _age - protected property
    #__age - private property

    def __init__(self, name):
         self.name = name
         self.__age = 33

    def get_info(self):
        print(f'My name is: {self.name}. I am {self.__age} years old')

    # Age getter
    # def get_age(self):
    #     return self.__age

    # Age setter
    # def set_age(self, value):
    #     self.__age = value

    # Age getter (decorator)
    @property
    def age(self):
        return self.__age

    # Age setter (decorator)
    @age.setter
    def age(self, value):
        self.__age = value


pers1 = Person('Vilan')
# pers1.set_age(30)
print(pers1.age)
pers1.age = 77
pers1.get_info()