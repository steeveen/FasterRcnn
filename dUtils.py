# -*- coding: utf-8 -*-
'''
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
 @Author = 'steven'   @DateTime = '2019/7/4 16:27'
'''
from matplotlib import pyplot as plt
from matplotlib import patches as pts
import numpy as np
def showPatches(a,bg = np.zeros((128, 128))):

    plt.imshow(bg, 'gray')
    axs = plt.gca()
    for i in range(a.shape[0]):
        _a=a[i,:]
        if i%9<3:
            ec='#ff0000'
        elif i%9<6:
            ec='#00ff00'
        else:
            ec='#0000ff'
        w=_a[3]-_a[1]
        h=_a[2]-_a[0]
        axs.add_patch(pts.Rectangle((_a[1],_a[0]),w,h,edgecolor=ec,facecolor=None,fill=False))
    plt.show()
if __name__ == '__main__':
    showPatches([(64-25,64-25,64+25,64+25)])