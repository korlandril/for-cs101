# Genetic algorithm yayyyyyyyyyyyyy
#
#
#
#
#

import random

IDEAL_STRING = "See you later, Space Cowboy"
BEST_POSSIBLE_SCORE = 0
current_best_score = 9999

random_population = []

for i in range(0, 501):
    random_parent = ""
    for k in range(0, len(IDEAL_STRING)):
        random_parent += chr(random.randint(31, 126))
    random_population.append(random_parent)

current_population = random_population
breeding_population = []

while current_best_score != BEST_POSSIBLE_SCORE:
    best_possible_string = ""
    score_of_all_strings = 0
    average_set_score = 0

    for current_parent in current_population:
        current_string_score = 0
        print("Current string iterating: " + current_parent)
        for char in range(0, len(current_parent) -1):
            current_difference = abs(ord(IDEAL_STRING[char]) - ord(current_parent[char]))
            #print(IDEAL_STRING[char],current_parent[char],current_difference)
            current_string_score += current_difference

        if current_string_score < current_best_score:
            current_best_score = current_string_score
            score_of_all_strings += current_string_score
            best_possible_string = current_parent
        else:
            score_of_all_strings += current_string_score
        print(current_string_score, current_population.index(current_parent), best_possible_string)
        #print("Best fit so far: " + best_possible_string + " Score:" + str(current_best_score))
