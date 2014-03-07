class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print ('Total Employee %d' %Employee.empCount)

    def displayEmployee(self):
        print ('Name:', self.name, '   Salary: ', self.salary)

#creates info for first employee'
emp1 = Employee('sarah', 20000)

#creates infor for second employee'
emp2 = Employee('rory', 60000)

#calls display function for both employees'
emp1.displayEmployee()
emp2.displayEmployee()

#printing total number of empolyees'
print('Total number of employees is', Employee.empCount)

