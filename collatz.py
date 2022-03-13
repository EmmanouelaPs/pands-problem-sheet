positiveNumber = int(input("Please enter a positive integer"))#asks from the user to enter a positive integer
positiveNumber = int(positiveNumber) #convert the positive number into an integer

calcs = positiveNumber #create a new variable taking the number the user entered
calcs = int(calcs) #convert the new variable into an integer
type(calcs) #check the variable is an integer
print (calcs) #print the variable

loop = int(calcs) #create a new variable with the value given modified by whatever the result from the conditions is
while loop > 1: #create a loop that stops when the value is equal or less than 1
    if calcs % 2 == 0: #first condition if the number is even should be dicided by 2
        calcs = int(loop) / 2 
    else:
        calcs = ( loop * 3 ) + 1 #second condition if the number is not even should be multiplied by 3 and add 1
    loop = int(calcs) # the new variable value depends on the above conditions
    print (loop) #print the variable in the loop until the while condition is satisfied


