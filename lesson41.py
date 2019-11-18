# Polymorphism
class Person:

    def __init__(self, name, age):
         self.name = name
         self.age = age

    def get_info(self):
        print(f'My name is: {self.name}. I am {self.age} years old')


pers1 = Person('Vilan', 30)


# Class Employee inherit class Person
class Employee(Person):
    
    def __init__(self, name, age, company):
        super().__init__(name, age)
        self.company = company


    def get_info(self):
        super().get_info()
        print('Add line to employee object method get_info()')

    def more_info(self):
        print(f'{self.name} works in {self.company}')


employee = Employee('Test', 55, 'Privatix')
employee.get_info()
employee.more_info()