def factorial(number, result):

    if number == 0:
        return result
    else:
        print(result)
        result = result * number
        number -= 1
        return factorial(number, result)  # Return the recursive call


number = int(input("Enter a number\n"))

result = number
number -= 1

result = factorial(number, result)  # Save the returned result

print(result)