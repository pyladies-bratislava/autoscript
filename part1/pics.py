# Organize pictures by year/month according to the filename
import os
import shutil


def organize_pics(folder):

    print(f"Organizing pictures in {folder}...")

    for filename in os.listdir(folder):
        # Print the filename
        print(f"Processing {filename}")

        # Get information from the filename
        path = os.path.join(folder, filename)
        year = filename[:4]  # String slicing by index
        month = filename[4:6]
        print(f"Path: {path}: Year: {year}, Month: {month}")

        # Define folder's name, e.g. 2023/05
        new_folder = os.path.join("organized", year, month)
        print(f"New folder: {new_folder}")

        # Create the folder if it doesn't exist
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        # Copy the file to the new folder (keeps the original)
        shutil.copy(path, os.path.join(new_folder, filename))
        print(f"File {filename} copied to {new_folder}")

        # Move the file to the new folder (deletes the original)
        # shutil.move(pic_path, os.path.join(pic_new_folder, pic_name))

    print(f"Organizing pictures in {folder} completed.")


# Entry point of the script/program
if __name__ == "__main__":
    organize_pics("pictures")
