print("1 - add")
print("2 - subtract")
print("3 - multiply")
print("4 - divide")
Option = int(input("choose operation:"))

if(Option in [1,2,3,4]):
    num1 = int(input("Enter your first number"))
    num2 = int(input("Enter your second number"))

if(Option == 1):
    result = num1 + num2
elif(Option == 2):
     result = num1 - num2
elif(Option == 3):
     result = num1 * num2
elif(Option == 4):
     result = num1 // num2
   
else:
    print("Invalid operation entered")     

print ("the result of the operatiion  is {}".format(result))