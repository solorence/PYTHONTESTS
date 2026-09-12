employees = [
    {'name': 'John', 'age': 34, 'salary': 75000, 'active': True},
    {'name': 'Mary', 'age': 28, 'salary': 68000, 'active': True},
    {'name': 'Peter', 'age': 41, 'salary': 92000, 'active': False},
    {'name': 'Grace', 'age': 31, 'salary': 81000, 'active': True},
    {'name': 'David', 'age': 24, 'salary': 55000, 'active': False}
]

status = {'eligible':[], 'needs_attention':[]}
for data in employees:
 if data['age'] >= 30 and data['salary'] >= 80000 and data['active'] :
  status['eligible'].append(data['name'])
else:
 if not data['active'] or data['salary'] < 60000:
  status['needs_attention'].append(data['name'])
     
print(status)

def printEligibleEmployees():
 print('\nEligible Employees:')
 for name in status['eligible']:
   print(name)

def printEmployeThatNeedsAttention():
 print('\nEmployees that need attention:')
 for name in status['needs_attention']:
   print(name)
 

printEligibleEmployees()                             
printEmployeThatNeedsAttention()