class person():
  def __init__(self, name ):
   self.name = name 
  def person_name (self):
    print(f"my name is {self.name}")
class student(person):
 pass
stud1 = student("aditya")
stud1.person_name()

            