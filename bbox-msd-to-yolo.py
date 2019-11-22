import pandas as pd
from pillow import Image

train_csv_path = "./msd-train/__DressType_msd_train-prod.csv"

train_csv = pd.read_csv(train_csv_path)

urls = train_csv["image_urls"] # list of all the image urls in the training CSV
alt_urls = train_csv[""

for img_path in image_paths:
    with Image.open(img_path) as img:
        width, height = img.size
    