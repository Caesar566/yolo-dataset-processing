from bs4 import BeautifulSoup

path = '/home/caesar/'#xml文件中的对应图像路径

def left(xmin, xmax, ymin, ymax):
    xmin, ymin = ymin, xmin   #向左90
    xmax, ymax = ymax, xmax
    xmin = int(xmin) + 80
    xmax = int(xmax) + 80
    ymin = 480 - (int(ymin) - 80)
    ymax = 480 - (int(ymax) - 80)
    return str(xmin), str(xmax), str(ymin), str(ymax)

def right(xmin, xmax, ymin, ymax):
    xmin = 640 - int(xmin)      #180
    xmax = 640 - int(xmax)
    ymin = 480 - (int(ymin))
    ymax = 480 - (int(ymax))
    return str(xmin), str(xmax), str(ymin), str(ymax)

def mir(xmin, xmax, ymin, ymax):
    xmin = 640 - int(xmin)      #镜像
    xmax = 640 - int(xmax)
    return str(xmin), str(xmax), str(ymin), str(ymax)

def run(filename):
    with open('voc/' + xmlNumALL[i], 'r') as file:
        file_str = file.read()
    bs = BeautifulSoup(file_str, 'lxml')
    bs.filename.string = filename
    bs.path.string = path
    for object in bs.find_all('object'):
        obbs = BeautifulSoup(str(object), 'lxml')
        if way == 0:
            object.xmin.string, object.xmax.string, object.ymin.string, object.ymax.string = obbs.xmin.string, obbs.xmax.string, obbs.ymin.string, obbs.ymax.string
        elif way == 1:
            object.xmin.string, object.xmax.string, object.ymin.string, object.ymax.string = left(obbs.xmin.string, obbs.xmax.string, obbs.ymin.string, obbs.ymax.string)
        elif way == 2:
            object.xmin.string, object.xmax.string, object.ymin.string, object.ymax.string = right(obbs.xmin.string, obbs.xmax.string, obbs.ymin.string, obbs.ymax.string)
        elif way == 3:
            object.xmin.string, object.xmax.string, object.ymin.string, object.ymax.string = mir(obbs.xmin.string, obbs.xmax.string, obbs.ymin.string, obbs.ymax.string)
    bs = str(bs).replace('<html><body>', '')
    bs = str(bs).replace('</body></html>', '')
    return bs

way = 0
xmlNumALL = [str(i) + '.xml' for i in range(1, 501)]
print(len(xmlNumALL))

start_num = 0

for i in range(4 * len(xmlNumALL)):
    a = i + start_num
    if way == 1:
        i -= 500
    elif way == 2:
        i -= 1000
    elif way == 3:
        i -= 1500
    if a < 10:
        file = open('label/0000' + a.__str__() + '.xml','w')
        bs = run('0000' + a.__str__() + '.jpg')
    elif a>=10 and a<100:
        file = open('label/000' + a.__str__() + '.xml','w')
        bs = run('000' + a.__str__() + '.jpg')
    elif a>=100 and a<1000:
        file = open('label/00' + a.__str__() + '.xml','w')
        bs = run('00' + a.__str__() + '.jpg')
    elif a >= 1000 and a < 10000:
        file = open('label/0' + a.__str__() + '.xml','w')
        bs = run('0' + a.__str__() + '.jpg')
    file.write(bs)
    file.close()
    
    if a == 499 + start_num:#此处设置为500张为一组
        way = 1
    elif a == 999 + start_num:
        way = 2
    elif a == 1499 + start_num:
        way = 3    