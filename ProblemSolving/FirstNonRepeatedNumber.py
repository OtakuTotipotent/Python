limit = int(input("Enter limit : "))
num_list = []

for i in range(limit):
    num_list.append(int(input("Enter the number : ")))

for i in num_list:
    if num_list.count(i) == 1:
        print(i)
        break
