### HOW THE FCK AM I SUPPOSED TO SLICE IMAGES IN A DIRECTORY VERTICALLY
##

import os
import glob

inputted_directory = input("What is the name of the directory you would like to pull images from?")
whole_path = os.path.join(os.getcwd(), inputted_directory)

while not os.path.isdir(whole_path):
    inputted_directory = input("That is not a valid directory. Enter it again.")
    whole_path = os.path.join(os.getcwd(), inputted_directory)

valid_files = False
while not valid_files:
    images = []

    for file_name in glob.glob(os.path.join(whole_path, '*.ppm')):
        raw_data = open(file_name).readlines()
        images.append([i.strip('\n') for i in raw_data])
    print(images)

    current_size = images[0][1]

    for image in images:
        if image[0] != "P3":
            print("An image had an invalid header")
        elif image[1] != current_size:
            print("An image had an invalid size: ({}) instead of ({})".format(image[1], current_size))
        elif image[2] != "255":
            print("An image had an invalid color depth")
        else:
            del image[0:3]
            valid_files = True

#This is when I start to have literally no idea what I'm doing :-)

print(len(images[0]))
print(len(images))
slice_point = int(len(images[0]) / len(images))

##ughhhhhHHhhhHHHHhhhHhH Idon't know how to do this
