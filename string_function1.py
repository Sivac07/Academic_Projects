print("Major String function")
print("1. Capitalize")
print("2. Check whether the given string is lowercase or not")
print("3. Change all the characters into lowercase for the given string")
print("4. Change all the characters into uppercase for the given string")
print("5. Split the sentence into words")
print("6. Exit")
function = "Function name"
n = int(input("Enter your choice: "))
string = input("Enter the string: ")
while(n!=6):
 if n==1:
  print(function + ": capitalize()")
  print("Answer: " + string.capitalize())
 elif n==2:
   print(function + ": islower()")
   print("Answer: " + str(string.islower()))
 elif n==3:
   print(function + ": lower()")
   print("Answer: " + string.lower())
 elif n==4:
   print(function + ": upper()")
   print("Answer: " + string.upper())
 elif n==5:
    print(function + ": spilt()")
    print("Answer: " + string.split())
 else:
    print("Invalid Number")
 query = input("Do you want to continue further?(Yes/No)")
 if (query == "Yes" or query == "YES" or query== "yes"):
      n = int(input("Enter your choice: "))
      string = input("Enter the string: ")
 else:
     n=6
 
