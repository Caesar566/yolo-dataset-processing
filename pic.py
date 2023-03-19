# -*- coding: UTF-8 -*-
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

#对图像读取，进行旋转和翻转处理
imageNum = xmlNumALL = ['pic/' + str(i) + '.jpg' for i in range(1, 501)]
print(len(imageNum))

for i in range(len(imageNum)):
    im = Image.open(''+imageNum[i])
    im_rotate_90 = im.rotate(90)
    im_rotate_180 = im.rotate(180)
    im_rotate_transpose_LEFT_RIGHT= im.transpose(Image.FLIP_LEFT_RIGHT)
    im_rotate_transpose_TOP_BOTTOM = im.transpose(Image.FLIP_TOP_BOTTOM)
    if i <10:
        im_rotate_90.save('90/'+i.__str__()+'.jpg')
        im_rotate_180.save('180/' + i.__str__() + '.jpg')

        im_rotate_transpose_LEFT_RIGHT.save('360/' + i.__str__() + '.jpg')

    elif i>=10 and i<100:
        im_rotate_90.save('90/' + i.__str__() + '.jpg')
        im_rotate_180.save('180/' + i.__str__() + '.jpg')

        im_rotate_transpose_LEFT_RIGHT.save('360/' + i.__str__() + '.jpg')

    elif i>=100 and i<1000:
        im_rotate_90.save('90/' + i.__str__() + '.jpg')
        im_rotate_180.save('180/' + i.__str__() + '.jpg')

        im_rotate_transpose_LEFT_RIGHT.save('360/' + i.__str__() + '.jpg')





#对图像进行读取重新编号，放在同一个文件夹中
imageNum1 = ['pic/' + str(i) + '.jpg' for i in range(1,501)]
imageNum3 = ['90/' + str(i) + '.jpg' for i in range(500)]
imageNum4 = ['180/' + str(i) + '.jpg' for i in range(500)]
imageNum5 = ['360/' + str(i) + '.jpg' for i in range(500)]

print(len(imageNum1))

imageNumALL = imageNum1+imageNum3+imageNum4+imageNum5
print(len(imageNumALL))
print(imageNumALL)
for i in range(len(imageNumALL)):
    im = Image.open(''+imageNumALL[i])
    if i < 10:
        im.save('111/0000' + i.__str__() + '.jpg')
    elif i>=10 and i<100:
        im.save('111/000' + i.__str__() + '.jpg')
    elif i>=100 and i<1000:
        im.save('111/00' + i.__str__() + '.jpg')
    elif i >= 1000 and i < 10000:
        im.save('111/0' + i.__str__() + '.jpg')

