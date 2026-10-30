```python
def QuickSort(myList):
    if len(myList) <= 1:
        return myList

    pivot = myList[-1]
    partition_index = 0

    for i in range(len(myList) - 1):
        if myList[i] < pivot:
            temp = myList[i]
            myList[i] = myList[partition_index]
            myList[partition_index] = temp
            partition_index += 1

    temp = myList[-1]
    myList[-1] = myList[partition_index]
    myList[partition_index] = temp

    left = QuickSort(myList[:partition_index])
    right = QuickSort(myList[partition_index + 1:])

    return left + [pivot] + right


myList = [33,65,77,49,26,93,56,25,24,4,17,7,3,80,92,45,70,14,74,16,78,71,35,91,44,51,53,52,60,73,89,32,96,54,81,87,20,38,27,68,62,95,21,84,100,86,18,2,5,12,58,79,97,22,55,94,15,41,46,83,88,48,59,19,8,76,9,85,61,50,57,13,6,90,23,39,1,30,82,36,69,66,37,67,99,64,28,11,72,63,43,40,34,42,98,47,29,31,10,75]

print(f"Unsorted: {myList}")
myList = QuickSort(myList)
print(f"Sorted: {myList}")
```