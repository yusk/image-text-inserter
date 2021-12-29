from PIL import Image, ImageDraw, ImageFont


def insert_text_2_image(img, text, fontsize, fontpath, fontcolor=(0, 0, 0)) -> Image:
    img = img.copy()
    w, h = img.size
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(fontpath, fontsize)
    tw, th = d.textsize(text=text, font=font)
    d.text(
        xy=((w-tw)/2, (h-th)/2),
        text=text,
        font=font, fill=fontcolor)
    return img
