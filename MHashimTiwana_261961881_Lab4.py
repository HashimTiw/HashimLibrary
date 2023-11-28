#LAB4
#Question1
def countEvenNumbers(n):
    if n==[]:
        return 0
    else:
        return (1 if n[0] % 2 == 0 else 0) + countEvenNumbers(n[1:])

list1=[1,2,3,4,5,6,7,8,9,10,12,14]
result=countEvenNumbers(list1)

print(f"The number of even numbers in the list is: ")
print(countEvenNumbers(list1))

#Question2
class myclass:
    def __init__(self,x):
        self.x = x
p1= myclass(16)

print(p1.x)


#Question3
class bookstore:
    def __init__(self,title,author,publisher):
        self.title = title
        self.author = author
        self.publisher = publisher

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publisher(self):
        return self.publisher

    def set_title(self,title):
        self.title = title

    def set_author(self,author):
        self.author = author

    def set_publisher(self,publisher):
        self.publisher = publisher

    def bookinfo(self):
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Publisher: {self.publisher}')

firstbook=bookstore("Harry Potter","Ahmed","FCCU")
print(firstbook.bookinfo())


#Question4
class calculator:
    def __init__(self,n1,n2):
        self.n1= n1
        self.n2= n2

    def add_numbers(self):
        return self.n1 + self.n2

    def sub_numbers(self):
        return self.n1 - self.n2

    def mul_numbers(self):
        return self.n1 * self.n2

    def divide_numbers(self):
        if self.n2 != 0:
            return self.n1/self.n2
        else:
            return "This number cannot be divided"


n1 = 30
n2 = 15

calc = calculator(n1,n2)
print(f"Addition: {calc.add_numbers()}")
print(f"Subtraction: {calc.sub_numbers()}")
print(f"Multiplication: {calc.mul_numbers()}")
print(f"Division: {calc.divide_numbers()}")








        





