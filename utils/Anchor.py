# -*- coding: utf-8 -*-
'''anchor生成类
        司马懿：“善败能忍，然厚积薄发”
                                    ——李叔说的
code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
          --┃      ☃      ┃--
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗II━II┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
 @Belong = 'FasterRcnn'  @MadeBy = 'PyCharm'
 @Author = 'steven'   @DateTime = '2019/7/4 16:02'
'''
import numpy as np
from dUtils import showPatches


def _genePoints(cx, cy, w, h):
    return (np.round(cx - w / 2))


def _geneOneScale(squareLength, ratio=[0.5, 1.2]):
    a = []
    for i in ratio:
        w = squareLength * np.square(i)
        h = squareLength / np.square(i)
        a.append((-h / 2, -w / 2, h / 2, w / 2))
    a=np.array(a)
    print(a.shape)
    return a


def getAnchor(baseLength, scale=[0.5, 1, 2], ratio=[0.5, 1, 2]):
    a = np.concatenate([_geneOneScale(baseLength * i, ratio) for i in scale])
    for _a in a:
        print(_a)
    print('*'*16)
    a=a+[baseLength/2,baseLength/2,baseLength/2,baseLength/2]
    for _a in a:
        print(_a)
    return a


if __name__ == '__main__':
    from skimage import io as skio
    from skimage.transform import resize
    acs = getAnchor(8)
    img= resize( skio.imread(r'C:\Users\lenovo\Desktop\桌面\image\net.png'),(128,128),preserve_range=True)
    showPatches(acs,img)
