# -*- coding: utf-8 -*-
'''anchor生成类
行索引为Y，列索引为X，所以矩阵第一维为Y
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
import itertools

def _genePoints(cx, cy, w, h):
    return (np.round(cx - w / 2))


def _geneOneScale(squareLength, ratio=[0.5, 1,2]):
    a = []
    for i in ratio:
        w = squareLength / np.sqrt(i)
        h = squareLength * np.sqrt(i)
        a.append((-h / 2, -w / 2, h / 2, w / 2))
    a=np.array(a)
    print(a.shape)
    return a


def getOneAnchor(baseLength, scale=[0.5, 1, 2], ratio=[0.5, 1, 2]):
    a = np.concatenate([_geneOneScale(baseLength * i, ratio) for i in scale])
    a=a+[baseLength/2,baseLength/2,baseLength/2,baseLength/2]
    return a
def getAnchors(baseLength,imgShape):
    y=list(range(0,imgShape[0], baseLength))
    x=list(range(0,imgShape[1],baseLength))
    shifty,shiftx= map( lambda x:x.flatten(),np.meshgrid(y,x))
    print(shifty.shape)
    print(shiftx.shape)
    shifts=np.stack([shifty,shiftx,shifty,shiftx],axis=1)
    print(shifts)
    baseAnchors=getOneAnchor(baseLength)
    allAcs=[(_shift+_anchor) for _shift,_anchor in itertools.product(shifts,baseAnchors) ]

    return np.array(allAcs)


if __name__ == '__main__':
    from skimage import io as skio
    from skimage.transform import resize

    img= resize( skio.imread(r'..\res\test.tif'),(64,64),preserve_range=True)
    # acs = getOneAnchor(8)
    acs = getAnchors(8,img.shape[0:2])

    showPatches(acs,img)

