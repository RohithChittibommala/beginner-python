# This is a program for swapping two numbers.

P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  
   
# To swap the value of two variables  
# we will user third variable which is a temporary variable  
temp_1 = P  
P = Q  
Q = temp_1  
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  

# End of the program
