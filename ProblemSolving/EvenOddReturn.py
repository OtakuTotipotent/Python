def evenOddGenerator(limit=10):
    evenList = []
    oddList = []
    for i in range(1, limit + 1):
        if i % 2 == 0:
            evenList.append(i)
        else:
            oddList.append(i)
    return evenList, oddList


evenNum, oddNum = evenOddGenerator()

print(evenNum)
print(oddNum)

