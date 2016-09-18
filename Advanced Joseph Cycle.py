OriginalList = []
original = 1

maximum = input("Please type in the length of the list:\n")

StepList = list(input("Please type in the list of steps in the format of '1,2,3':\n"))

while original <= maximum:
    OriginalList.append(original)
    original += 1

OriginalDict = dict(zip(OriginalList, StepList))

print ("Original Dictionary:\n{}".format(OriginalDict))
print ("Original List:\n{}".format(OriginalList))

n = 1
count = 1

while len(OriginalList) > 1:
    i = 1
    index = 0
    while i <= len(OriginalList):
        if count % OriginalDict[n] == 0:
            n = OriginalDict[OriginalList[index]]
            OriginalList.pop(index)
            index -= 1
            i -= 1
            print(OriginalList)
        count += 1
        index += 1
        i += 1
        
