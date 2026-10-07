def factorial(number, result):
    if number == 0:
        return result 
    else:
        print(result)
        result = result * number
        number -= 1
        factorial(number, result)
number = int(input("Enter a number\n"))
result = number
number -= 1
factorial(number, result)

print(result)