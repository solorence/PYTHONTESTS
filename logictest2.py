employees = [
    {'name': 'John', 'age': 34, 'salary': 75000, 'active': True},
    {'name': 'Mary', 'age': 28, 'salary': 68000, 'active': True},
    {'name': 'Peter', 'age': 41, 'salary': 92000, 'active': False},
    {'name': 'Grace', 'age': 31, 'salary': 81000, 'active': True},
    {'name': 'David', 'age': 24, 'salary': 55000, 'active': False}
]


result = {
    'senior': [],
    'junior': [],
    'high_earner': [],
    'inactive': []
}

for staff in employees:
 if staff['age'] >= 30:
  result['senior'].append(staff['name'])
 else:
  result['junior'].append(staff['name'])
 
 if staff ['salary'] >= 80000:
  result['high_earner'].append(staff['name'])

 if not staff['active']:
  result['inactive'].append(staff['name'])

print(result)


