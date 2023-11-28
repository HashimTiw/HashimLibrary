#---------------------------LAB5---------------------------------------
# Q1
print("Q1:-")
class CompStudents:
    type= "CS-Student"
    count_students=0

    def __init__(self,name,roll_number,CGPA):
        self.name= name
        self.roll_number= roll_number
        self.CGPA= CGPA
        CompStudents.count_students +=1

    def view_info(self):
        print(f"Type: {CompStudents.type}")
        print(f"Name Of Student: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"CGPA: {self.CGPA}")


#students
Student_1= CompStudents("Hashim","261961881","3.072")

Student_2= CompStudents("Ali","251678449","2.06")

Student_3= CompStudents("Hashir","235665645","3.14")

print("-----------------------------------------------")
Student_1.view_info()
print("-----------------------------------------------")
Student_2.view_info()
print("-----------------------------------------------")
Student_3.view_info()
print("-----------------------------------------------")

print(f"Total number of Students are: {CompStudents.count_students}")

#Q3
print("///////////////////////////////////////////")


print("Q3:-")

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.calculate_slope_intercept()



#Q2
print("Q2:- ")

class Salary:
    def __init__(self,amount,bonus):
        self.amount = amount
        self.bonus = bonus

class Employee:
    def __init__(self,ID,Designation):
        self.ID = ID
        self.Designation = Designation
        self.salary = None  

    def calc_bonus(self):
        if self.Designation == "H":
            return 5000
        elif self.Designation == "M":
            return 2500
        elif self.Designation == "L":
            return 1000
        else:
            return 

    def base_salary(self,amount):
        bonus=self.calc_bonus()
        self.salary= Salary(amount,bonus)


employee1 = Employee(ID=1, Designation="M")
employee2 = Employee(ID=2, Designation="L")
employee3 = Employee(ID=3, Designation="H")

employee1.base_salary(35000)
employee2.base_salary(10000)
employee3.base_salary(90000)

print("-----------------------------------------------")
print(f"Employee 1 Salary: {employee1.salary.amount}, Bonus - {employee1.salary.bonus}")
print("-----------------------------------------------")
print(f"Employee 2 Salary: {employee2.salary.amount}, Bonus - {employee2.salary.bonus}")
print("-----------------------------------------------")
print(f"Employee 3 Salary: {employee3.salary.amount}, Bonus - {employee3.salary.bonus}")
print("-----------------------------------------------")








