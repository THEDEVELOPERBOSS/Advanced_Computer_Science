from time import perf_counter

def SelectionSort(myList):
    for i in range(len(myList)):
        min_index = i
        small_num = i + 1
        for j in range(small_num, len(myList)):
            if myList[j] < myList[min_index]:
                min_index = j 
        temp = myList[i]
        myList[i] = myList[min_index]
        myList[min_index] = temp
    return myList

def BubbleSort(myList):
    while True:
        swapped = False
        for i in range(len(myList) - 1):
            num_1 = myList[i]
            num_2 = myList[i + 1]
            if num_1 > num_2:
                myList[i] = num_2 # this could also be done without num_1 and num_2 using a tuple assignment 
                myList[i + 1 ] = num_1
                swapped = True
        if not swapped:
            break
    return myList
def InsertionSort(myList):
    for i in range(1, len(myList)):
        current = myList[i]
        j = i - 1 
        while j >= 0 and myList[j] > current:
            myList[j + 1] = myList[j]
            j -= 1 
        myList[j + 1] = current
    return myList
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
start = perf_counter()
print(f"Selection Sort: {SelectionSort(myList)}")
end = perf_counter()
print(f"Selection Sort Time: {end-start}")
start = perf_counter()
print(f"Bubble Sort: {BubbleSort(myList)}")
end = perf_counter()
print(f"Bubble Sort Time: {end-start}")
start = perf_counter()
print(f"Insertion Sort: {InsertionSort(myList)}")
end = perf_counter()
print(f"Insertion Sort Time: {end-start}")
start = perf_counter()
print(f"Merge Sort: {MergeSort(myList)}")
end = perf_counter()
print(f"Merge Sort Time: {end-start}")
start = perf_counter()
print(f"Quick sort: {QuickSort(myList)}")
end = perf_counter()
print(f"Quick Sort Time: {end-start}")