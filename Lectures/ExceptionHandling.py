userInput = input("Enter your age : ")

try:
    userInput = int(userInput)
except:
    print("invalid input")
    exit()

print(userInput)
