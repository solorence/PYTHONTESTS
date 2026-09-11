students = """John, 23, 78
Mary, 21, 65
Peter, 25, 91
Grace, 22, 84
John, 23, 78
Mary, 21, 65"""

listOfStudentInfo=[]
record={}
studentNames=[]
scoreCategory={}

for student in students.split('\n'):
 listOfStudentInfo.append(tuple(student.split(', ')))

def removeDuplicatesInList(LIST):
 duplicatesIndex=[]
 compared = {}
 for data in LIST:  
  compared.setdefault(data, False)
  seen = False
  for dataindex in range(len(LIST)):   
   if data == LIST[dataindex] and not compared[data]:
    if seen == True:     
     duplicatesIndex.append(dataindex)
     compared[data]= True
    seen = True
 
 duplicatesIndex.reverse()

 for i in duplicatesIndex:
  del LIST[i]
 

removeDuplicatesInList(listOfStudentInfo)

def addToRecord(LIST):
 for data in LIST:
  name, age, score = list(data)
  datainfo = list(data)
  studentNames.append(name)

  for info in datainfo:
   record[name]={}
   record[name]['name']= name
   record[name]['age']= age
   record[name]['score']= score


addToRecord(listOfStudentInfo)

def calAverageScore():
 total=0
 for name in studentNames:
   total += int(record[name]['score'])
 return total/len(studentNames)


def studentWithHighestScore():
 studentName=''
 newHighScore=0
 for name in studentNames:
  if int(record[name]['score']) > newHighScore:
   studentName = name
   newHighScore = int(record[name]['score'])
 
 return studentName   


print('\nAverage Score:', calAverageScore())

print('\nThe student with the highest Score is: ', studentWithHighestScore()   )

for name in record:
 score = int(record[name]['score'])
 if score >= 90:
  scoreCategory.setdefault('Excellent', [])
  scoreCategory['Excellent'].append(name)
 
 elif score >= 80 and score  <= 89:
   scoreCategory.setdefault('Very Good', [])
   scoreCategory['Very Good'].append(name)
 
 elif score >= 70 and score <= 79:
  scoreCategory.setdefault('Good', [])
  scoreCategory['Good'].append(name)
 
 elif score < 70:
   scoreCategory.setdefault('Needs Improvement', [])
   scoreCategory['Needs Improvement'].append(name)

print('\nscoreCategory: ',scoreCategory)
 



