import os

for directory in os.listdir():

    if  directory == "README.md" or directory == "temp.py":
        continue

    # get all file names in the directory
    files = os.listdir(directory)

    # loop through each file and rename it
    for i, filename in enumerate(files):
        # generate new filename by adding number before original filename
       
        new_filename = filename.replace(".java",".txt")
        # join directory path with original filename
        old_path = os.path.join(directory, filename)
        # join directory path with new filename
        new_path = os.path.join(directory, new_filename)
        # rename file
        os.rename(old_path, new_path)   

