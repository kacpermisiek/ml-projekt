import os
import shutil

import pandas as pd
from PIL import Image


def prepare_train():
    train_base_path = os.path.join(os.getcwd(), 'Data_images', 'Train')
    dest_base_path = os.path.join(os.getcwd(), 'Data_images', 'Train_new')
    class_dirs = sorted(os.listdir(train_base_path), key=lambda x: int(x))
    data = []
    for class_dir in class_dirs:
        print("Progress: ", int(class_dir) / len(class_dirs) * 100, "%")
        class_path = os.path.join(train_base_path, class_dir)

        image_names = os.listdir(class_path)

        for image in image_names:
            img = Image.open(os.path.join(class_path, image))
            if img.mode != 'RGB':
                img = img.convert('RGB')

            width, height = img.size
            extent = (0, 0, width, height)

            img.transform((128, 128), method=1, data=extent)
            img.save(os.path.join(dest_base_path, image.split(".")[0] + '.png'))

            data.append([class_dir, image.split(".")[0] + '.png'])

        df = pd.DataFrame(data, columns=['class', 'image'])
        df.to_csv('Train_data.csv', index=False)


def remove_from_new_train():
    shutil.rmtree(os.path.join(os.getcwd(), 'Data_images', 'Train_new'))


if __name__ == '__main__':
    prepare_train()
    # remove_from_new_train()
