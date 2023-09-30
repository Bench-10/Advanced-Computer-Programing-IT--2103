student = str(input("Student name: "))

englishGrade = float(input("Grade in English: "))
scienceGrade = float(input("Grade in Science: "))
filipinoGrade = float(input("Grade in Filipino: "))
mathGrade = float(input("Grade in Math: "))
apGrade = float(input("Grade in Araling Panlipunan: "))
peGrade = float(input("Grade in Physical Education: "))

sumGrade = englishGrade + scienceGrade + filipinoGrade + mathGrade + apGrade + peGrade

avgGrade = sumGrade/6

print("Average Grade:", avgGrade)
