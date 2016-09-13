# Shaved Ice program whoopeeeee
#
# TODO: Write doc for this thingamabob and don't forget to comment so the grader doesn't count off points
# TODO: Fix the while loop checking to see if the player's moeny is below 0
#

import random

total_money = 5.0
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
exit_ticket = ""

print("Welcome to shaved ice simulator 2016!")

while exit_ticket is not ("no" or "n"):
    while total_money > 0.5:
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
            else:
                daily_profit_or_loss = (desired_price * daily_customers) - (
                    desired_cones * cost_per_cone)  #

            print("You made " + str(desired_cones) + " cones of Shaved Ice costing you $" + str(
                desired_cones * cost_per_cone))
            print("You sold " + str(daily_customers) + " taking in $" + str(
                cost_per_cone * daily_customers) + " for a daily profit/"
                                                   "loss of " + str(daily_profit_or_loss))
            total_money += daily_profit_or_loss

            daily_count += 1
            desired_price = -1.0

    if total_money <= 0:
        print("You do not have enough money in the bank to make any Shaved Ice. Thanks for playing")

    print("You played " + str(daily_count) + " days of the simulation and ended with $" + str(total_money))

    exit_ticket = input("Do you want to play again? Y/YES/N/NO").lower()

    if exit_ticket is not ("y" or "yes" or "n" or "no"):
        print("You must input Y or N only")
        exit_ticket = input("Do you want to play again? Y/YES/N/NO").lower()
