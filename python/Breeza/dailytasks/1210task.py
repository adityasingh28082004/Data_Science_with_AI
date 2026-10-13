import json

Name = input("enter the name :")
Age  = input("enter the age :")
City = input("enter the city :")
Course= input("enter the course :")

student = {
    "Name" :  Name,
    "Age"  :   Age ,
    "City" :  City ,
    "Course" : Course

}
# with open("student.json", "w") as file:
#     json.dump(student, file, indent=4)

# print("Data saved to JSON file successfully!") 

with open ("student.json","w") as file:
    json.load(student,file)
print("Data saved to JSON file successfully!") 
