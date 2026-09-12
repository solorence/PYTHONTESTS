
employees = [
    {'name': 'John', 'age': 34, 'salary': 75000, 'active': True},
    {'name': 'Mary', 'age': 28, 'salary': 68000, 'active': True},
    {'name': 'Peter', 'age': 41, 'salary': 92000, 'active': False},
    {'name': 'Grace', 'age': 31, 'salary': 81000, 'active': True},
    {'name': 'David', 'age': 24, 'salary': 55000, 'active': False}
]

def getEmployeeStats(employees):
 stats = {
    'total_employees':0,
    'active_employees':0,
    'active_salary_total':0,
    'average_active_salary':0,
    'inactive_employees':0
 }
 
 active_salary_total = 0

 for staff in employees:
  stats['total_employees'] += 1

 for staff in employees:
  if staff['active']:
   stats['active_employees'] +=1
 
 for staff in employees:
  if staff['active']:
   stats['active_salary_total'] += staff['salary']

 stats['average_active_salary'] = stats['active_salary_total']/stats['active_employees']
 
 for staff in employees:
  if not staff['active']:
   stats['inactive_employees'] += 1

 return stats

print(getEmployeeStats(employees))