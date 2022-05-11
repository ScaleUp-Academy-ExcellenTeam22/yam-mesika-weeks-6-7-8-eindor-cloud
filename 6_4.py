from PIL import Image
import numpy

def decript(path):
    im = Image.open(r"C:\Users\amit\Desktop\code.png")
    image = im.load()
    cols, rows = im.size
    word = ""
    for x in range(cols):
        for y in range(rows):
            if image[x, y] != 255:
                word += chr(y)
    return word


print(decript(r"C:\Users\amit\Desktop\code.png"))