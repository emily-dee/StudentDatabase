student_names = ['James Holden', 'Naomi Nagata', 'Alex Kamal', 'Amos Burton', 'Clarissa Mao', 'Bobby Draper']
student_hometowns = ['Bozeman', 'Ceres', 'Olympia', 'Baltimore', 'New York', 'Hecates']
student_foods = ['Coffee', 'Chips', 'Noodles', 'Chili', 'Mushroom Burgers', 'Curry']

#  Getting user pick
while True:
    student_pick = input(f'Which student would you like to learn about? '
                         f'Enter a number 1 - {len(student_names)} or a student name\n'
                         f'If you\'d like to see a list of all student names, please enter "all" \n>> ')

    while True:  # testing user input for type and converting it to valid index
        if any(student_pick in name for name in student_names):  # allowing user to type a name to select student
            student_name_pick = [e for e in student_names if student_pick in e]
            student_index = student_names.index(student_name_pick[0])
            break

        elif student_pick.isnumeric() and 0 < int(student_pick) <= len(student_names):  # checking for valid number
            student_index = int(student_pick) - 1  # turning the student pick into the correct index
            break

        elif student_pick == 'all':  # list the options
            listed_numbers = 1
            for i in student_names:
                print(f'{listed_numbers}. {i}')
                listed_numbers += 1
            print()
            student_pick = input(f'Which student would you like to learn about? Enter a number 1 - {len(student_names)} '
                                 f'or a student name >> ')
        else:  # trying again
            student_pick = input(
                f'Please select a valid student number from 1 - {len(student_names)} or a student name >> ')

    print()
    print(f"You've selected {student_names[student_index]}")
    print()

    # learning about the student pick
    while True:
        student_fact_pick = input(f"Would you rather learn about {student_names[student_index]}'s "
                                  f"favorite food or hometown? >> ").lower()
        if 'home' in student_fact_pick:
            print(f"{student_names[student_index]} is from {student_hometowns[student_index]}")
            break
        elif 'food' in student_fact_pick:
            print(f"{student_names[student_index]}'s favorite food is {student_foods[student_index]}")
            break
        else:
            print('Please pick a valid category')

    print()
    again = input('Would you like to learn about another student? y or n >> ')
    print()
    if again != 'y':
        break

print('Thanks!')
