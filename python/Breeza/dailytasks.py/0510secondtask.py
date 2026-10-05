student_name = input("enter the name :")
marks_in_python =int(input("enter the marks in python:"))
marks_in_sql = int((input("enter the marks in sql:")))
marks_in_machine_learning = int(input("enter the marks in machine learning :"))
attendence = int(input("enter the attendance :"))
total_marks = marks_in_python + marks_in_sql  + marks_in_machine_learning
percentage = total_marks /3
print("total_marks :" , total_marks)
print("percentage:" , percentage)
if marks_in_python >=40 and marks_in_sql >= 40 and marks_in_machine_learning >= 40 and attendence >= 75 :
        print("Pass")

elif marks_in_python < 40:
     print("fail:" , "python")
elif marks_in_sql <40 :
      print("fail:" , " sql")
elif marks_in_machine_learning <40:
      print("fail:" , "machine learning")

        
# Grade     
if percentage >= 90:
    print("grade:", "A+")
elif percentage >=80 and percentage <= 89 : 
    print("grade :", "A")
elif percentage >=70 and percentage <= 79 :
    print("grade:", "B")   
elif percentage >=60 and percentage <= 69 : 
    print("grade :", "C")  
elif percentage >= 50 and percentage <= 59 :
    print("grade:", "D")
elif percentage < 50 :
    print("grade: ","F" )
#Scholership    
if attendence < 75 :
         
        print("Detained due to low attendence")
elif percentage >90 and attendence >= 90 :
        print("100%" , "Fee wavier")
elif percentage >= 80 and attendence >= 85 :
        print("50%" ,"Fee wavier")
elif percentage >= 70 and attendence >= 80 :
        print("25%" ,"Fee wavier")
else:
        print("Not eligible")
        print("Failed and detained students are not eligible for scholership")



    