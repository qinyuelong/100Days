'''
https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/15.%E5%9B%BE%E5%83%8F%E5%92%8C%E5%8A%9E%E5%85%AC%E6%96%87%E6%A1%A3%E5%A4%84%E7%90%86.md
'''


from PIL import Image, ImageFilter



def image_demo():
    image = Image.open('../res/guido.jpg')
    rect = 80, 20, 310, 360
    image.show()
    image.crop(rect).show()

    size = 128, 128
    # image.thumbnail(size)
    # image.show()

    image.transpose(Image.FLIP_LEFT_RIGHT).show()

    image.filter(ImageFilter.CONTOUR).show()


if __name__ == '__main__':
    image_demo()