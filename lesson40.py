# Inheritance
class Person:

    def __init__(self, name):
         self.name = name
         self.age = 33

    def get_info(self):
        print(f'My name is: {self.name}. I am {self.__age} years old')


pers1 = Person('Vilan')


# Class Employee inherit class Person
class Employee(Person):
    company = 'Google'

    def more_info(self):
        print(f'{self.name} works in {self.company}')


employee = Employee('Test')
employee.more_info()