jobs=[   
    
     {
    "job_id": 101,
    "title": "Data Analyst",
    "company": "ABC Technologies",
    "city": "Hyderabad",
    "salary": 600000,
    "skills": ["Python","SQL","Excel"]},

    {"job_id": 102,
    "title": "data science",
    "company": "wipro",
    "city": "bangalore",
    "salary": 900000 ,
    "skills": ["numpy ","pandas","power bi"]  },        


     {"job_id": 103,
         "title": "front end developer",
         "company": "infosys",
         "city": "noida",
         "salary": 80000 ,
         "skills": ["html ","css","javascript"]  },  ]  


print(jobs[0]["title"])
print(jobs[0]["skills"])
count= 0
for job in jobs:
    if "Python" in job["skills"]:
        count = count+1
print("Jobs requiring Python:", count)
skill_count ={}
for job in jobs:
     for skill in job ["skills"]:
          skill = skill.strip()
          if skill in skill_count :
            skill_count[skill] = skill_count[skill] + 1
          else:
            skill_count[skill] = 1


most_demanded_skill= max(skill_count, key = skill_count.get)
print("Most in-demand skill:", most_demanded_skill)  

total_salary = 0 
for job in jobs:
    total_salary = total_salary + job["salary"]
    average_salary = total_salary / len(jobs)
print("Average_salary :" , average_salary)
highest_salary = 0 

highest_salary= max(job["salary"]for job in jobs)
print("Highest_salary:", highest_salary)
for job in jobs:
 if job["salary"] == highest_salary:
      print("highest paying job:",job["title"])
      print("salary:", job["salary"] )
lowest_salary  = min(job["salary"] for job in jobs)
print("Lowest_salary:", lowest_salary)
for job in jobs :
    if job["city"] == "Hyderabad":
       print("Job title :",job["title"]) 
       print("salary:", job["salary"])
def get_jobs_by_city(city):
    for job in jobs:
        if job["city"].lower() == city.lower() :
            print("Job title :",job["title"]) 
            print("salary:", job["salary"])

get_jobs_by_city("hyderabad")
get_jobs_by_city("Bangalore")
def get_jobs_by_skill(skills):
    for job in jobs:
        if skills in job["skills"]:
             if skills.strip().upper() == skills.strip().upper():
              print("Job title :",job["title"])  
              print("Salary:", job["salary"])
get_jobs_by_skill("Python")
get_jobs_by_skill("html")
def get_jobs_by_skill(skills):
    for job in jobs:
        for job_skill in job["skills"]:
            if job_skill.strip().upper() == skills.strip().upper():
                print("Job title:", job["title"])
                print("Salary:", job["salary"])
                break


get_jobs_by_skill("python")
def get_jobs_by_salary(min_salary):
    for job in jobs:
        if job["salary"] >= min_salary:
            print("Job title:", job["title"])
            print("Salary:", job["salary"])
get_jobs_by_salary(50000)
def get_jobs_by_salary_and_skills(skills,salary):
    for job in jobs:
        for job_skill in job["skills"]:
            if (job_skill.strip().upper() == skills.strip().upper() and job["salary"] >= salary):
                

                print("Job title:", job["title"])
                print("Salary:", job["salary"])
get_jobs_by_salary_and_skills("python", 600000)
def get_jobs_by_city_and_salary(city, salary):
    for job in jobs:
        
            if (job["city"].strip().lower()=="city".strip().lower() 
            and job["salary"] >= salary):
                print("Job title:", job["title"])
                print("Salary:", job["salary"])
                

get_jobs_by_city_and_salary("hyderabad" , 50000) 
def count_jobs_by_city(city) :
    count = 0
    for job in jobs:
         if job["city"].strip().lower() == city.strip().lower():
          count += 1
    
    print("Total jobs in", city, ":", count)
count_jobs_by_city("hyderabad")
def count_jobs_by_skill(skill):
    count = 0 
    for job in jobs:
        if skill in job["skills"]:
        #    if job["skills"] == skill:
            
            
            count+=1
    
    print("Total jobs in", skill, ":", count)
count_jobs_by_skill("Python")



    


