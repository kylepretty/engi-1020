getCourseLetter = letterGrade

if getCourseLetter >= 80:
  letterGrade = A
elif getCourseLetter >= 65 and < 80:
  letterGrade = B
elif getCourseLetter >= 55 and < 65:
  letterGrade = C
elif getCourseLetter >= 50 and < 55:
  letterGrade = D
elif getCourseLetter >= 0 and < 50:
  letterGrade = E
else:
  letterGrade = X