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
##
##OTHER COMMENTS:
##
##
#TODO: Parse the file for the desired input criteria, input meteorite information into the output file
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

def get_coordinates():
    """This prompts the user for the desired to geolocation to search in and returns a tuple filled with the coordinates."""

    while True:
        try:
            latitude = float(input("What is your desired latitude?"))
            while latitude < -90 or latitude > 90:
                latitude = int(input("Invalid input for latitude. You must enter a number between -90 and 90."))

            longitude = float(input("What is your desired longitude?"))
            while longitude < -180 or latitude > 180:
                longitude = int(input("Invalid input for longitude. You must enter a number between -180 and 180."))
            coordinates = (latitude, longitude)
            break

        except ValueError:
            print("You did not enter a number. Please try again.")


    #See, I could splice a string at the comma, store the values in a tuple and convert them to ints
    #But I don't want to bother accounting for invalid input.

    return coordinates

def get_radius():
    while True:
        try:
            radius = float(input("What is the radius you'd like to search in your given coordinates?"))
            break
        except ValueError:
            print("You did not enter a number. Please try again.")
    return radius

def is_within_radius():
    return False
    # TODO: STUB

def get_coordinates(document):
    while True:
        try:
            for line in document:
                coordinates = line[165:].strip()
                newer = eval(coordinates)
                print(newer[1])
            break
        except NameError:
            continue
        except SyntaxError:
            continue
    return None
    # TODO: STUB
#################################################################################################################


#######################################################Main Loop#################################################
while exit_ticket == "y" or exit_ticket == "yes":

    file_to_read = get_file("Please enter the name of the file you want to pull meteorite data from.", 'r')
    get_coordinates(file_to_read)
    #TODO: PARSE THE METEORITE COORDINATES WITHOUT AN ERROR PLEASE
    break

    #file_to_write = get_file("Please enter the name of the file you would like to output data to.", 'r+')


    # desired_coordinates = get_coordinates()
    # desired_latitude = desired_coordinates[0]
    # desired_longitude = desired_coordinates[1]
    #
    # desired_radius = get_radius()










# file_to_read.close()
# file_to_write.close()


