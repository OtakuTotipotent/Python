data = input("Enter sentence : ")

for char in data:
    if data.count(char) == 1:
        print(char)
        break
