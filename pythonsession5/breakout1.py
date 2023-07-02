class Student:
    name = ""
    age = 0
    gender = ""
    gradeLevel = 0
    courses = []

    def __init__(self, name, age, gender, gradeLevel):
        self.name = name
        self.age = age
        self.gender = gender
        self.gradeLevel = gradeLevel

    def addcourse(self, course):
        self.courses += course
        return self.courses

    def anotheryear(self, age):
        self.age += age
        return self.age

    def takecourse(self, course):
        self.courses -= course
        return self.courses

    def takegrade(self, grades):
        self.gradeLevel -= grades
        return self.gradeLevel

    def plusgrade(self, grades):
        self.gradeLevel += grades
        return self.gradeLevel

    def studentinfo(self):
        return self.name, self.age, self.gender, self.gradeLevel, self.courses


student = Student("Greg", 14, "male", 2)
print(student.name)
print(student.age)
print(student.gender)
print(student.gradeLevel)

student.anotheryear(1)
print(student.age)

student.addcourse(["Python"])
student.addcourse(['Maths'])
print(student.courses)

student.plusgrade(3)
print(student.gradeLevel)

student.takegrade(1)
print(student.gradeLevel)

student.studentinfo()
print("Student info:", student.studentinfo())
