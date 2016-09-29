# Genetic algorithm yayyyyyyyyyyyyy
#
#please help oh myh gosh
#
#
#

import random

IDEAL_STRING = "See you later, Space Cowboy"
BEST_POSSIBLE_SCORE = 0
current_best_score = 9999

random_population = []

for i in range(0, 500):
    random_parent = ""
    for k in range(0, len(IDEAL_STRING)):
        random_parent += chr(random.randint(31, 126))
    random_population.append(random_parent)

current_population = random_population
breeding_population = []

#################################################################
# best_possible_string = ""
# score_of_all_strings = 0
# average_set_score = 0
#
# for current_parent in current_population:
#     current_string_score = 0
#     # print("Current string iterating: " + current_parent)
#
#     for char in range(0, len(current_parent) - 1):
#         current_difference = abs(ord(IDEAL_STRING[char]) - ord(current_parent[char]))
#         # print(IDEAL_STRING[char],current_parent[char],current_difference)
#         current_string_score += current_difference
#
#     if current_string_score < current_best_score:
#         current_best_score = current_string_score
#         score_of_all_strings += current_string_score
#         best_possible_string = current_parent
#     else:
#         score_of_all_strings += current_string_score
#
# print("Best fit so far: " + best_possible_string + " Score:" + str(current_best_score))
#
# average_set_score = score_of_all_strings / len(current_population)
#
# for current_parent in current_population:
#     current_string_score = 0
#
#     for char in range(0, len(current_parent) - 1):
#         current_difference = abs(ord(IDEAL_STRING[char]) - ord(current_parent[char]))
#         current_string_score += current_difference
#     #print(current_string_score)
#     if current_string_score < average_set_score:
#         breeding_population.append(current_parent)
#
#     current_population = []
#
# print(breeding_population)
# print(len(breeding_population))
#
# for m in range(0, 500):
#     breed1 = random.choice(breeding_population)
#     breed2 = random.choice(breeding_population)
#     new_child = ""
#     #print(breed1, breed2)
#
#     for l in range(0, len(breed1)-1):
#         char_to_cop = ""
#         if random.random() < .5:
#             char_to_copy = breed1[l]
#             if random.random() < 0.01:
#                 char_to_copy = chr(ord(char_to_copy) + 1)
#                 new_child += char_to_copy
#             else:
#                 new_child += char_to_copy
#
#         elif random.random >= .5:
#             char_to_copy = breed2[l]
#             if random.random() < 0.01:
#                 char_to_copy = chr(ord(char_to_copy) + 1)
#                 new_child += char_to_copy
#             else:
#                 new_child += char_to_copy
#     print(new_child)



##################################################################

while current_best_score != BEST_POSSIBLE_SCORE:
    best_possible_string = ""
    score_of_all_strings = 0
    average_set_score = 0

    for current_parent in current_population:
        current_string_score = 0
        #print("Current string iterating: " + current_parent)

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

    print("Best fit so far: " + best_possible_string + " Score:" + str(current_best_score))

    average_set_score = score_of_all_strings/len(current_population)

    for current_parent in current_population:
        current_string_score = 0

        for char in range(0, len(current_parent)-1):
            current_difference = abs(ord(IDEAL_STRING[char]) - ord(current_parent[char]))
            current_string_score += current_difference
        if current_string_score < average_set_score:
            breeding_population.append(current_parent)

        current_population = []
        #print(breeding_population)

#TODO: Algorithm for creating a child is so, so fucked up. everything else pretty much works.
        for l in range (0, 500):
            breed1 = random.choice(breeding_population)

            # there's a one in 500 chance that breed1 and breed2 will be the same. :c do i get points off?
            breed2 = random.choice(breeding_population)


            new_child = ""

            for m in range(0, len(breed1) - 1):
                char_to_copy = ""

                if random.random() < 0.5:
                    char_to_copy = breed1[char]
                    if random.random() < 0.01:
                        char_to_copy = chr(ord(breed1[m]) + 1)
                    else:
                        new_child += char_to_copy

                elif random.random() >= 0.5:
                    char_to_copy = breed2[char]
                    if random.random() < 0.01:
                        char_to_copy = chr(ord(breed2[m]) + 1)
                    else:
                        new_child += char_to_copy
            current_population += new_child
    breeding_population = []
    print(current_population)

#UGHHHHHHHHHHHHHHHHGHHH