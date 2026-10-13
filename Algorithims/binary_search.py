def binary_serach(myList, num):
    low = 0 
    high = len(myList) - 1
    while low <= high:
        mid = (low + high) // 2 
        if num == myList[mid]: 
            print(f"Number found at index {mid}")
            break
        elif num > myList[mid]:
            low = (mid + 1 )
        elif num < myList[mid]:
            high = (mid - 1)
    else:
        print("Number not in list")
myList = [2,7,11,30,39,40,78,86,91,98,105,108,112,129,139,151,169,174,185,209,210,221,225,244,250,263,278,292,303,307,309,346,363,372,374,386,407,410,411,422,423,437,440,446,454,455,457,464,469,477,488,509,519,532,533,538,575,580,588,605,608,614,653,658,663,670,683,686,689,722,727,746,758,763,780,784,790,794,805,812,843,846,849,857,864,873,886,916,917,942,951,957,965,972,982,985,991,995,998,1000]
num = int(input("What number would you like to find?:\n"))
binary_serach(myList, num)