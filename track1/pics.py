# Organize pictures by year/month according to the filename
import os
import shutil


def organize_pics(folder):
    for pic in os.listdir(folder):
        if pic.endswith('.png'):
            pic_path = os.path.join(folder, pic)
            pic_year = pic[:4]
            pic_month = pic[4:6]
            pic_new_folder = os.path.join(folder, pic_year, pic_month)
            if not os.path.exists(pic_new_folder):
                os.makedirs(pic_new_folder)
            shutil.copy(pic_path, os.path.join(pic_new_folder, pic))


if __name__ == "__main__":
    organize_pics('pictures')
