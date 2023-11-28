#Lab7
#Q1
class Employee:
    def __init__(self, employeeName, employeeID, employeeDesignation):
        self.__employeeName = employeeName
        self.__employeeID = employeeID
        self.__employeeDesignation = employeeDesignation
        self.all_employee = []

    def add_employee(self):
        self.all_employee.append([self.__employeeID, [self.__employeeName,self.__employeeDesignation]])

    def remove_employee(self,employeeName):
        print("\n Employee has been removed")

        if self.__employeeName in Employee:
            Employee.remove(self.__employeeName)
        else:
            print ("Employee is not found")

    def getEmployeeDetails(self):
        print(f"name: {self.__employeeName}")
        print(f"ID: {self.__employeeID}")
        print(f"Designation: {self.__employeeDesignation}")

firstobj= Employee("Hashim","2","Video Editor")
firstobj.getEmployeeDetails()

class Branch:
    def __init__(self,employee):
        self.__employee1st = employee
        self.__BranchCode = 4599
        self.__Address = DoctorsHospital

    def addAccount(self):
        self.__obj_bank= Bank([self.__BranchCode, self.__Address])
        self.__obj_bank.addBranch()
    def removeAccount(self, code, address):
        self.__obj_bank = 
        




class Bank:
    def __init__(self,self.__Name,self.__Headoffice_Location,self.__Code,self.__BranchList,self.__AccountList):
        self.__Name = BankName
        self.__Headoffice_Location = Headoffice_Location
        self.__Code = Code
        self.__BranchList = []
        self.__AccountList = []

    def addBranch(self,branch):
        self.branch= self.__BranchList

    def removeBranch(self,branch):
        if self.__branch = 
        Bank.remove(self.__BranchList)
        
        
        

        
 
