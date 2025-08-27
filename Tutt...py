
#simple calculator using only if else statement 


print("1  add")
print("2  sub")
print("3  mult")
print("4  devide")


option = int(input("choose an operation: "))

if(option in [1,2,3,4]):
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))

    if(option == 1):
        result=num1+num2

    elif(option==2):
        result = num1-num2

    elif(option == 3):
        result = num1*num2
    elif(option==4):
        result=num1//num2
    else:
        result = "sorry you dont choose any number"         
else:
    result="please choose a method"


print(f"result is {result}")


# bin
num = 98
num.bit_count()
print(num)

string  =5
check = bin(string)
print (check)
