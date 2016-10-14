##CS101
##Program 4
##Tarsus Arciga
##taa522@mail.umkc.edu
##
##PROBLEM: Take input from a file that contains meteorite data and output specified data from
## given radii and geolocations from the user.
##
##ALRGORITHM:
##1.  Prompt the user for the file to read from and the file to write to
##2.  Prompt the uesr for the desired latitude and longitutde and  mile radius to search in given coordinates
##3.  Check every meteorite entry to see if it's within the given radius,
## and write its information to the output file given the meteorite matches given criteria
##4. Repeat until the user wishes to exit the program
##
##ERROR HANDLING:
##FileNotFound
##
##OTHER COMMENTS:
##
##

#####################################
exit_ticket = "y"
#####################################

def get_file(prompt, process_type):
    """This gets a file with a set prompt and processing type for the file."""
    while True:
        try:
            file = open(str(input(prompt)), process_type)
            return file
        except FileNotFoundError:
            print("WARNING. Inputted file not found. Please try again.")
#######################################################Main Loop#################################################
while exit_ticket == "y" or exit_ticket == "yes":
    file_to_read = get_file("Please enter the name of the file you want to pull meteorite data from.", "r")
    file_to_write = get_file("Please enter the name of the file you would like to output data to.", "w")



