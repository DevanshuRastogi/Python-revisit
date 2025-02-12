# students =[
#     {"name" : "Dev" , "YOB" : 2004},
#     {"name" : "Arsh" , "YOB" : 2003},
#     {"name" : "Gagan" , "YOB" : 2003},
# ]


# def age_calc(student):
#     age= 2025 - student["YOB"];
#     print(f"{student["name"] } is {age} years old")
    
    



# for std in students:
#     age_calc(std)
    
    
    
    ##------------------return in fn -----------------------##

# students =[
#     {"name" : "Dev" , "YOB" : 2004},
#     {"name" : "Arsh" , "YOB" : 2003},
#     {"name" : "Gagan" , "YOB" : 2003},
# ]


# def age_calc(student):
#     age= 2025 - student["YOB"];
#     return (f"{student["name"] } is {age} years old")
    
    

# my_age_list = list();

# for std in students:
#     my_age_list.append(age_calc(std))
    
    




# print(my_age_list) 



# -------------------------------------------------------


 ##------------------return in fn -----------------------##

# students =[
#     {"name" : "Dev" , "YOB" : 2004},
#     {"name" : "Arsh" , "YOB" : 2003},
#     {"name" : "Gagan" , "YOB" : 2003},
# ]


# def age_calc(student , current_year=2025):
#     age= current_year - student["YOB"];
#     return (f"{student["name"] } is {age} years old")
    
    

# my_age_list = list();

# for std in students:
#     my_age_list.append(age_calc(std , 2024))
    
    




# print(my_age_list) 


##-----------------lambda------------------------##

students =[
    {"name" : "Dev" , "YOB" : 2004},
    {"name" : "Arsh" , "YOB" : 2003},
    {"name" : "Gagan" , "YOB" : 2003},
]


age_calc =lambda student , current_year=2025: (f"{student["name"] } is {current_year - student["YOB"]} years old")
    
    

my_age_list = list();

for std in students:
    my_age_list.append(age_calc(std , 2024))
    
    




print(my_age_list) 