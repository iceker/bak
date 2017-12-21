from PIL import Image
try:
    im = Image.open('test.jpg')
    im.show()
    im.close()
except:
    pass
