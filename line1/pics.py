# Organize pictures by year/month according to the filename
import os
import shutil


def organize_pics(folder):
    for filename in os.listdir(folder):
        # Get information from the filename
        path = os.path.join(folder, filename)
        year = filename[:4]
        month = filename[4:6]
        new_folder = os.path.join(folder, year, month)

        # Create the folder if it doesn't exist
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)

        # Copy the file to the new folder (keeps the original)
        shutil.copy(path, os.path.join(new_folder, filename))

        # Move the file to the new folder (deletes the original)
        # shutil.move(pic_path, os.path.join(pic_new_folder, pic_name))


if __name__ == "__main__":
    organize_pics('pictures')
