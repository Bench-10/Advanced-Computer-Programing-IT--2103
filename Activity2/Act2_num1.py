Fname = str(input("Enter Father's name: "))
Bplace = str(input("Enter place of birth: "))
Byear = int(input("Enter birthyear: "))
Bmonth = int(input("Enter birthmonth: "))
Bday = int(input("Enter birthday: "))

currentYear = 2023
currentMonth = 9
currentDay = 15

if Bmonth <= currentMonth :
    if Bday < currentDay :
        currentAge = currentYear - 1 - Byear
    else :
        currentAge = currentYear - Byear
else :
        currentAge = currentYear - Byear

print("Father's name:", Fname)
print("Birthplace:", Bplace)
print("Age:", currentAge)
