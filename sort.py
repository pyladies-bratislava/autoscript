import os
import shutil


def sort_photos(folder):
    # Sort photos by year/month according to the filename
    print(f"Sorting photos in {folder} ...\n------")

    # For each file in the folder
    for filename in os.listdir(folder):

        # Step 0 - Print the filename
        print(f"Processing {filename}")

        # Step 1 - Get information from the filename
        filepath = os.path.join(folder, filename)
        year = filename[0:4]  # String slicing by index 0 1 2 3
        month = filename[4:6]  # String slicing by index 4 5
        print(f"Path: {filepath} Year: {year}, Month: {month}")

        # Step 2 - Define folder's name, e.g. 2023/05
        new_folder = os.path.join("sorted", year, month)
        print(f"New folder: {new_folder}")

        # Step 3 - Create a folder if it doesn't exist
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
            print(f"Created new folder: {new_folder}")

        # Step 4 - Copy the file to the appropriate folder
        new_filepath = os.path.join(new_folder, filename)
        shutil.copy(filepath, new_filepath)
        print(f"File {filename} copied to {new_folder}")

        print("------")

    print(f"Sorting pictures in {folder} completed.")
