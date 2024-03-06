import os
import json
import shutil


def organize_images_by_date(json_file_path, images_dir):
    # Load metadata from JSON file
    with open(json_file_path, "r") as f:
        metadata = json.load(f)

    # Create a directory to store the organized images
    output_dir = "organized_images"
    os.makedirs(output_dir, exist_ok=True)

    # Iterate over each image entry in the metadata
    for image_name, image_data in metadata.items():
        acquisition_date = image_data.get("Acquisition date")
        if acquisition_date:
            # Create directory based on acquisition date if it doesn't exist
            date_folder = os.path.join(output_dir, acquisition_date)
            os.makedirs(date_folder, exist_ok=True)

            # Copy image to the corresponding folder
            image_path = os.path.join(images_dir, f"{image_name}.jpg")
            if os.path.exists(image_path):
                shutil.copy(image_path, date_folder)
            else:
                print(f"Image file '{image_name}.jpg' not found in '{images_dir}'")


metadata_json_file = "metadata/metadata.json"
images_directory = "/pictures"
organize_images_by_date(metadata_json_file, images_directory)
