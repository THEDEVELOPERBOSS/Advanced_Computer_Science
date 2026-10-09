def LinearSearch(myList, desired_num):
    attempts = 0 
    for i in myList:
        if i == desired_num:
            print(f"Found {desired_num} at {attempts}")
            break
        else: 
            attempts += 1 
            print(f"Not able to find it. Attempts: {attempts}")
    print("Number is not in list ")
myList = [33,65,77,49,26,93,56,25,24,4,17,7,3,80,92,45,70,14,74,16,78,71,35,91,44,51,53,52,60,73,89,32,96,54,81,87,20,38,27,68,62,95,21,84,100,86,18,2,5,12,58,79,97,22,55,94,15,41,46,83,88,48,59,19,8,76,9,85,61,50,57,13,6,90,23,39,1,30,82,36,69,66,37,67,99,64,28,11,72,63,43,40,34,42,98,47,29,31,10,75]

desired_num = int(input("What number do you want to find?(1-100)\n"))
LinearSearch(myList, desired_num)