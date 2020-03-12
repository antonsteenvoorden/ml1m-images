import os
import pandas as pd
import urllib.request

FOLDER = "images"
INPUT_FILE = "movie_images.csv"


def download_image(df):
    new_id, item_id, image = df
    image_path = f"{FOLDER}/{item_id}.jpg"

    if image == "" or image is None or not isinstance(image, str):
        print("Failed: id", new_id, image)
        return

    if os.path.exists(image_path):
        return

    try:
        urllib.request.urlretrieve(image, image_path)
    except Exception:
        print("ERROR: id", new_id, image)


if __name__ == '__main__':
    os.makedirs(FOLDER, exist_ok=True)
    df = pd.read_csv(INPUT_FILE)
    df[['new_id', 'item_id', 'image']].apply(lambda x: download_image(x), axis=1)
