from stack import Stack

print("\nLet's play Towers of Hanoi!!\n")

#Create the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")

stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
num_disk = 0
while num_disk < 3:
    try:
        print("Please choose at least 3 or more disks.")
        num_disk = int(input("How many disks do you want to play with?\n"))
    except ValueError:
        print("Input a number please.")
    else:
        print(f"You want to play with {num_disk} disks.\n")

for i in range(num_disk, 0, -1):
    left_stack.push(i)

num_optimal_moves = pow(2, num_disk) - 1

print(f"\nThe fastest you can solve this game is in {num_optimal_moves} moves.")

#Get User Input
def get_input():
    choices = [i.get_name()[0] for i in stacks]
    while True:
        for i in range(len(stacks)):
            name = stacks[i].get_name()
            letter = choices[i]
            print(f"Enter {letter} for {name}")
        
        user_input = input("")
        if user_input in choices:
            for i in range(len(stacks)):
                if user_input == choices[i]:
                    return stacks[i]

#Play the Game
num_user_moves = 0
while right_stack.get_size() != num_disk:
    print("\n\n\n...Current Stacks...")
    for i in stacks:
        i.print_items()
    while True:
        print("\nWhich stack do you want to move from?\n")
        from_stack = get_input()
        print("\nWhich stack do you want to move to?\n")
        to_stack = get_input()
        
        if from_stack.is_empty():
            print("\n\nInvalid Move. Try Again")
        elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            disk = from_stack.pop()
            to_stack.push(disk)
            num_user_moves += 1
            break
        else:
            print("\n\nInvalid Move. Try Again")

print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")