# age = 21  ##int


# print(age);



# # python uses  snake_case

# PI = 3.14  #float

# Area_of_circle = 2*PI*PI

# print(Area_of_circle);



## ----------------------------------##


# print(12/3)  # ye dega float 4.0
# print(12//3)  # ye dega integer 4



##-----------------------------------------##

#  % use for remainder

# print(13%2) # ye dega 1 remainder



##-----------------------------------------##


# my_quote = "ultimately , everyone will meet their own fate"
# print(my_quote)



# song_lyrics = "Wise man say : \"only fools rushed in \"  "
# print(song_lyrics)


##-----------------------------------------##

# print(
# """
# hello hii 

# """)


##-----------------------------------------##


# # concat strings and num

# print("hello " + "dev")
  

# print("dev is "+str( 18) + " years old")
##-----------------------------------------##




# f string like string literal in js  use like (f"bla bla {value}")
# age = "21"
# about = f"dev is {age} years old"
# print(about)

# # comes with drawback like if we change value , it wont reflect

# age = "22"

# print(about) 
# # dev is 21 years old   result in same value so thats problem
# # dev is 21 years old


##-----------------------------------------##


# # using .format 

# age = 21;
# about = "hey are you {} years old ?"
# print(about.format(age))


# age = 22;
# print(about.format(age))


# age = 21 ;
# name = "devanshu";

# about= "are u {} of age {}";

# print(about.format( name,age))

##-----------------------------------------##

# age = int(input("What's ur age man? : "))

# print(age)




##----------------Boolean-------------------------##

# print(bool("" and []) )
# print(bool("hj" and [1,2]) )
# print(bool(False and True) )
# print(bool(False or True) )
# print(bool(45 or '') )
# print(bool(False and False) )

# name = input("name  : ")
# print("hello {} ".format(name  or "Guest")  )


##-----------------------------------------##

#  list or array in python
 

# my_list = [12 , 14 , 16]
# print(my_list)

# my_list.insert(3,4)
# print(my_list)

# my_list.append(5)
# print(my_list)


# my_list.pop()
# print(my_list)

# my_list.remove(12)
# print(my_list)




##-----------------------------------------##


# Tuples

# my_tuple = ("ram " , "krishna" , "hari");
# print(my_tuple)
# my_tuple = my_tuple + (" mohan" ,)
# print(my_tuple)


##-----------------------------------------##


# set_A = {12 , 15 , 16};
# set_B = {12 , 20 , 10};
# set_A.add(14)
# print(set_A)





# print(set_A.difference(set_B))
# print(set_B.difference(set_A))
# print(set_B.symmetric_difference(set_A))

# age = 21  ##int


# print(age);



# # python uses  snake_case

# PI = 3.14  #float

# Area_of_circle = 2*PI*PI

# print(Area_of_circle);



## ----------------------------------##


# print(12/3)  # ye dega float 4.0
# print(12//3)  # ye dega integer 4



##-----------------------------------------##

#  % use for remainder

# print(13%2) # ye dega 1 remainder



##-----------------------------------------##


# my_quote = "ultimately , everyone will meet their own fate"
# print(my_quote)



# song_lyrics = "Wise man say : \"only fools rushed in \"  "
# print(song_lyrics)


##-----------------------------------------##

# print(
# """
# hello hii 

# """)


##-----------------------------------------##


# # concat strings and num

# print("hello " + "dev")
  

# print("dev is "+str( 18) + " years old")
##-----------------------------------------##




# f string like string literal in js  use like (f"bla bla {value}")
# age = "21"
# about = f"dev is {age} years old"
# print(about)

# # comes with drawback like if we change value , it wont reflect

# age = "22"

# print(about) 
# # dev is 21 years old   result in same value so thats problem
# # dev is 21 years old


##-----------------------------------------##


# # using .format 

# age = 21;
# about = "hey are you {} years old ?"
# print(about.format(age))


# age = 22;
# print(about.format(age))


# age = 21 ;
# name = "devanshu";

# about= "are u {} of age {}";

# print(about.format( name,age))

##-----------------------------------------##

# age = int(input("What's ur age man? : "))

# print(age)




##----------------Boolean-------------------------##

# print(bool("" and []) )
# print(bool("hj" and [1,2]) )
# print(bool(False and True) )
# print(bool(False or True) )
# print(bool(45 or '') )
# print(bool(False and False) )

# name = input("name  : ")
# print("hello {} ".format(name  or "Guest")  )


##-----------------------------------------##

#  list or array in python
 

# my_list = [12 , 14 , 16]
# print(my_list)

# my_list.insert(3,4)
# print(my_list)

# my_list.append(5)
# print(my_list)


# my_list.pop()
# print(my_list)

# my_list.remove(12)
# print(my_list)




##-----------------------------------------##


# Tuples

# my_tuple = ("ram " , "krishna" , "hari");
# print(my_tuple)
# my_tuple = my_tuple + (" mohan" ,)
# print(my_tuple)


##-------------------sets----------------------##


# set_A = {12 , 15 , 16};
# set_B = {12 , 20 , 10};
# set_A.add(14)
# print(set_A)





# print(set_A.difference(set_B))
# print(set_B.difference(set_A))
# print(set_B.symmetric_difference(set_A))
# print(set_B.intersection(set_A))
# print(set_B.union(set_A))



##--------------------Dictonaries---------------------##

# my_dict = {
#     id:0,
#     name : "Mohan",
#     Age : 12,
# }


#  list of dictonaries

# my_dict = [
#     {
#     "id":0,
#     "name" : "Mohan",
#     "Age" : 12,
# } ,
#     {
#     "id":2,
#     "name" : "Deepak",
#     "Age" : 21,
# } 
# ]


# print(my_dict[1 ]["name"])




# another way to create dictonary




# my_dict_2 = [("name" , "Hero") , ("age" , 21) , ("id", 0) ]


# print(my_dict_2)
# print(dict(my_dict_2))   # it creates dictonaries


###-----------------------------------------##


# my_list = [12 , 18 , 20 , 25 ]

# print(sum(my_list))
# print(len(my_list))
# print(sum(my_list)/len((my_list)))


##-----------------------------------------##
# Joining list


# prabhuName = ["Raghav" , "Raghunanandan"  , "Karunanidhan"]
# print(f"my prabhu name is {", ".join(prabhuName)}" )

##-----------------------------------------##
