operation = input("please input your operation (+,-,*,/): ")
number_1 = int(input("Please enter your first number: ")) 
number_2 = int(input("Please enter your second number: ")) 

if operation == '+':
    print("result: ",(number_1 + number_2))

elif operation == '-':
    print("result: ",(number_1 - number_2))

elif operation == '*':
    print("result: ",(number_1 * number_2))

elif operation == '/':
    print("result: ",(number_1 / number_2))

else:
    print("Invalid input")