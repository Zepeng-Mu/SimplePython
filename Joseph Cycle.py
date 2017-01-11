OriginalList = []
original = 1

maximum = input("Please type in the length of the list:\n")
m = input("Please type in the value of step:\n")

while original <= maximum:
    OriginalList.append(original)
    original += 1

print ("Original List:\n{}".format(OriginalList))
count = 1

while len(OriginalList) > 1:
    i = 1
    index = 0
    while i <= len(OriginalList):
        if count % m == 0:
            OriginalList.pop(index)
            index -= 1
            i -= 1
            print(OriginalList)
        count += 1
        index += 1
        i += 1