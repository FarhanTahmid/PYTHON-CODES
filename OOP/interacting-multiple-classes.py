
class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name=name
        self.max_students=max_students
        self.students=[]

    def add_student(self,addstudent):
        if len(self.students)<self.max_students:
            self.students.append(addstudent)
            return True
        return False

    def get_average_grade(self):
        pass

s1=student("farhan", 21, 90)
s2=student("nandini", 20, 85)
s3=student("neha", 19, 60)

crs=Course("CSE115",2)
crs.add_student(s1)
crs.add_student(s2)
print(crs.students[0].name)
    
