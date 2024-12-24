num = int(input("Enter any number : "))

for i in range(2, (int(num / 2) + 1)):
    if num % i == 0:
        print("Given number is COMPOSITE")
        exit()

print("Given number is a PRIME")
