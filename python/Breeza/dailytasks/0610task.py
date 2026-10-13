employees = [    {'emp_id': 'EMP1001', 'name': 'Aarav Sharma', 'department': 'Finance'},  
               {'emp_id': 'EMP1002', 'name': 'Priya Reddy', 'department': 'Engineering'},  
                {'emp_id': 'EMP1003', 'name': 'Rohit Iyer', 'department': 'Sales'},   
         {'emp_id': 'EMP1004', 'name': 'Ananya Patel', 'department': 'Marketing'},
           {'emp_id': 'EMP1005', 'name': 'Vikram Nair', 'department': 'Human Resources'},  
         {'emp_id': 'EMP1006', 'name': 'Sneha Gupta', 'department': 'Customer Support'}, 
            {'emp_id': 'EMP1007', 'name': 'Karthik Rao', 'department': 'Operations'},  
               {'emp_id': 'EMP1008', 'name': 'Divya Singh', 'department': 'Product Management'},   
             {'emp_id': 'EMP1009', 'name': 'Arjun Kulkarni', 'department': 'Quality Assurance'},  
              {'emp_id': 'EMP1010', 'name': 'Meera Menon', 'department': 'IT Support'},]
#for employee in employees:
    #if employee ['department'] in ['Engineering' , 'Sales' ]:
       # print(employee['name'])
for employee in employees:        
    if employee ['name'].startswith('A'):
        print(employee['name'])
     

