print("Hello! You are welcome. \n")
print("I am a calculator. \n")
print("I can perform tasks like: \n 1. Addition \n 2. Substraction \n 3. Multiplication \n 4. Divison \n 5. Exponential \n")

print("Please carefully read the instructions which are as follows: \n") 
print("1. You will have to insert two numbers for the operation to be solved between them. \n")
print("2. You can change the operation in midway by typing 'change' when asked about execution \n ")
print("3. Type addition, substraction, multiplication, division or exponential when asked.\n")


print("OK, then we can start \n")

while True:
    operation = str(input("Which operation do you want to execute? \n"))

    match operation:

        case 'addition' : 
            a = int(input("Write the first number: " ))
            b = int(input("Write the second number: " ))
            print("\n The result is", a + b)
        
        case 'substraction' :
            a = int(input("Write the first number: " ))
            b = int(input("Write the second number: " ))
            print("\n The result is", a - b)

        case 'multiplication' :
            a = int(input("Write the first number: " ))
            b = int(input("Write the second number: " ))
            print("\n The result is", a * b)

        case 'division' :
            a = int(input("Write the first number: " ))
            b = int(input("Write the second number: " ))
            print("\n The result is", float(a / b))

        case 'exponential' :
            a = int(input("Write the first number: " ))
            b = (input("Write the second number: " ))
            print("\n The result is", a ** b)

        case 'change' : 
            operation = str(input("Which operation do you want to execute? \n"))


        case _:
            print("Write the correct operation \n")