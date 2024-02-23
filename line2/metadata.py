import json
import os

from PIL import Image
from PIL.PngImagePlugin import PngInfo


def converto_to_png():
    for filename in os.listdir("pictures"):
        if filename.endswith(".jpg"):
            img = Image.open(f"pictures/{filename}")
            img.save(f"pictures/{filename[:-4]}.png")


def save_metadata_to_image():
    # Define folder's name, e.g. 2023/05
    new_folder = os.path.join("pictures", "new")
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    for filename in os.listdir("pictures"):
        try:
            img = Image.open(f"pictures/{filename}")
            with open("metadata/metadata.json", 'r') as f:
                metadata = json.load(f)
            for image_name, image_data in metadata.items():
                if image_name == filename[:-4]:
                    metadata = PngInfo()
                    for key, value in image_data.items():
                        metadata.add_text(key, str(value))
                    img.save(f"{new_folder}/{filename}", pnginfo=metadata)

                    targetImage = Image.open(f"{new_folder}/{filename}")

                    print(targetImage.text)

        except IsADirectoryError:
            ...


if __name__ == "__main__":
    #converto_to_png()
    save_metadata_to_image()
