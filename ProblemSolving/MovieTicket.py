day = input("Enter day : ")
day = day.lower()
age = int(input("Enter your age : "))

price = 12 if age > 17 else 8

if day == "wednesday":
    print(f"Your movie ticket price is ${price-2}")
else:
    print(f"Your movie ticket price is ${price}")
