def getCourseLetter(letterGrade):
	if getCourseLetter(letterGrade) >= 80:
	  return letterGrade = 'A'
	elif getCourseLetter(letterGrade) >= 65:
	  return letterGrade = 'B'
	elif getCourseLetter(letter) >= 55:
	  return letterGrade = 'C'
	elif getCourseLetter >= 50:
	  return letterGrade = 'D'
	elif getCourseLetter >= 0:
	  letterGrade = 'F'
	else:
	  letterGrade = 'X'
def getCourseGPA(letterGrade):
	if letterGrade == 'A':
	  getCourseGPA = 4
	elif letterGrade == 'B':
	  getCourseGPA = 3
	elif letterGrade == 'C':
	  getCourseGPA = 2
	elif letterGrade == 'D':
	  getCourseGPA = 1
	elif letterGrade == 'F':
	  getCourseGPA = 0
	else:
	  getCourseGPA = -1