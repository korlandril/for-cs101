##CS101
##Program 3
##Tarsus Arciga
##taa522@mail.umkc.edu
##
##PROBLEM: Imitate genetic algorithms and breed the ultimate pokemon
##...Predefine a string, create populations of strings increasingly less degenerate and create offspring from them
## until you get... well... the ultimate pokemon.
##
##ALGORITHM:
##      1. Generate a random population of 500 random strings of characters as long as the ideal string.
##      2. Go through every string in the population and determine the lowest fitness score out of the bunch
##      (defined by the absolute value of the ordinal difference betwe.... yeah, you know)
##      3. Find the average of all the fitness score, put all the above average strings into a breeding population
##      4. Create 500 new children from the breeding population, randomly selecting parents and traits
##      5. Account for the 1% chance that a character will mutate up by one ordinal value
##      6. Discard the breeding population and the previous population
##      7. Repeat repeat repeat until the desired string is achieved
##
##ERROR HANDLING: ...IndexError. Hahah. Hah.
##
##OTHER COMMENTS: Not gonna lie, it took me like half an hour to figure out where Pr. Bingham's header guide was lol
##For the life of me, I couldn't get this thing to run 100% of the time without getting an IndexError. You'll see my
## other frustrated comments right at where the error is stemming from.
##So... I... fixed it. Kind of. It was the best I could do. I've tried leaving and coming back to this dilemma all week
##to no avail. It is what it is, I guess!


import random
#############################################################################
# Let's get them starter variables in here
IDEAL_STRING = "See you space cowboy..."
# This can be a pokemon if you want it to be a pokemon.
# No, really, everything in this program is based on the length of the IDEAL_STRING instead of hard-coded values.
BEST_POSSIBLE_SCORE = 0
current_best_score = 9999
pointsToDeductMe = 0
random_population = []
breeding_population = []
best_possible_string = ""
############################################################################

##############################################################
# This generates the initial random population to work with.
for i in range(0, 500):
    random_parent = ""
    for k in range(len(IDEAL_STRING)):
        random_parent += chr(random.randint(31, 126))
    random_population.append(random_parent)
#############################################################


while True:
    try: # Because we all know that sometimes kids are never going to be more than average :\
    # That's why I dropped my double major in Cello Performance and just kept the Computer Science...

        current_population = random_population

        while current_best_score != BEST_POSSIBLE_SCORE: # Until we get a perfect string, keep going
            score_of_all_strings = 0
            average_set_score = 0

            for current_parent in current_population: # Iterate through every string in the current population given
                current_string_score = 0
                for char in range(len(current_parent)): # Iterate through every character in the current string
                    current_difference = abs(ord(IDEAL_STRING[char]) - ord(current_parent[char]))
                    # Finds the absolute value of the ordinal sum of the ideal minus the ordinal sum of the current string.
                    current_string_score += current_difference

                if current_string_score < current_best_score:
                    current_best_score = current_string_score
                    score_of_all_strings += current_string_score
                    best_possible_string = current_parent
                else:
                    score_of_all_strings += current_string_score
                # If it's a slightly more viable string, remember it. Either way, contribute to the grand score

            print("Best fit so far: \"" + best_possible_string + "\" Score:" + str(current_best_score))

            average_set_score = score_of_all_strings/len(current_population)

            for current_parent in current_population:
                current_string_score = 0

                for char in range(len(current_parent)):
                    current_difference = abs(ord(IDEAL_STRING[char]) - ord(current_parent[char]))
                    current_string_score += current_difference
                if current_string_score < average_set_score:
                    breeding_population.append(current_parent)
            # We iterate through the current population again to figure out what's actually worth breeding
            # BUT WHAT HAPPENS WHEN ALL THE STRINGS ARE BELOW AVERAGE???
            # I spent hours scratching my head and consulting Piazza and I still am completely clueless. Please tell me.

            current_population = []
            # Everyone who was just blah was killed off by the aristocratic elite

            for l in range (0, 500): # Time to make babies
                breed1 = random.choice(breeding_population)
                breed2 = random.choice(breeding_population)
                # Parents can have multiple partners. Also they can be asexual lol.
                # I didn't think it was super necessary to make sure that the two parents weren't the same
                new_child = ""

                for m in range(len(IDEAL_STRING)): # make that new child as long as the ideal string
                    char_to_copy = ''
                    whatTrait = random.random()  # I'm mixing camelCase with underscores :o

                    if whatTrait < 0.5: # Got breed1's trait
                        char_to_copy = breed1[m]
                        if random.random() < 0.01: # ew it mutated
                            char_to_copy = chr(ord(breed1[m]) + 1)
                            new_child += char_to_copy
                        else:
                            new_child += \
                                char_to_copy

                    elif whatTrait >= 0.5: # Got breed2's trait
                        char_to_copy = breed2[m]
                        if random.random() < 0.01:
                            # there's absolutely no reason i used a separate int to store the value of whatTrait.
                            # i guess i'm that edgy
                            char_to_copy = chr(ord(breed2[m]) + 1)
                            new_child += char_to_copy
                        else:
                            new_child += char_to_copy

                current_population.append(new_child)
            breeding_population = []
            # don't forget to make the children eat their own parents in order to survive the cold, harsh winter
        break

    except IndexError: # Average...ness... is inevitable
        print("Offspring were all average or below average, so they all died off. \n Just like my grade for this "
              "assignment did. \n rebooting the Star Trek franchise...")
        pointsToDeductMe += 1
        # You kill everyone and start all over again.

print("We made it to the end! Only had to reboot the population " + str(pointsToDeductMe) + " times in order"
        " to achieve obscure anime references.")
# At least it doesn't crash, right? RIIIGHT? :c