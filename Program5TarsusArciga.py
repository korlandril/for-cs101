##CS101
##Program 5
##Tarsus Arciga
##taa522@mail.umkc.edu
##
##PROBLEM: Compare four speeches with four mystery texts and determine the highest word commonality
##and frequency between the files.
##
##ALRGORITHM:
##yuck.
##
##
##ERROR HANDLING:
##
##
##
##
##OTHER COMMENTS:
##
##

import string
import copy
from math import sqrt
from collections import Counter

stopWords = open("stopWords.txt", 'r').readlines()
stop_list =[i.strip('\n') for i in stopWords]

def file_to_clean_string(file_to_clean, to_exclude):
    punctuation = set(string.punctuation)

    new_text = ""
    for line in file_to_clean:
        if line != "\n":
            new_text += line

    new_text = ''.join(ch for ch in new_text if ch not in punctuation).lower()

    clean_text_list = new_text.split()
    no_more_stop = [x for x in clean_text_list if x not in to_exclude]
    return no_more_stop

def calculate_word_commonality(speech1, speech2):
    first_speech = set(speech1)
    second_speech = set(speech2)

    first_speech_distinct = len(first_speech)
    second_speech_distinct = len(second_speech)

    words_in_common = len(first_speech.intersection(second_speech))

    commonality_percentage = (words_in_common / ((first_speech_distinct + second_speech_distinct) - words_in_common)* 100)

    return commonality_percentage

def calculate_relative_frequency(speech1):
    rel_freq = copy.deepcopy(speech1)
    grand_total = sum(rel_freq.values())

    for key, value in rel_freq.items():
        rel_freq[key] = rel_freq[key] / grand_total

    return rel_freq

def calculate_frequency_similarity(speech1, speech2):
    first_speech = set(speech1)
    second_speech = set(speech2)
    common_words = first_speech.intersection(second_speech)
    common_length = len(common_words)

    first_speech_freq = calculate_relative_frequency(speech1)
    second_speech_freq = calculate_relative_frequency(speech2)

    to_compare = [first_speech_freq, second_speech_freq]
    common_frequencies = dict()

    for speech in to_compare:
        for key,value in speech.items():
            if key in common_words:
                common_frequencies[key] = (first_speech_freq[key] - second_speech_freq[key]) ** 2
    sum_of_squares  = sum(common_frequencies.values())

    frequency_similarity = sqrt(sum_of_squares / common_length)

    return frequency_similarity

trump = Counter(file_to_clean_string(open("trump.txt", 'r'), stop_list))
clinton = Counter(file_to_clean_string(open("clinton.txt", 'r'), stop_list))
romney = Counter(file_to_clean_string(open("romney.txt", 'r'), stop_list))
obama = Counter(file_to_clean_string(open("obama.txt", 'r'), stop_list))

mystery1 = Counter(file_to_clean_string(open("mystery1.txt", 'r'), stop_list))
mystery2 = Counter(file_to_clean_string(open("mystery2.txt", 'r'), stop_list))
mystery3 = Counter(file_to_clean_string(open("mystery3.txt", 'r'), stop_list))
mystery4 = Counter(file_to_clean_string(open("mystery4.txt", 'r'), stop_list))





#print(calculate_relative_frequency(trump))
#print(trump)

print(calculate_frequency_similarity(clinton, mystery4))


#print(calculate_word_commonality(romney, mystery2))
#print(calculate_relative_frequency(romney,mystery4))



#TODO: Account for frequency similarity



