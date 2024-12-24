data = input("Enter a word : ")
reverse = ""

i = len(data) - 1

while i > -1:
    reverse += data[i]
    i -= 1

print(f"\nGiven : {data} \nReversed : {reverse}")
