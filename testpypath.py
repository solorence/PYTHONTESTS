import re
from pathlib import Path

SALARY_TOTAL = 0
VALID_EMAILS = []
location = Path(Path.home()/'Desktop'/'employees.txt')


print('File Exists: ' + str(location.exists()) + '\n')


fileRequest = open(location)

employeesFile = fileRequest.read()

findEmailsRegEx = re.compile(r'\w+@\w+\.\w+ \.?\w*\.?\w*')

findSalariesRegEx = re.compile(r'\d+')


def findAndPrintValidEmails():
 validMails = findEmailsRegEx.findall(employeesFile)
 global VALID_EMAILS
 VALID_EMAILS = validMails
 print('Emails:')
 for email in validMails:
  print(email)
 print('')

def findAndPrintTotalValidSalaries():
 totalSalary = 0 
 global SALARY_TOTAL
 staffInfo = employeesFile.split('\n') 
 
 for staff in staffInfo:
  if 'invalid' not in staff:
   salaryMatch = findSalariesRegEx.search(staff)
   if salaryMatch != None:
    totalSalary += int(salaryMatch.group())
 
 SALARY_TOTAL = totalSalary
 print('Total salary: ' + str(totalSalary) + '\n')

def printAverageSalary():
 average_salary = SALARY_TOTAL//len(VALID_EMAILS)
 print('Average salary: ' + str(average_salary) + '\n')

 
findAndPrintValidEmails()
findAndPrintTotalValidSalaries()
printAverageSalary()

