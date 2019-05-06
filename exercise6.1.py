# Allow the user to go home when they are done exercising. The program should stop asking for input if the user enters 'go home'.   
# See if you can also make the program tell the user when they have entered a command that does not exist.

distance_count = 0

while distance_count >= 0:
    print("Do you want to run or walk?")
    action = input()
    if action == "walk":
        print("Distance from home is {}km.".format(distance_count + 1))
        distance_count += 1
    elif action == "run":
        print("Distance from home is {}km.".format(distance_count + 5))
        distance_count += 5
    elif action == "go home":
        print("Good job! Sprint back to home now hahaha!")
        break
    else: 
        print("You entered wrong command")  

