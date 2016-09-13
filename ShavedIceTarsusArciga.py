# Shaved Ice program whoopeeeee
#
# TODO: Write doc for this thingamabob and don't forget to comment so the grader doesn't count off points
# TODO: Clean up the code with some more convenient variable names
# TODO: Fix number of days played

import random


exit_ticket = "yes"

print("Welcome to shaved ice simulator 2016!")

while exit_ticket == "yes" or exit_ticket == "y":
    daily_profit_or_loss = 0.0
    temperature = 0
    rain = False
    chance_for_rain = 0
    cost_per_cone = 0.50
    desired_cones = 0
    desired_price = -1.0
    max_customers = 0
    daily_customers = 0
    daily_count = 0
    total_money = 5.0
    actual_sold = 0


    for k in range(1, 11):
        chance_for_rain = random.randint(1, 100)

        if chance_for_rain <= 10:
            rain = True
        temperature = random.randint(70, 110)

        print("day " + str(k) + " you have $" + str(total_money) + " in the bank")

        if rain:
            print("It is raining and " + str(temperature) + " degrees outside")
        else:
            print("It is clear and " + str(temperature) + " degrees outside")

        desired_cones = int(input("How many cones of Shaved Ice will you make?"))

        break_my_program = True

        while break_my_program:
            if desired_cones < 0:
                print("You must enter 0 or more cones")
                desired_cones = int(input("How many cones of Shaved Ice will you make?"))
            elif desired_cones * cost_per_cone > total_money:
                print("You don't have enough money to make that many cones")
                desired_cones = int(input("How many cones of Shaved Ice will you make?"))
            else:
                break_my_program = False

        while desired_price <= 0:
            desired_price = float(input("What price do you charge per cone?"))
            if desired_price <= 0:
                print("Must enter greater than 0")

        if rain:
            max_customers = int((((temperature - 70) * 0.5) / desired_price) / 2)
        else:
            max_customers = int(((temperature - 70) * 0.5) / desired_price)

        print("max customers today is " + str(max_customers))
        daily_customers = random.randint(0, max_customers)
        print("daily customer today is " + str(daily_customers))

        if (desired_cones < daily_customers):  # Pls tell me if there's a more efficient way to do this
            daily_profit_or_loss = (desired_price * desired_cones) - (
                desired_cones * cost_per_cone)
            actual_sold = desired_cones
        else:
            daily_profit_or_loss = (desired_price * daily_customers) - (
                desired_cones * cost_per_cone)
            actual_sold = daily_customers

        print("You made " + str(desired_cones) + " cones of Shaved Ice costing you $" + str(
            desired_cones * cost_per_cone))
        print("You sold " + str(actual_sold) + " taking in $" + str(
            desired_price * actual_sold) + " for a daily profit/"
                                                   "loss of " + str(daily_profit_or_loss))
        total_money += daily_profit_or_loss
        if total_money < cost_per_cone:
            break

        k += 1
        desired_price = -1.0

    if total_money <= cost_per_cone:
        print("You do not have enough money in the bank to make any Shaved Ice. Thanks for playing")

    print("You played " + str(k) + " days of the simulation and ended with $" + str(total_money))

    exit_ticket = input("Do you want to play again? Y/YES/N/NO").lower()

    if exit_ticket == "y" or exit_ticket == "yes":
        continue
    elif exit_ticket == "n" or exit_ticket == "no":
        break
    else:
        print("You must input Y or N only")
        exit_ticket = input("Do you want to play again? Y/YES/N/NO").lower()

print("Game successfully ended")