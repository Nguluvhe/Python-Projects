class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    
class Employee(Person):
    def __init__(self, fname, lname, age, enumber, erole):
        Person.__init__(self, fname, lname, age)
        self.employeeNumber = enumber
        self.employeeRole = erole

    def myPrint(self):
        print("Name: " + self.firstname + "\nLast Name: " + self.lastname + "\nAge: " + str(self.age) + " years old")
        print("Employee Number: " + str(self.employeeNumber) + "\nEmployee Role: " + self.employeeRole)
        if self.age > 50:
            print("This person is old damn!!\n")
        else:
            print("This peron is young\n")

#p1 = Employee("Kelvin", "Setho", 55, 10, "Cleaner")
#p2 = Employee("Gaze", "Blow", 18, 66, "Programmer")

lsEmp = [Employee("Kelvin", "Setho", 55, 10, "Cleaner"), Employee("Gaze", "Blow", 18, 66, "Programmer"), Employee("Voice", "Box", 45, 3644, "DJ")]

#lsEmp[0].myPrint()
#lsEmp[1].myPrint()
 
a = len(lsEmp)
b = 0
while a > 0:
    
    lsEmp[b].myPrint()
    b += 1
    a -= 1
    