#Q1(a)
def divisible_3():
    data = int(input("Please enter a number: "))
    if data %3 == 0:
        print("True")
    else:
        print("False")


#Q1(b)
def divisible_n():
    num_1 = int(input("Please enter first number: "))
    num_2 = int(input("Please enter second number: "))
    if num_1 %num_2 == 0:
        print("First number is divisible by the second number")
    else:
        print("First number is not divisible by second number")


print("Please select the following you would like to check:")
print("")
print("1. 3: To check if a number is divisible by three")
print("2. N: To check if first number is divisible by second number")
print("3. n: To check if first number is divisible by second number")
print("")
option = input("Please enter choice 3/N/n: ")

while option not in ["3","N","n"]:
    option = input("Please re-enter the choice 3/N/n: ")
if option == "3":
    divisible_3()

elif option == "N" or "n":
    divisible_n()

    
    
     
