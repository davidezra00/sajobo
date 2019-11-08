
def arit(num1, num2,choice):
   if choice==1 :
      return num1+num2
   else :
      return num1-num2
   
num1,num2,choice= int(input("Enter first number: ")),int(input("Enter second number: ")),int(input("Enter choice.\n 1.Add\n 2.Subtract-----\nEnter your choice:"))
if choice == 1:
   print(num1,"+",num2,"=", arit(num1,num2,choice))
elif choice == 2:
   print(num1,"-",num2,"=", arit(num1,num2,choice))
else:
   print("Invalid input")





#There are several parts of the syntax for a function definition :
   # syntax is def function_name():
 #A more general 

