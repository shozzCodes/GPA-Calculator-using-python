def setGrads(score: int):
    if score >= 91 and score <= 100:
        return "A", 4.00
    elif score >= 80:
        return "A-", 3.66
    elif score >= 75:
        return "B+", 3.33
    elif score >= 71:
        return "B", 3.00
    elif score >= 68:
        return "B-", 2.66
    elif score >= 64:
        return "C+", 2.33
    elif score >= 61:
        return "C", 2.00
    elif score >= 58:
        return "C-", 1.66
    elif score >= 54:
        return "D+", 1.33
    elif score >= 50:
        return "D", 1.00
    elif score < 50 and score >= 0:
        return "F", 0
    else:
        return "Invalid!"
    
def viewReport(courses: list):
    print("="*60)
    print(f"{'Semester Report':^60}")
    print("="*60)
    print(f"{'Name':<30}  {'Units':^15} {'Grade':^15}")
    print("-"*60)
    gdPoints = 0
    if courses != None:
        for course in courses:
            grade, gpa = setGrads(course["Score"])
            print(f"{course["Name"]:<30} {course["Credits"]:^15} {grade:^18}")
            gdPoints += gpa * course["Credits"]
    print("-"*60)
    result = gdPoints / TOT_CRD
    print("GPA: ",result)

print("="*60)
print(f"{'GPA Calculator':^60}")
print("="*60)
TOT_CRD = 0
TOT_CS = int(input("Enter total no. of courses (including labs): "))

dets = []
for i in range(0,TOT_CS):
    name = input(f"Enter course {i+1} name: ")
    creds = int(input(f"Enter course {i+1} credits: "))
    scor = int(input(f"Enter course {i+1} score (out of 100): "))
    dets.append(dict(Name = name, Credits = creds, Score = scor))
    TOT_CRD += creds
    print()

viewReport(dets)
 
