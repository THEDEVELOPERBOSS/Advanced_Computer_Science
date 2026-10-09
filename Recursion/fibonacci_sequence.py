num_1 = 0
num_2 = 1
num_3 = 1
def fibonacci(times, num_1, num_2, num_3):
    if times == 0:
        return 
    else:
        num_3 = num_1
        num_1 = num_2 + num_1
        print(f"{num_1}")
        num_2 = num_3 
        times -= 1 
        fibonacci(times, num_1, num_2, num_3)
times = int(input("How many numbers of the fibonacci sequence would you like to see?\n"))
fibonacci(times, num_1, num_2, num_3)