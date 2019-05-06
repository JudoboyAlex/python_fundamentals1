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
