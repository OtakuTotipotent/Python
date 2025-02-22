roman = input("Please enter the Roman number : ")
roman = roman.upper()
roman_letters = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

num = 0
for i in range(len(roman) - 1):
    if roman[i] not in "IVXLCDM":
        print("Invalid Roman number")
        exit()
    elif roman_letters[roman[i]] < roman_letters[roman[i + 1]]:
        num -= roman_letters[roman[i]]
    else:
        num += roman_letters[roman[i]]
num += roman_letters[roman[-1]]

print(num)
