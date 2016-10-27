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

import codecs

# def convert_file_to_string():
#     #TODO: STUB
#
# def strip_common(text):
#     #TODO: STUB
#
# def string_to_list(text):
#     """Every word becomes an element in a list"""
#     #TODO: STUB
#
# def list_to_dict(lst):
#     """Converts a list to a dict and maps the number of occurrences of the same element to the value of every word"""
#     #TODO: STUB
#
# def calculate_word_commonality(text1, dict1, text2, dict2):
#     #TODO: STUB
#     #Compare two dictionaries????
# def calculate_word_frequency(dict1):
#     #TODO: STUB
#     #return a dict
# def calculate_relative_freqeuncy(text1, dict1, text2, dict2):
#     #TODO: STUB
#     #takes dictionaries. maybe

trump = open("trump.txt", 'r')
clinton = open("clinton.txt", 'r', encoding="utf-8")
romney = open("romney.txt",'r', encoding="utf-8")
obama = open("obama.txt",'r', encoding="utf-8")

mystery1 = open("mystery1.txt",'r', encoding="utf-8")
mystery2 = open("mystery2.txt",'r', encoding="utf-8")
mystery3 = open("mystery3.txt",'r', encoding="utf-8")
mystery4 = open("mystery4.txt",'r', encoding="utf-8")

