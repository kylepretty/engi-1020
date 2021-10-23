if getCourseLetter >= 80:
  letterGrade = A
elif getCourseLetter >= 65 and < 80:
  letterGrade = B
elif getCourseLetter >= 55 and < 65:
  letterGrade = C
elif getCourseLetter >= 50 and < 55:
  letterGrade = D
elif getCourseLetter >= 0 and < 50:
  letterGrade = F
else:
  letterGrade = X

getCourseGPA = GPA

if letterGrade = A:
  GPA = 4
elif letterGrade = B:
  GPA = 3
elif letterGrade = C:
  GPA = 2
elif letterGrade = D:
  GPA = 1
elif letterGrade = F:
  GPA = 0
else:
  GPA = -1