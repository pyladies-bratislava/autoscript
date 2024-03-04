import os
import shutil


# Organize pictures by year/month according to the filename
def organize_pics(folder):

    print(f"Organizing photos in {folder} folder...")

    # For each file in the folder
    for filename in os.listdir(folder):

        # Step 1 - Get information from the filename
        print(f"Processing {filename}")
        filepath = os.path.join(folder, filename)
        year = filename[0:4]  # String slicing by index 0 1 2 3
        month = filename[4:6]  # String slicing by index 4 5
        print(f"Path: {filepath} Year: {year}, Month: {month}")

        # Step 2 - Define folder's name, e.g. 2023/05
        new_folder = os.path.join("organized", year, month)
        print(f"New folder: {new_folder}")

        # Step 3 - Create a folder if it doesn't exist
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
            print(f"Created new folder: {new_folder}")

        # Step 4 - Copy the file to the appropriate folder (keeps the original)
        new_filepath = os.path.join(new_folder, filename)
        shutil.copy(filepath, new_filepath)
        print(f"File {filename} copied to {new_folder}")

    print(f"Organizing pictures in {folder} completed.")


organize_pics("photos")
