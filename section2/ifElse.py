
set_1 = {"ram" , "mohan" , "ravi"}

name = input( "ur name is  : ");

if name in set_1:
    print("Name is present")
    print("welcome {}".format(name))
    
else:
    print("sorry name is not present")