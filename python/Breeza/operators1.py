student_information =[
    {'user_name':'aditya',
     'password':'ad1234',
     'marks_obtain':45,
     'passing_marks':30,
     'total_marks':100,

    },
       {'user_name':'shivam',
     'password':'sh1234',
     'marks_obtain':80,
     'passing_marks':32,
     'total_marks':100,},


     {'user_name':'shiv',
     'password':'sh1234',
     'marks_obtain':85,
     'passing_marks':40,
     'total_marks':100,},

       {'user_name':'ashish',
     'password':'asg657',
     'marks_obtain':87,
     'passing_marks':33,
     'total_marks':100,},


        {'user_name':'akash',
     'password':'ak5464',
     'marks_obtain':48,
     'passing_marks':67,
     'total_marks':100,}
]
print(student_information[0] == student_information[1])
print(student_information[2] ['marks_obtain'])
print(student_information[3] ['marks_obtain'] - student_information[0]['passing_marks'])
print(student_information[4] ['passing_marks'] == student_information[2]['total_marks'])
print(student_information[1] ['marks_obtain'] >= student_information[2]['total_marks'])
print(student_information[3] ['total_marks'] == student_information[4]['passing_marks'])
print(student_information[0] ['user_name'] == student_information[3]['user_name'])                      
print(student_information[3] ['marks_obtain'] - student_information[3]['total_marks'])
print(student_information[4] ['passing_marks'] % student_information[0]['total_marks'])
print(student_information[3] ['password'] != student_information[0]['password'])
print(student_information[1] ['total_marks'] // student_information[2]['total_marks'])
print(student_information[2] ['passing_marks'] * student_information[0]['total_marks'])
print(student_information[3] ['marks_obtain'] / student_information[4]['total_marks'])
print(student_information[4])
print(student_information[3])
print(student_information[1] ['marks_obtain'] <= student_information[0]['total_marks'])
print(student_information[2] ['user_name'] + student_information[4]['user_name'])

#for student in student_information:
   # print(student['user_name'])
     #print(student['total_marks'])
print(student_information[4]['user_name']==student_information[2]['user_name'])
print(student_information[0]['user_name']=='aditya'or student_information[3]['user_name']=='aditya')
print(student_information[0]['passing_marks']==30 and student_information[3]['user_name']=='30')
print(student_information[0]['total_marks']==100 and student_information[3]['total_marks']!=100)
print(student_information[3]['marks_obtain']==85 or student_information[4]['marks_obtain']==98)

