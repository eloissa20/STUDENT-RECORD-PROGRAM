import os
import csv

class Subject:
    def __init__(self, name):
        self.name = name
        self.grade = 0

    def setGrade(self, value):
        self.grade = value

    def name(self):
        return self.name


class Student():
    def __init__(self, name):
        self.name = name
        self.grades = []
        self.average = 0


    def setAverage(self):
        temp = 0
        for i in self.grades.values():
            temp += i
            self.average = (temp / 5)
        
        return self.average
    
    def name(self):
        return self.name
    
    def getGradeSize(self):
        return len(self.grades)

    def writeGrades(self):
        templist = []
        for i in self.grades:
            temp = ["Grade", i.name, i.grade]
            templist.append(temp)
        return templist

    def getSubjects(self):
        for i in self.grades:
            print(i.name + " ")

    def checkSubject(self, name):
        for i in self.grades:
            if i.name == name:
                return True
        
        return False

    def setAverage(self):
        temp = 0
        for i in self.grades:
            temp += i.grade
        self.average = (temp / len(self.grades))

    def updateAverage(self, value):
        self.average = value
    
    def getAverage(self):
        return self.average

    def getSubjectCount(self):
        return len(self.grades)

    def addSubject(self, subjectName):
        temp = Subject(subjectName)
        self.grades.append(temp)

    def setGrade(self, subjectName, value):
        for i in self.grades:
            if i.name == subjectName:
                i.setGrade(value)

    def getGrades(self):
        for i in self.grades:
            print(i.name + ": " + str(i.grade) + "\n")

    def printInfo(self):
        self.setAverage()
        print("Name: " + self.name + "\n")
        print("Average: " + str(int(self.average)) + '\n')
        self.getGrades()

    def changeName(self, name):
        self.name = name



def addStudent(STUDENTS):
    os.system("cls")
    name = input("Student Name: ")

    for i in STUDENTS:
        if i.name == name:
            print("Student Already Exists... returning to main menu!")
            return

    student = Student(name)
    STUDENTS.append(student)
    os.system("pause")
    os.system("cls")

def addSubject(STUDENTS):
    os.system("cls")
    if len(STUDENTS) == 0:
        print("Add Students First!")
    else: 
        temp = ""
        print("1. Add Subject to a Specific Student\n2. Add Subject to all Students")
        temp = input("Choice: ")


        if temp == '1':
            os.system("cls")
            j = 1
            for i in STUDENTS:
                num = str(j)
                print(num + ": " + i.name + "\n")
                j += 1
            user = int(input("Enter Choice: "))

            if user > len(STUDENTS):
                print("Invalid Input! returning to main menu!")
            else:
                name = input("Enter Subject Name: ")
                if STUDENTS[(user - 1)].checkSubject(name.lower()):
                    print("Subject already exists")
                else:
                    STUDENTS[(user - 1)].addSubject(name.lower())
        elif temp == '2':
            name = input("Enter Subject Name: ")
            if STUDENTS[0].checkSubject(name.lower()):
                print("Subject already exists")
            else:
                for i in STUDENTS:
                    i.addSubject(name.lower())
        else:
            print("invalid Input returning to main menu!")


    os.system("pause")
    os.system("cls")

def addGrade(STUDENTS):
    os.system("cls")
    if len(STUDENTS) == 0:
        print("Add Students First!")
    elif len(STUDENTS[0].grades) == 0:
        print("Add some Subjects first!")
    else: 

        j = 1
        for i in STUDENTS:
            num = str(j)
            print(num + ": " + i.name + "\n")
            j += 1
        user = int(input("Enter Choice: "))

        if user > len(STUDENTS):
            print("Input Out of Range!")
        else:
            STUDENTS[(user - 1)].getSubjects()
            subjName = input("Enter subject name to add grades(in lowercase): ")
            if STUDENTS[(user - 1)].checkSubject(subjName.lower()):
                grade = int(input("Enter the Grade of the said subject: "))
                STUDENTS[(user - 1)].setGrade(subjName.lower(), int(grade))
            else:
                print("Subject Does not Exists returning to main menu...")
    os.system("pause")
    os.system("cls")

def display(STUDENTS):
    os.system("cls")
    for i in STUDENTS:
        i.printInfo()
        print("----------------------\n")
    os.system("pause")
    os.system("cls")

def search(STUDENTS):
    os.system("cls")
    if len(STUDENTS) == 0:
        print("Add Students First!")
    elif len(STUDENTS[0].grades) == 0:
        print("Add some Subjects first!")
    else:
        name = input("Enter student's name: ")
        stud = Student
        for i in STUDENTS:
            if i.name == name:
                stud = i
            else:
                stud = 0
        
        if stud == 0:
            print("ERROR! Student record not found.")
        else:
            stud.printInfo()
    os.system("pause")
    os.system("cls")

def update(STUDENTS):
    os.system("cls")
    if len(STUDENTS) == 0:
        print("Add Students First!")
    elif len(STUDENTS[0].grades) == 0:
        print("Add some Subjects first!")
    else: 
        j = 1
        for i in STUDENTS:
            num = str(j)
            print(num + ": " + i.name + "\n")
            j += 1
        user = int(input("Enter Choice: "))

        if user > len(STUDENTS):
            print("Input Out of Range!")
        
        print("1. Update Name\n2. Update Grades")
        choice = ''
        choice = input("Enter Choice: ")

        if choice == '1':
            os.system("cls")
            name = input("Enter a name: ")
            STUDENTS[(user - 1)].changeName(name)
        elif choice == '2':
            os.system("cls")
            STUDENTS[(user - 1)].getSubjects()
            subjName = input("Enter subject name to update the grade(in lowercase): ")
            grade = int(input("Enter the Grade of the said subject: "))
            STUDENTS[(user - 1)].setGrade(subjName.lower(), int(grade))
        else:
            print("Invalid Input! returning to main menu!")
    os.system("pause")
    os.system("cls")

def delete(STUDENTS):
    os.system("cls")
    if len(STUDENTS) == 0:
        print("Add Students First!")
    elif len(STUDENTS[0].grades) == 0:
        print("Add some Subjects first!")
    else: 
        os.system("cls")
        j = 1
        for i in STUDENTS:
            num = str(j)
            print(num + ": " + i.name + "\n")
            j += 1
        user = int(input("Enter Student to Delete: "))

        STUDENTS.remove(STUDENTS[(user - 1)])
    os.system("pause")
    os.system("cls")



def write(STUDENTS):
    os.system("cls")
    if len(STUDENTS) == 0:
        print("Add Students First!")
    elif len(STUDENTS[0].grades) == 0:
        print("Add some Subjects first!")
    else:
        name = input("Enter student's name: ")

        for i in STUDENTS:
            if i.name == name:
                with open('student.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Name", i.name])
                    writer.writerow(["Average", i.average])
                    writer.writerows(i.writeGrades())

    os.system("pause")
    os.system("cls")
def read(STUDENTS):
    os.system("cls")
    if os.path.isfile("./student.csv"):
        file = open('student.csv')
        csvreader = csv.reader(file)
        student = Student("")
        for row in csvreader:
            if row[0] == "Name":
                student.changeName(row[1])
            elif row[0] == "Average":
                student.updateAverage(row[1])
            elif row[0] == "Grade":
                student.addSubject(row[1])
                student.setGrade(row[1], int(row[2]))
        STUDENTS.append(student)
    os.system("pause")
    os.system("cls")
