Number1 = int(input("Please enter your first number: "))
Number2 = int(input("Please enter your second number"))
Operator = input("Please add operator + or - or / or * :")

if Operator == "+":
    print (Number1 + Number2)
elif Operator =="-":
    print (Number1 - Number2)
elif Operator =="*":
    print(Number1*Number2)
elif Operator =="/":
    print(Number1/Number2)
else:
    print("Incorrect entry, please check operator")
#Comments