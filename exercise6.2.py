# You started the day with energy, but you are going to get tired as you travel! Keep track of your energy.
# If you walk, your energy should increase. If you run, it should decrease. Moreover, you should not be able to run if your energy is zero.
# ...then, go crazy with it! Allow the user to rest and eat. Do whatever you think might be interesting.
# Congrats for making it this far!

distance_count = 0
energy = 100

while distance_count >= 0 and energy >= 0:
    print("Do you want to run or walk or go home?")
    action = input()
    if action == "walk":
        print("Distance from home is {}km. Your current energy level is {}".format(distance_count + 1, energy + 30))
        distance_count += 1
        energy += 30
    elif action == "run":
        print("Distance from home is {}km. Your current energy level is {}".format(distance_count + 5, energy - 50))
        distance_count += 5
        energy -= 50
    elif action == "rest":
        print("Good idea. Relax your body. Your energy level got boosted to {}".format(energy + 35))
        energy += 35
    elif action == "go home":
        print("Good job! Sprint back to home now hahaha!")
        break
    else: 
        print("You entered wrong command")  
        
    if energy <= 0:
        print("You are out of energy. Do you want to rest?(yes or no)")
        action2 = input()
        if action2 == "yes":
            print("Ok, you are good to go. Your energy level recovered to {}".format(energy + 35))
            energy += 35
        elif action2 == "no":
            print("Just make sure take it easy")
            break 
        else:
            print("You entered wrong command")