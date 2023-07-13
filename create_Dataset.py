# TO DELETE EXTRA TAGS

# with open("LabelResultAll.txt", "r") as file:
#     lines = file.readlines()

# with open("LabelResultAll1.txt", "w") as output_file:
#     for line in lines:
#         words = line.split()
#         new_line = " ".join(words[:1]) + "\n"
#         output_file.write(new_line)

# REMOVE TEXT TAGS FROM FILE

# import fileinput
# import re

# # define the regular expression pattern to match
# pattern = r"\b\w+,\s*"

# # iterate over the lines of the file and remove the matched pattern
# for line in fileinput.input("LabelResultAll.txt", inplace=True):
#     new_line = re.sub(pattern, "", line)
#     print(new_line, end="")


# TO MOVE IMAGES TO THEIR DIRECTORIES

# import os

# # define the path to the directory containing the images
# image_dir = "/Users/sarvesh/Desktop/Twitter_Dataset/data"

# # define the path to the text file containing the image IDs and classes
# text_file = "LabelResultAll.txt"

# # create a dictionary to map classes to directories
# class_to_dir = {
#     "positive": "/Users/sarvesh/Desktop/Twitter_Dataset/positive",
#     "negative": "/Users/sarvesh/Desktop/Twitter_Dataset/negative",
#     "neutral": "/Users/sarvesh/Desktop/Twitter_Dataset/neutral"
#     # add more classes and directories as needed
# }

# # iterate over the lines of the text file
# with open(text_file, "r") as f:
#     for line in f:
#         # parse the image ID and class from the line
#         image_id, image_class = line.strip().split(' ')

#         # define the source and destination paths
#         source_path = os.path.join(image_dir, image_id)

#         if image_class not in class_to_dir:
#             print(f"Invalid class: {image_class}")
#             continue

#         dest_path = os.path.join(class_to_dir[image_class], image_id)

#         # create the destination directory if it doesn't exist
#         os.makedirs(os.path.dirname(dest_path), exist_ok=True)
#         source_path=source_path+".jpg"
#         dest_path=dest_path+".jpg"
#         print(f"Moving file {source_path} to {dest_path}")
#         # move the image to the destination directory
#         os.rename(source_path, dest_path)


