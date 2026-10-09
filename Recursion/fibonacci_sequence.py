num_1 = 1
num_2 = 2 
def fibonacci(times, num_1, num_2):
    if times == 0:
        return 
    else:
        num_1 = num_2 + num_1
        print(f"{num_1}, {num_2}")
        times -= 1 
times = int(input("How many numbers of the fibonacci sequence would you like to see?\n"))
fibonacci(times, num_1, num_2)