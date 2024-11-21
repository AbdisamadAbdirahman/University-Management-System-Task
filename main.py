import uuid
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def get_details(self):
        print(f"Name: {self.name} \n Age: {self.age} \n Gender: {self.gender}")

class Student(Person):
    def __init__(self, name, age, gender, course):
        super().__init__(name, age, gender)
        self.id = str(uuid.uuid4()).split("-")[0]
        self.course = course
        self.grades = []
    def set_student_details(self, student_id: bool, course):
        if student_id:
            self.id = str(uuid.uuid4()).split("-")[0] + "-" + "STU"
        self.course = course
    def add_grade(self,grade):
        self.grades.append(grade)
    def calculate_average_grade(self):
        if self.grades == []:
            return 0
        else:
            total = 0
            for i in range(len(self.grades)):
                total += self.grades[i]
            return total / len(self.grades)
    def get_mentor(self):
        if self.mentor:
            print(self.mentor)
        else:
            print("No mentor assigned.")
    def get_student_summary(self):
        print(f"Name: {self.name} \n Age: {self.age} \n Gender: {self.gender} \n Course: {self.course} \n ID: {self.id} \n Grades: {self.grades} Average grade: {self.calculate_average_grade()}")

class Professor(Person):
    def __init__(self, name, age, gender, department, salary):
        super().__init__(name, age, gender)
        self.dep = department
        self.salary = salary
        self.mentored_students = []
        self.staff_id = str(uuid.uuid4()).split("-")[0] + "-" + "STA"
    def set_professor_details(self,staff_id: bool, department, salary):
        if staff_id:
            self.staff_id = str(uuid.uuid4()).split("-")[0] + "-" + "STA"
        self.dep = department
        self.salary = salary
    def give_feedback(self, Student, feedback):
        print(f"Feedback for {Student.name}, {feedback}")
    def increase_salary(self, percent):
        self.salary *= (percent / 100)
    def mentor_student(self, Student):
        print(f"Professor {self.name} is nor mentoring {Student.name} on {Student.course}")
        Student.mentor = self.name
        self.mentored_student.append(Student.name)
    def get_mentored_students(self):
        print(self.mentored_students)
    def get_professor_summary(self):
        print(f"Name: {self.name} \n Age: {self.age} \n Gender: {self.gender} \n ID: {self.staff_id} \n Department: {self.dep} \n Salary: {self.salary}")
class Admin(Person):
    def __init__(self, name, age, gender, office, years):
        super().__init__(name, age, gender)
        self.admin_id = str(uuid.uuid4()).split("-")[0] + "-" + "ADM"
        self.office = office
        self.years = years
    def set_admin_details(self, admin_id: bool, office, years):
        if admin_id:
            self.admin_id = str(uuid.uuid4()).split("-")[0] + "-" + "ADM"
        self.office = office
        self.years = years
    def increase_service_years(self):
        self.years += 1
    def get_admin_summary(self):
        print(f"Name: {self.name} \n Age: {self.age} \n Gender: {self.gender} \n ID: {self.admin_id} \n Department: {self.office} \n Years of service: {self.years}")

student_a = Student("Akram", 17, "Male", "Maths")
student_b = Student("Taheem", 16, "Male", "Physics")
prof_a = Professor("Mr. Mahdi", 33, "Male", "Comp Sci", 60000)
prof_b = Professor("Dr. Yazdi", 67, "Male", "Chemistry", 1000000)
admin = Admin("Mr Balon", 40, "Female", "Room M25", 4)
student_a.add_grade(9)
student_a.add_grade(7)
student_a.add_grade(6)
student_b.add_grade(8)
student_b.add_grade(7)
student_b.add_grade(9)
print(student_a.calculate_average_grade(),student_b.calculate_average_grade())
print(prof_a.give_feedback(student_b, "Be more attentive"))
prof_a.increase_salary(20)
admin.increase_service_years()
student_a.get_details()
student_b.get_details()
prof_a.get_professor_summary()
prof_b.get_professor_summary()
admin.get_admin_summary()

