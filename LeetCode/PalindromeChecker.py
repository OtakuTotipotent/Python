def isPalindrome(num):
    if (num < 0) or (num % 10 == 0 and num != 0):
        return False

    reversed_half = 0
    while num > reversed_half:
        reversed_half = (reversed_half * 10) + (num % 10)
        num = num // 10

    if num == reversed_half or num == reversed_half // 10:
        return True

    return False


num = int(input("Please Enter a number : "))

if isPalindrome(num):
    print("YES! The number is PALINDROME")
else:
    print("NOPE! The number is NOT a PALINDROME")
