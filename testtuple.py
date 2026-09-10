students = """John, 23, 78
Mary, 21, 65
Peter, 25, 91
Grace, 22, 84
John, 23, 78
Mary, 21, 65"""

listOfStudentInfo=[]

for student in students.split('\n'):
 listOfStudentInfo.append(tuple(student.split(', ')))

print( listOfStudentInfo)

