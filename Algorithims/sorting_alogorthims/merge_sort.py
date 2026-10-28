def MergeSort(myList):
    times = 0 
    mid_index = len(myList) // times
    firstHalf = myList[:mid_index]
    secondHalf = myList[mid_index:]
    while True: 
        times += 2 
        # figure out how to append to myList correctly 
        for i in range(len(firstHalf) - 1):
            num_1 = firstHalf[i]
            num_2 = firstHalf[i + 1]
            if num_1 > num_2:
                firstHalf[i] = num_2
                firstHalf[i + 1] = num_1
        for i in range(len(secondHalf) - 1):
            num_1 = secondHalf[i]
            num_2 = secondHalf[i + 1]
            if num_1 > num_2:
                secondHalf[i] = num_2
                secondHalf[i + 1] = num_1
        if # need to figure out what condition to put here:
            False
        first_index = len(firstHalf) // times
        second_index = len(secondHalf) // times
        firstHalf = firstHalf[:first_index]
        secondHalf = firstHalf[first_index:]
        thirdHalf = secondHalf[:second_index]
        fourthHalf = secondHalf[second_index:]
        
        


myList = [33,65,77,49,26,93,56,25,24,4,17,7,3,80,92,45,70,14,74,16,78,71,35,91,44,51,53,52,60,73,89,32,96,54,81,87,20,38,27,68,62,95,21,84,100,86,18,2,5,12,58,79,97,22,55,94,15,41,46,83,88,48,59,19,8,76,9,85,61,50,57,13,6,90,23,39,1,30,82,36,69,66,37,67,99,64,28,11,72,63,43,40,34,42,98,47,29,31,10,75]
print(f"Unsorted: {myList}")
MergeSort(myList)
print(f"Sorted: {myList}")