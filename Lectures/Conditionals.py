userInput = int(input("Enter your age : "))

if userInput < 13:
    print("Child")
elif userInput > 12 and userInput < 20:
    print("Teenager")
elif userInput > 19 and userInput < 60:
    print("Adult")
else:
    print("Senior Citizen")
