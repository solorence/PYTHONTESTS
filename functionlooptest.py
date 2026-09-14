employees = [
    {'name': 'John', 'age': 34, 'salary': 75000, 'active': True},
    {'name': 'Mary', 'age': 28, 'salary': 68000, 'active': True},
    {'name': 'Peter', 'age': 41, 'salary': 92000, 'active': False},
    {'name': 'Grace', 'age': 31, 'salary': 81000, 'active': True},
    {'name': 'David', 'age': 24, 'salary': 55000, 'active': False}
]


def analyzeEmployees(employees):
 status= {
    'senior': [],
    'junior': [],
    'high_earner': [],
    'low_earner': [],
    'active': [],
    'inactive': []
 }

 for staff in employees:
  if staff['age'] >= 30:
   status['senior'].append(staff['name'])
  else:
   status['junior'].append(staff['name'])
 
  if  staff['salary'] >= 80000:
   status['high_earner'].append(staff['name'])
 
  if staff['salary'] < 60000:
   status['low_earner'].append(staff['name'])

  if staff['active']:
   status['active'].append(staff['name'])
 
  if not staff['active']:
   status['inactive'].append(staff['name'])

 return status


print(analyzeEmployees(employees))