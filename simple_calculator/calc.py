#Progam:        mycalc
#Date created:  2017-05-05
#Description:   A simple calculator script that allows users to enter 2 numbers and
#               one math operator to calculate a value. This is rewritten version of
#               the program that I wrote in unit 3. It removes repetitious code by
#               using functions and function calls. I also changed the output to show
#               the full equation.
#Restrictions:  User cannot enter 0 for firstNumber or secondNumber.
#               User must enter a valid integer.
#               User is restricted to 4 maths operations:    - addition
#                                                            - subtraction
#                                                            - multiplication
#                                                            - division
#Notes:         Run on Python 3.6.1
#               Variable names used as per the flowchart.

#=============================== Function Defintions ==========================

#Define integerError() to handle the error message when a incorrect value
#other than 0 is entered.
def integerError():
    
    print("Error: The value you entered is not a whole number, please try again")

    return

#Define operatorError() to handle the error message when a incorrect value is
#entered for the math operator.
def operatorError():

    print("Error: That is not a valid math operation, please try again")

    return

#Define getNum() to handle the error message when a incorrect value is
#entered for the variable num.
def getNum():

    #Allow the global variable to be modified.
    global number
    
    while True:
    
        try:
            
            #Input is stored as an integer in the variable number.
            number = int(input("Please enter a whole number: "))

            #Check whether the value entered was 0.
            if number == 0:
                
                print("Error: Zero is not allowed to be entered, please try again")

                continue
            
        except ValueError:
            
            #If the input entered is not an integer type, print an error.
            #Loop through until a valid integer has been entered.
            integerError()
            
            continue
        
        else:
            
            #number successfully parsed. Exit loop.
            break
    return

#==============================================================================
#                                Main Program
#==============================================================================

#=============================== Introduction =================================

print("My Calculator, version: 1.2", "\n")
print("INSTRUCTIONS:")
print("Enter 2 whole numbers and 1 math operator to perform a calculation", "\n")
print("RESTRICTIONS:")
print("1. Only whole numbers are allowed to be entered.")
print("2. 0 is not accepted as a number.")
print("3. Math operators are restricted to: +, -, /, and *.")
print("\n")

#=============================== Global variables =============================

number = 0

#=============================== First Number =================================

#Call getNum() to parse the first number
getNum()

#Assign the value of num to num1
num1 = number

#=============================== Math Operator ===============================
    
while True:
    
        #Input is stored as an string in the variable operator.
        operator = input("Please enter the math operation (+, -, *, or /): ")
        
        #if operator does not equal +, -, * or /, print an error and loop through until
        #one of the four maths operations is picked.
        if operator == "+":
            
            break
        
        elif operator == "-":
            
            break
        
        elif operator == "*":
            
            break
        
        elif operator == "/":
            
            break
        
        else:
            
            operatorError()
            continue

#=============================== Second Number =================================
#Call getNum() to parse the first number
getNum()

#Assign the value of num to num2
num2 = number

#=============================== Operator Case =================================
#Check which math operation operator is equal to. Perform the appropriate
#calculation and store it in the variable result.
    
if operator == "+":
    
    Result = num1 + num2
    
elif operator == "-":
    
    Result = num1 - num2
    
elif operator == "*":
    
    Result = num1 * num2
    
else:
    #result on the division is a float
    Result = num1 / num2

#=============================== Output result ==================================

#Print the result to the screen.
print(num1, operator, num2, "=", Result)

#==============================================================================
#                                Main Program End
#==============================================================================
                      
