class problem():
    def __init__(self,name):
#print("we are inn costructor of problem class ")
        self.name=name
        #print("we aree")
    def get_name(self):
        return self.name
    def isEmployee(self):
        return False

class Employee(problem):
    def isEmployee(self):
        return True

emp=problem("geek1")
print(emp.get_name(),emp.isEmployee())
emp=Employee("geeks2")
print(emp.get_name(),emp.isEmployee())