##CS101
##Program 5
##Tarsus Arciga
##taa522@mail.umkc.edu
##
##PROBLEM: Compare four speeches with four mystery texts and determine the highest word commonality
##and frequency between the files.
##
##ALRGORITHM:
## 1. Take every file and turn it into a string
## 2. Strip every string of punctuation and common words
## 3. Convert every string to a list (array), and then a dictionary (multidimensional array) assigning
## number of occurences to each word
## 4. For every mystery file, find the amount of common words between it and every known text and divide it by the sum of
## words unique to both speeches
## 5. For every mystery file,
##
##ERROR HANDLING:
##None
##
##
##
##OTHER COMMENTS:
##
##

###########################################Gee I sure love standard modules that won't get points deducted c:##########
import string
import copy
from math import sqrt
from collections import Counter
#######################################################################################################################

######################################Look at that beautiful comprehension#############################################
stopWords = open("stopWords.txt", 'r').readlines()
stop_list =[i.strip('\n') for i in stopWords]
# Takes out those nasty blank lines in between each stop word... if they're there, at least.
#######################################################################################################################



########################Yeah these took forever I should spend more time on my algorithms###############################
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
    sum_of_squares = sum(common_frequencies.values())

    frequency_similarity = sqrt(sum_of_squares / common_length)

    return frequency_similarity
#######################################################################################################################


############################################I hardcoded the names of the speecehs wheeeeeee############################

Trump = [Counter(file_to_clean_string(open("trump.txt", 'r'), stop_list)), "Trump"]
Clinton = [Counter(file_to_clean_string(open("clinton.txt", 'r'), stop_list)), "Clinton"]
Romney = [Counter(file_to_clean_string(open("romney.txt", 'r'), stop_list)), "Romney"]
Obama = [Counter(file_to_clean_string(open("obama.txt", 'r'), stop_list)), "Obama"]

mystery1 = [Counter(file_to_clean_string(open("mystery1.txt", 'r'), stop_list)),"mystery1"]
mystery2 = [Counter(file_to_clean_string(open("mystery2.txt", 'r'), stop_list)),"mystery2"]
mystery3 = [Counter(file_to_clean_string(open("mystery3.txt", 'r'), stop_list)),"mystery3"]
mystery4 = [Counter(file_to_clean_string(open("mystery4.txt", 'r'), stop_list)),"mystery4"]

#######################################################################################################################

known_texts = [Trump, Clinton, Romney, Obama]
mystery_texts = [mystery1, mystery2, mystery3, mystery4]

for text in mystery_texts:
    current_mystery = text[1]
    current_best_commonality = 0.0
    current_highest_freq = 99999.9
    best_common_speech = ""
    best_freq_speech = ""

    for known in known_texts:
        current_commonality = round(calculate_word_commonality(text[0],known[0]),4)

        if current_commonality > current_best_commonality:
            current_best_commonality = current_commonality
            best_common_speech = known[1]

        current_freq = round(calculate_frequency_similarity(text[0],known[0]),4)

        if current_freq < current_highest_freq:
            current_highest_freq = current_freq
            best_freq_speech = known[1]

    print("The text {} has the highest word commonality with {} ({}%)".format(current_mystery,
    best_common_speech, current_best_commonality))
    print("The text {} has the highest frequency similarity with {} ({})".format(current_mystery,
    best_freq_speech, current_highest_freq) + "\n")





#print(calculate_relative_frequency(trump))
#print(trump)

#print(calculate_frequency_similarity(Clinton, mystery4))


#print(calculate_word_commonality(romney, mystery2))
#print(calculate_relative_frequency(romney,mystery4))
#TODO: DOCUMENT THIS fustercluck



