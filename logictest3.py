employees = [
    {'name': 'John', 'age': 34, 'salary': 75000, 'active': True},
    {'name': 'Mary', 'age': 28, 'salary': 68000, 'active': True},
    {'name': 'Peter', 'age': 41, 'salary': 92000, 'active': False},
    {'name': 'Grace', 'age': 31, 'salary': 81000, 'active': True},
    {'name': 'David', 'age': 24, 'salary': 55000, 'active': False}
]


def calculatePayroll(employees):
 salarySumOfActives = 0
 for staff in employees:
  if staff['active']:
   salarySumOfActives += staff['salary']

 return salarySumOfActives

def calculateAverageActiveSalary(employees):
 totalActive=0
 for staff in employees:
  if staff['active']:
   totalActive +=1
 
 return calculatePayroll(employees)/totalActive

print('Average salary of Active employees is: ', calculateAverageActiveSalary(employees))