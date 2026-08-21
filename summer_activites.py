activties = ['Sleep', 'Coding', 'Eating', 'Mowing'] 
outside = []
inside = []

def add_activity():
    while True:
        user_input = input('Type what you want to add seperated by pressing enter. Type done when finished ').strip()

        if user_input.lower() == 'done':
            break

        new_items = user_input.split()
        for item in new_items:
            activties.append(user_input) 
def out_in():
    for item in activties:
        user_input = input(f'Is {item} indoor or outdoor? ').strip().lower()

        if user_input == 'outdoor':
            outside.append(item)
            break
        elif user_input == 'indoor':
            inside.append(item)
            break
        else:
            print("Please enter a valid option")
def remove():
    print("What would you like to remove")
while True:
    print('What do you want to do?')
    print(activties)
    print('1. Add Activity')
    print('2. Categorize into outdoor/inside')
    print('3. Remove an activity')
    print('Q. Quit')

    user_input = input().strip()
    if user_input == '1':
        add_activity()
    elif user_input == '2':
        out_in()
    elif user_input == '3':
        remove()
    elif user_input.lower() == 'q':
        quit()
