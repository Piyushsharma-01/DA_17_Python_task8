# Examples of encapsulation in Python:

# Example 1:
print("Example 1 Output: ")

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Method Protected

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    def __update_log(self):  # Method Private
        print("Transaction logged")

account = BankAccount("Anil", 10000)
account.deposit(5000)
print(account.get_balance())


# Example 2:
print("")
print("Example 2 Output: ")

class Car:
    def __init__(self):
        self._engine_condition = "Good"  # Method Protected
        self.__fuel_qty = 50  # Method Private

    def start(self):
        if self.__fuel_qty > 0:
            self._engine_condition = "Engine ON!"
            self.__burn_feul()

    def __burn_feul(self):  # Method Private
        self.__fuel_qty -= 40

car = Car()
car.start()
print(car._engine_condition) 
    
# Example 3:
print("")
print("Example 3 Output: ")

class Employee:
    def __init__(self,empName,salary,designation):
        self._empName = empName  # Method Protected
        self.__salary = salary  # Method Private
        self.__designation = designation

    def showSalary(self):
        return self.__salary
    
    def __calaculateBonus(self):
        return self.__salary * 0.1
    
    def showDesignation(self):
        return self.__designation
    
emp = Employee("Jahnvi", 50000, "Data Scientist")
print(emp._empName) 
print(emp.showSalary()) 
    
# Example 4:
print("")
print("Example 4 Output: ")

class Library:
    def __init__(self):
        self.__books = []  # Method Private
        self._members = []  # Method Protected
    
    def addBooks(self,books):
        self.__books.extend(books)
    
    def showBooks(self):
        return self.__books
    
books = ["Python Basics", "Data Science with Python", "Machine Learning", "Deep Learning Fundamentals"]
library = Library()
library.addBooks(books)
print(library.showBooks()) 

# Example 5:
print("")
print("Example 5 Output: ")

class Student:
    def __init__(self, StudName, Age):
        self._name = StudName  # Method Protected
        self.__age = Age  # Method Private

    def get_name(self):
        return self._name

    def __get_age(self):  # Method Private
        return self.__age
    
student = Student("Rahul", 20)
print(student.get_name())