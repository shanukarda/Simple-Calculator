print("Hello User!\n This is a basic Calculator.\n\nPlease enter your choice :")
def basic_calc():
    number1 = float(input("Enter First Number : "))
    op = input("Enter Operator : ")
    number2 = float(input("Enter Second Number : "))
    if op == "+":
        result1= number1 + number2
        print(float(result1))
    elif op == "-":
        result1= number1 - number2
        print(float(result1))
    elif op == "*":
        result1= number1 * number2
        print(float(result1))
    elif op == "/":
        result1= number1 / number2
        print(float(result1))
    else:
        print("Wrong Entry, Please check your entry!")

def raise_to_power():
    num1 = int(input("Enter base Number:"))
    num2 = int(input("enter power Number: "))
    print(pow(num1, num2))
continue1 = ""
while continue1 !="n":
    user_choice = input("Press 1 for +(plus),-(minus),*(multiply),/(divide).\nPress 2 for find the power of a Number:\n")
    if user_choice == "2":
        raise_to_power()
    elif user_choice == "1":
        basic_calc()
    else:
        print("Enter valid entry!")
    continue1 = input("Do you want to Continue?(y/n) : ")
print("thanks")
bye1 = input("B-Bye!!!")