import os

from PIL import Image
import pandas as pd

from src.insert_text_2_image import insert_text_2_image


def main(imgpath, csvpath, fontpath, text_col=1, filename_col=0, output_dir="local/output/"):
    img = Image.open(imgpath)
    fontpath = "font/Shippori_Mincho_B1/ShipporiMinchoB1-Bold.ttf"
    df = pd.read_csv(csvpath)

    os.makedirs(output_dir, exist_ok=True)
    for i in range(len(df)):
        text = df.iat[i, text_col]
        filename = df.iat[i, filename_col]
        output_img = insert_text_2_image(img, text, 72, fontpath)
        output_img.save(os.path.join(output_dir, f"{filename}.png"))


if __name__ == "__main__":
    fontpath = "font/Shippori_Mincho_B1/ShipporiMinchoB1-Bold.ttf"
    main("input.jpg", "input.csv", fontpath)
