'''Create a class named 'Shape' with a method to printShape "This is shape". 
Then create two other classes named 'Rectangle', 'Circle' inheriting the Shape class,
both having a method to print "This is rectangle" and "This is circle" respectively. 
Create a child class 'Square' of 'rectangle' having a method to printSquare "Square is a rectangle". 
Now call the method of 'Shape' and 'Rectangle' class by the object of 'Square' class.'''
class Shape:
    def printShape(self):
        print("This is a sahpe")
class Rectangle(Shape):
    def printrect(self):
        print("this is rectangle")
class circle(Shape):
    def print(self):
        print("This is a circle")
class Square(Rectangle):
    def printSquare(self):
        print("square is rectangle")

obj=circle()
obj.print()
obj.printShape()
adc=Square()
adc.printSquare()
adc.printShape()
adc.printrect()
print("============================================================================================================================")

"""Create a class named 'Member' having the following attributes:
Data Attributes of Member Class
1 - Name
2 - Age
3 - Phone number
4 - Address
5 - Salary
It also has a method named 'printSalary' which prints the salary of the members.
Two classes 'Employee' and 'Manager' inherits the 'Member' class. The 'Employee' 
and 'Manager' classes have attributes 'specialization' and 'department' respectively.
Both these classes will also have a method print_details.
Print_details of Employee class will print name & 'specialization' and will also call the printSalary method.
Print_details of Manager class will print name & 'department' and will also call the printSalary method.
Now, assign name, age, phone number, address and salary to an employee and a manager by making an object of both of these classes.
and print the same.
Hint:- Use super method to call parent constructor"""

class member:
    def __init__(self, name, age, phone, address, salary):
        self.name=name
        self.age=age
        self.phone=phone
        self.address=address
        self.salary=salary
    def Printsalary(self):
        print(self.salary)

class Employee(member):
    def __init__(self, name, age, phone, address, salary, specialization):
        super().__init__(name,age,phone,address,salary)
        self.specialization=specialization
    
    def Print_details(self):
        print(self.name,self.specialization,end=" "),self.Printsalary()
        

class Manager(member):
    def __init__(self, name, age, phone, address, salary, department):
        super().__init__(name,age,phone,address,salary)
        self.department=department
    
    def Print_details(self):
        print(self.name)
        print(self.department)
        self.Printsalary()

def main():
    emp=Employee("Rahul", 25, 1234567890, "Banglore",45000,"cse")
    man=Manager("Rohan", 30, 9876543210, "Mumbai",50000,"civil")
    emp.Print_details()
    man.Print_details()
main()


print("============================================================================================================================")

class PARENT:
    def print(self):
        print("this is a parent class")
    
class CHILD(PARENT):
    def print(self):
        print("this is a child class")


def main():
    obj_parent = PARENT()
    obj_parent.print()
    
    obj_child = CHILD()
    obj_child.print()
    super(CHILD,obj_child).print() 
    #super used to call method of parent class from child class when the same method name is also present in Child class
    #polymorohism

main()


         