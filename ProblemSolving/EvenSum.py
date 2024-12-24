limit = int(input("Enter the limit : "))
num_list = []
sum = 0

for i in range(limit):
    num_list.append(int(input(f"Enter number {i+1} : ")))

print(f"\nYour list contains following numbers : {num_list}\n")


for i in num_list:
    if i % 2 == 0:
        sum += i

print(f"\nSum of all even numbers is : {sum}\n")
