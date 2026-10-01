student_information =[
    {'user_name':'aditya',
     'password':'ad1234',
     'marks_obtain':45,
     'passing_marks':30,
     'total_marks':100,

    }
                      
]

print(student_information[0])
print(student_information[0]['marks_obtain'])
print(student_information[0]['total_marks'] - student_information[0]['marks_obtain'])
print(student_information[0]['total_marks'] > student_information[0]['marks_obtain'])
print(student_information[0]['total_marks'] < student_information[0]['passing_marks'])
print(student_information[0]['passing_marks'] != student_information[0]['marks_obtain'])
print(student_information[0]['marks_obtain'] % student_information[0]['total_marks'])
print(student_information[0]['marks_obtain'] / student_information[0]['total_marks'])
print(student_information[0]['marks_obtain'] // student_information[0]['total_marks'])
print(student_information[0]['marks_obtain'] + student_information[0]['total_marks'])
print(student_information[0]['marks_obtain'] * student_information[0]['total_marks'])