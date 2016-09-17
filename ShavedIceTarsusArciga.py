# Shaved Ice Program!
# By Tarsus Arciga
#
# This program simulates a shaved ice stand. Don't be unwise with your money!

import random

# needed to generate random integers for this program


exit_ticket = "yes"  # sets up the game loop

while exit_ticket == "yes" or exit_ticket == "y":

    #####################Let's define these variables from the start to use later throughout the loop#############
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
    #############################################################################################################

    print("Welcome to shaved ice simulator 2016! \n")

    for k in range(1, 11):
        chance_for_rain = random.randint(1, 100)  # randomize the chance for rain

        if chance_for_rain <= 10:
            rain = True

        temperature = random.randint(70, 110)  # randomize the temperature

        print('day {} you have ${:03.2f} in the bank'.format(k, total_money))

        if rain:
            print('It is raining and {} degrees outside'.format(temperature))
        else:
            print('It is clear and {} degrees outside'.format(temperature))

        desired_cones = int(input("How many cones of Shaved Ice will you make?"))

        break_my_program = True  # just keep on entering bad input pls.

        while break_my_program:
            if desired_cones < 0:
                print("You must enter 0 or more cones")
                desired_cones = int(input("How many cones of Shaved Ice will you make?"))
            elif desired_cones * cost_per_cone > total_money:
                print("You don't have enough money to make that many cones")
                desired_cones = int(input("How many cones of Shaved Ice will you make?"))
            else:
                break_my_program = False

        while desired_price <= 0:  # i probably could have made the last loop like this instead of making a boolean, but
            # nah
            desired_price = float(input("What price do you charge per cone?"))
            if desired_price <= 0:
                print("Must enter greater than 0")

        if rain:
            max_customers = int((((temperature - 70) * 0.5) / desired_price) / 2)
            # max daily customers halves if its raining
        else:
            max_customers = int(((temperature - 70) * 0.5) / desired_price)
            #  ...and it isn't halved if it's clear

        daily_customers = random.randint(0, max_customers)  # randomize the daily customer count

        if (desired_cones < daily_customers):
            # if you made less cones then there were customers, you only get money from the amount you actually sold
            daily_profit_or_loss = (desired_price * desired_cones) - (
                desired_cones * cost_per_cone)
            actual_sold = desired_cones
        else:
            # otherwise you will profit from the daily customer amount
            daily_profit_or_loss = (desired_price * daily_customers) - (
                desired_cones * cost_per_cone)
            actual_sold = daily_customers

        print('You made {} cones of Shaved Ice costing you ${:03.2f}'
              .format(desired_cones, (desired_cones * cost_per_cone)))
        print('You sold {} taking in ${:03.2f} for a daily profit/loss of {}'
              .format(actual_sold, (desired_price * actual_sold), daily_profit_or_loss))
        total_money += daily_profit_or_loss

        k += 1  # start of a new day

        if total_money < cost_per_cone:
            break # you're out of money.  you're not allowed to go into debt in this game.

        desired_price = -1.0  # reset this particular value so that the price setting loop doesn't skip over the next iteration
        print("\n")

    if total_money <= cost_per_cone:
        print("You do not have enough money in the bank to make any Shaved Ice. Thanks for playing")

    print('You played {} days of the simulation and ended with ${:03.2f}'.format(k - 1, total_money))

    exit_ticket = input("Do you want to play again? Y/YES/N/NO").lower()
    validExit = False

    while not (validExit):  # you're gonna be smart and try and break my program with bad input again. :/
        if exit_ticket == "y" or exit_ticket == "yes":
            validExit = True
            continue
        elif exit_ticket == "n" or exit_ticket == "no":
            validExit = True
            break
        else:
            print("You must input Y or N only")
            exit_ticket = input("Do you want to play again? Y/YES/N/NO").lower()

    print("\n")

print("Game successfully ended")
