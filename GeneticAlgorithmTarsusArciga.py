# Genetic algorithm yayyyyyyyyyyyyy
#
#please help oh myh gosh
#
#
#

import random


IDEAL_STRING = "See you Space Cowboy..."
BEST_POSSIBLE_SCORE = 0
current_best_score = 9999
pointsToDeductMe = 0
random_population = []
breeding_population = []
best_possible_string = ""

for i in range(0, 500):
    random_parent = ""
    for k in range(len(IDEAL_STRING)):
        random_parent += chr(random.randint(31, 126))
    random_population.append(random_parent)


while True:
    try:
        current_population = random_population
        while current_best_score != BEST_POSSIBLE_SCORE:
            score_of_all_strings = 0
            average_set_score = 0


            for current_parent in current_population:
                current_string_score = 0
                for char in range(len(current_parent)):
                    current_difference = abs(ord(IDEAL_STRING[char]) - ord(current_parent[char]))
                    current_string_score += current_difference

                if current_string_score < current_best_score:
                    current_best_score = current_string_score
                    score_of_all_strings += current_string_score
                    best_possible_string = current_parent
                else:
                    score_of_all_strings += current_string_score

            print("Best fit so far: " + best_possible_string + " Score:" + str(current_best_score))

            average_set_score = score_of_all_strings/len(current_population)

            for current_parent in current_population:
                current_string_score = 0
                for char in range(len(current_parent)):
                    current_difference = abs(ord(IDEAL_STRING[char]) - ord(current_parent[char]))
                    current_string_score += current_difference
                if current_string_score < average_set_score:
                    breeding_population.append(current_parent)

            current_population = []




            for l in range (0, 500):
                breed1 = random.choice(breeding_population)
                breed2 = random.choice(breeding_population)

                new_child = ""

                for m in range(len(IDEAL_STRING)):
                    char_to_copy = ''
                    whatTrait = random.random()
                    #mutationChance = random.random()

                    if whatTrait < 0.5:
                        char_to_copy = breed1[m]
                        if random.random() < 0.01:
                            char_to_copy = chr(ord(breed1[m]) + 1)
                            new_child += char_to_copy
                        else:
                            new_child += char_to_copy

                    elif whatTrait >= 0.5:
                        char_to_copy = breed2[m]
                        if random.random() < 0.01:
                            char_to_copy = chr(ord(breed2[m]) + 1)
                            new_child += char_to_copy
                        else:
                            new_child += char_to_copy

                current_population.append(new_child)
            breeding_population = []
        break

    except IndexError:
        print("Offspring were all average or below average, so they all died off. \n Just like my grade for this "
              "assignment did. \n rebooting the human race...")
        pointsToDeductMe += 1

print("We made it to the end! Only had to reboot the population " + str(pointsToDeductMe) + " times in order"
        " to find the perfect child fit for obscure anime references.")