#create a class Employee and add salary and increment properties to it.
#Write a method salary After increment method with a @property decorator with a setter 
# which changes the value of increment based on the salary

class Employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryafterincrement(self):
        return self.salary*self.increment

    @salaryafterincrement.setter
    def salaryafterincrement(self,sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryafterincrement)
print(e.increment)
e.salaryafterincrement = 2000
print(e.increment)