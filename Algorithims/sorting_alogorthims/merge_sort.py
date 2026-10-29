def MergeSort(myList):
    if len(myList) <= 1:
        return myList

    mid_index = len(myList) // 2
    firstHalf = myList[:mid_index]
    secondHalf = myList[mid_index:]

    firstHalf = MergeSort(firstHalf)
    secondHalf = MergeSort(secondHalf)

    sortedList = []
    first_index = 0
    second_index = 0

    while first_index < len(firstHalf) and second_index < len(secondHalf):
        if firstHalf[first_index] < secondHalf[second_index]:
            sortedList.append(firstHalf[first_index])
            first_index += 1
        else:
            sortedList.append(secondHalf[second_index])
            second_index += 1

    sortedList.extend(firstHalf[first_index:])
    sortedList.extend(secondHalf[second_index:])

    return sortedList


myList = [33,65,77,49,26,93,56,25,24,4,17,7,3,80,92,45,70,14,74,16,78,71,35,91,44,51,53,52,60,73,89,32,96,54,81,87,20,38,27,68,62,95,21,84,100,86,18,2,5,12,58,79,97,22,55,94,15,41,46,83,88,48,59,19,8,76,9,85,61,50,57,13,6,90,23,39,1,30,82,36,69,66,37,67,99,64,28,11,72,63,43,40,34,42,98,47,29,31,10,75]

print(f"Unsorted: {myList}")
myList = MergeSort(myList)
print(f"Sorted: {myList}")