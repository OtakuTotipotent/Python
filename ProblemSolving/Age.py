# Program that takes the age of Person and tells Life Stage
# ? Getting runtime user inputs
userInput = input("Enter your age : ")

# ? Checking if the input is valid
try:
    userInput = int(userInput)
except:
    print("invalid input")
    exit()

# ? Main logic of program
if userInput < 13:
    print("Child")
elif userInput < 20:
    print("Teenager")
elif userInput < 60:
    print("Adult")
else:
    print("Senior Citizen")
