employees = [{'name':'John', 'age':34, 'average_salary':75000}, 
	    {'name':'Mary', 'age':28, 'average_salary':68000},
            {'name':'Peter', 'age':41, 'average_salary':92000},
            {'name':'Grace', 'age':31, 'average_salary':81000} 
           ]

def employeeNames():
 print('Employee Names:')
 for staff in employees:
  print(staff['name'])
 print('\n')

def averageSalary():
 totalSalary=0
 
 for staff in employees:
  totalSalary+=staff['average_salary']
 
 avSalary = totalSalary/len(employees)
 
 print('Average Salary: '+ str(int(avSalary))+'\n')

def employeeWithTheHighestSalary():
 highestSalary=0
 highestStaff=''
 
 for staff in employees:
  if staff['average_salary'] > highestSalary:
   highestSalary = staff['average_salary']
  
 for staff in employees:
  if staff['average_salary'] == highestSalary:
   highestStaff = staff['name']
 
 print('Employee with the highest salary is '+ highestStaff+'.\n')

def employeesWithSalaryGreaterThan80000():
 print('Employees with salary greater than 80,000:')
 for staff in employees:
  if staff['average_salary'] > 80000:
   print(staff['name'])
 print('\n')

employeeNames()
averageSalary()
employeeWithTheHighestSalary()
employeesWithSalaryGreaterThan80000()

