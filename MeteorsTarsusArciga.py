##CS101
##Program 4
##Tarsus Arciga
##taa522@mail.umkc.edu
##
##PROBLEM: Take input from a file that contains meteorite data and output specified data from
## given radii and geolocations from the user to another file.
##
##ALRGORITHM:
##1.  Prompt the user for the file to read from and the file to write to
##2.  Prompt the uesr for the desired latitude and longitutde and  mile radius to search in given coordinates
##3.  Check every meteorite entry to see if it's within the given radius,
## and write its information to the output file given the meteorite matches given criteria
##4. Repeat until the user wishes to exit the program
##
##ERROR HANDLING:
##FileNotFoundError
##ValueError
##OSError
##OTHER COMMENTS:
## I noticed in the videos that this class requires you to do the pre and post condition things when you define functions.
## Is that really true?
# TODO: Prompt the user whether or not they want to restart the program again
# TODO: Document, document, document

import math
#####################################
exit_ticket = "y"
#####################################


############################FANCY SCHMANCY FUNCTIONS###########################################################
def get_file(prompt, process_type):
    """This gets a file with a set prompt and processing type for the file."""
    while True:
        try:
            file = open(str(input(prompt)), process_type, encoding="utf-8")
            return file
        except FileNotFoundError:
            print("WARNING. Inputted file not found. Please try again.")
        except OSError:
            print("pls stop trying to break my program :/ i don't even know why using an asterisk returns an OSError")

def get_coordinates():
    """This prompts the user for the desired to geolocation to search in and returns a tuple filled with the coordinates."""

    while True:
        try:
            latitude = float(input("What is your desired latitude?"))
            while latitude < -90 or latitude > 90:
                latitude = float(input("Invalid input for latitude. You must enter a number between -90 and 90."))

            longitude = float(input("What is your desired longitude?"))
            while longitude < -180 or longitude > 180:
                longitude = float(input("Invalid input for longitude. You must enter a number between -180 and 180."))
            coordinates = (latitude, longitude)
            return coordinates

        except ValueError:
            print("You did not enter a number. Please try again.")


    #See, I could splice a string at the comma, store the values in a tuple and convert them to ints
    #But I don't want to bother accounting for invalid input.

    return coordinates

def get_radius():
    while True:
        try:
            radius = float(input("What is the radius you'd like to search in your given coordinates?"))
            while radius <= 0:
                float(input("You need to enter a number over 0 for the radius."))
            break
        except ValueError:
            print("You did not enter a number. Please try again.")
    return radius

def is_within_radius(point_of_origin, point_to_compare, radius):
    """Figures out if two given points are within the radius given"""
    lat1 = math.radians(point_of_origin[0])
    lat2 = math.radians(point_to_compare[0])
    long1 = math.radians(point_of_origin[1])
    long2 = math.radians(point_to_compare[1])

    deltaLong = long2 - long1
    deltaLat = lat2 - lat1

    a = (math.sin(deltaLat/2) ** 2) + (math.cos(lat1)) * (math.cos(lat2)) * (math.sin(deltaLong/2) ** 2)
    c = 2 * (math.atan2(math.sqrt(a), math.sqrt(1 -a)))
    distance_in_miles = 3961 * c

    if distance_in_miles <= radius:
        return True
    else:
        return False

def get_coordinates_from_line(document):
    coordinates = document[165:].strip()
    newer = eval(coordinates)
    return newer
#################################################################################################################


#######################################################Main Loop#################################################
while exit_ticket == "y" or exit_ticket == "yes":

    file_to_read = get_file("Please enter the name of the file you want to pull meteorite data from.", 'r')
    file_to_write = get_file("Please enter the name of the file you would like to output data to.", 'r+')
    file_to_write.write(file_to_read.readline())

    desired_coordinates = get_coordinates()
    print(desired_coordinates)

    desired_radius = get_radius()

    while True:
        try:
            for line in file_to_read:
                 if is_within_radius(desired_coordinates, get_coordinates_from_line(line), desired_radius) == True:
                     file_to_write.write(line)
            break
        except NameError:
            continue
        except SyntaxError:
            continue
    print("Operation successfully completed. Meteorites within specified range have been added to the output file.")

    exit_ticket = input("Would you like to run the program again? Y/YES/N/NO").lower()

#######################################################################################################################
file_to_read.close()
file_to_write.close()


