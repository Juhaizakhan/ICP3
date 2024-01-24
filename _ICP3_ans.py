#!/usr/bin/env python
# coding: utf-8

# In[22]:


#task 1

class Company:
    def __init__(self):
        self.employees = []
        self.employee_count = 0  # data member to count the number of Employees

    def add_employee(self, employee):
        self.employees.append(employee)
        self.employee_count += 1  

    def average_salary(self): # function to calculate average salary
        if not self.employees:
            return 0  

        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary / len(self.employees)

class Employee: 
    def __init__(self, name, family, salary, department): #constructor to initialize name, family, salary, department
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

class FulltimeEmployee(Employee): # a Fulltime Employee class that inherits the properties of Employee class
    pass

company = Company() #company instance

# instances of Fulltime Employee class and Employee class 
employee1 = FulltimeEmployee("Jack", "Jack Family", 2000000, "Dept A")
employee2 = FulltimeEmployee("Max", "Max Family", 500, "Dept B")
company.add_employee(employee1)
company.add_employee(employee2)

# Calling member functions
print("The average salary of employees is: ", company.average_salary())
print("The employee count is", company.employee_count)


# In[27]:


#task 2

import numpy as np
random_vector = np.random.uniform(1, 20, 20)

print("Random Vector: ", random_vector)

reshaped_array = random_vector.reshape(4, 5)

reshaped_array[np.arange(4)[:, None], np.argmax(reshaped_array, axis=1)[:, None]] = 0

print("Reshaped array is: ", reshaped_array)


# In[ ]:




