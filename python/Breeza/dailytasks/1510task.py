class person ():
    def __init__(self , person_id , name, age , email):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.email = email
        if not self.validate_age():
            raise ValueError("age must be graeter than zero")
    def validate_age(self):
        return self.age > 0
    def display_person(self):
        print("Id:", self.person_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("email:", self.email)
class student(person):
    def __init__(self, person_id,name,age,email,course,marks,attendence):
        super().__init__(person_id,name,age,email)
        if not 0 <= marks <= 100:
            raise ValueError("marks must be between 0 and 100")
        if not 0 <= attendence <= 100:
            raise ValueError("attendence must be between 0 nad 200")
        self.course = course
        self.marks = marks
        self.attendence = attendence
    def calculate_grades(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"
    def display_student(self):
       print("student details")
       super().display_person()
       print("course:", self.course)
       print("marks:", self.marks)
       print(f"attendence:, {self.attendence}%")
       print("grade:", self.calculate_grades())

class faculty(person):
    def __init__(self, person_id, name, age, email,
                 department, salary, experience_years):
        super().__init__(person_id,name,age,email)
        self.department = department
        self.salary = salary
        self.experience_years= experience_years
    def calculate_bonous(self):
        if self.experience_years >= 10:
            bonus_rate = 20
        elif self.experience_years >= 5:
            bonus_rate = 10
        else:
            bonus_rate = 5

        return self.salary * bonus_rate / 100
    def display_faculty(self):
        print("faculty details")
        super().display_person()
        print("department:", self.department)
        print(f"monthly salary:,{self.salary:.2f}")
        print("experience:", self.experience_years)
        print(f"bonous:,{self.calculate_bonous():.2f}")
class staff(person):
    def __init__(self, person_id, name, age, email,
                 designation, working_hours, overtime_hours):
        super().__init__(person_id, name, age, email)
        self.designation = designation
        self.working_hours= working_hours
        self.overtime_hours = overtime_hours
    def calculate_overtime_pay(self):
        overtime_rate= 200
        return self.overtime_hours * overtime_rate
    def display_staff(self):
        print(" Staff Details")
        self.display_person()
        print("Designation:", self.designation)
        print("Working Hours:", self.working_hours)
        print("Overtime Hours:", self.overtime_hours)
        print(f"Overtime Pay: ₹{self.calculate_overtime_pay():.2f}")
student1 = student(
    101, "Rahul", 20, "rahul@example.com",
    "Python", 85, 92)
student2 = student(
    102, "Neha", 21, "neha@example.com",
    "Data Science", 95, 88
)
faculty1 = faculty(
    201, "Priya", 35, "priya@example.com",
    "Computer Science", 60000, 8
)
faculty2 = faculty(
    202, "Raj", 45, "raj@example.com",
    "Mathematics", 80000, 12
)
staff1 = staff(
    301, "Amit", 28, "amit@example.com",
    "Lab Assistant", 8, 2
)

staff2 = staff(
    302, "Sneha", 30, "sneha@example.com",
    "Office Assistant", 7, 3
)



student1.display_student()
student2.display_student()

faculty1.display_faculty()
faculty2.display_faculty()

staff1.display_staff()
staff2.display_staff()








