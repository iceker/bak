from PIL import Image
from pylab import *


im = Image.open('captcha.gif')

#im.thumbnail((200,44))
im = im.resize((200,44),Image.ANTIALIAS)
imshow(im)
print('Please input points')
x = ginput(7)


for i in range(len(x)):
    x[i] = list(x[i])
    for j in range(2):
        x[i][j] = int(x[i][j]*10000)/10000

print(x)


