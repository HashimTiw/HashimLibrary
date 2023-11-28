#ASSIGNMENT 2
#COMP 102 SECTION B
#HASHIM TIWANA
#261961881

#1.LOOPS
def Q1():
    n=input("Enter value of n: ")
    n=int(n)
    total_sum=0
    for i in range(1, n+1):
        total_sum = total_sum + i
        print("Total sum is: ", total_sum)

#2.Conditions(Decision Constructs):
def Q2():
    num=int(input("Enter any number: "))
    if num % 2==0:
        print("The number is even")
    else:
        print("The number is odd")
    
#3. Data Types(Strings,Integers,Floats)
def Q3a():
    str1=str(input("Enter any string: "))
    count=0
    for i in str1:
        count += 1
    print(count)
    print(str1[::-1])

def Q3b():
    num1=int(input("Enter first number: "))
    num2=float(input("Enter second number: "))
    print(num1 + num2)
    print(num1 - num2)
    print(num1 * num2)
    print(num1 / num2)

#4. Recursion

def Q4():
    v = int(input("Enter a positive integer: "))
    def factorial(n):
            if n==0:
                return 1
            else:
                return n * factorial(n-1)

    print(factorial(v))

#5. Object Oriented Programming

def Q5():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    person_instance = Person(name="Hashim", age=19)

    print("Full Name:", person_instance.name)
    print("Years Old:", person_instance.age)


#6. Relationships (Association, Aggregation, Composition)

def Q6():
#1.Association
    class Student:
        def __init__(self, name):
            self.name = name

    class Course:
        def __init__(self, title):
            self.title = title

    class Enrollment:
        def __init__(self, student, course):
            self.student = student
            self.course = course

    student1 = Student("YOUSAF")
    course1 = Course("COMP-111")

    enrollment1 = Enrollment(student1, course1)
    print(f"{enrollment1.student.name} is enrolled in {enrollment1.course.title}")

#2.Aggregation
    class Professor:
        def __init__(self, name):
            self.name = name

    class Department:
        def __init__(self, name):
            self.name = name
            self.professors = []

        def add_professor(self, professor):
            self.professors.append(professor)

    class University:
        def __init__(self, name):
            self.name = name
            self.departments = []

        def add_department(self, department):
            self.departments.append(department)

    professor1 = Professor("Sharon Nasim")
    department1 = Department("Computer Science")
    department1.add_professor(professor1)

    university1 = University("FCCU")
    university1.add_department(department1)

    print(f"{professor1.name} is in the {department1.name} department at {university1.name}")

#3.Composition
    class Engine:
        def __init__(self, horsepower):
            self.horsepower = horsepower

    class Car:
        def __init__(self, make, model, horsepower):
            self.make = make
            self.model = model
            self.engine = Engine(horsepower)

        def get_car_details(self):
            return f"{self.make} {self.model} with {self.engine.horsepower} horsepower"

    car1 = Car("CHEVROLET", "CORVETTE", 900)
    print(f"The car details: {car1.get_car_details()}")

#7. Inheritance and Its Types

def Q7():
#single inheritance
    class Vehicle:
        def __init__(self, make, model):
            self.make = make
            self.model = model


    class Car(Vehicle):
        def __init__(self, make, model, manufacture_year):
            Vehicle.__init__(self, make, model)
            self.manufacture_year = manufacture_year

    car_instance = Car(make="Toyota", model="Yaris", manufacture_year=302)

    print("Make:", car_instance.make)
    print("Model:", car_instance.model)
    print("Manufacture Year:", car_instance.manufacture_year)

#multiple inheritances
    class Parent1:
        def __init__(self, attribute1):
            self.attribute1 = attribute1

    class Parent2:
        def __init__(self, attribute2):
            self.attribute2 = attribute2


    class Child(Parent1, Parent2):
        def __init__(self, attribute1, attribute2, child_attribute):
            
            Parent1.__init__(self, attribute1)
            Parent2.__init__(self, attribute2)
            self.child_attribute = child_attribute


    child_instance = Child(attribute1="qasim", attribute2="ali", child_attribute="children")


    print("Atb1 from Parent1:", child_instance.attribute1)
    print("Atb2 from Parent2:", child_instance.attribute2)
    print("Child Attribute:", child_instance.child_attribute)

#8. Method Overloading and Overriding
def Q8():
# Method Overloading
    class Calculator:
        def add(self, x, y):
            return x + y

        def add_multiple(self, *args):
            result = 0
            for num in args:
                result += num
            return result

        def subtract(self, x, y):
            return x - y

        def multiply(self, x, y):
            return x * y

        def divide(self, x, y):
            if y != 0:
                return x / y
            else:
                return "Cannot divide by zero."

    calculator_inst = Calculator()

    result1 = calculator_inst.add(5, 3)
    result2 = calculator_inst.add_multiple(1, 2, 3, 4)

    print("Result1:", result1)
    print("Result2:", result2)

# Method Overriding
    class Shape:
        def area(self):
            pass  
    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        def area(self):
            return 3.14 * self.radius ** 2

    class Rectangle(Shape):
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width

    circle_inst = Circle(radius=5)
    rectangle_inst = Rectangle(length=4, width=6)


    circle_area = circle_inst.area()
    rectangle_area = rectangle_inst.area()

    print("Circle Area:", circle_area)
    print("Rectangle Area:", rectangle_area)
