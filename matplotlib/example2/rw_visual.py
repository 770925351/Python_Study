import matplotlib.pyplot as plt
from radom_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
''' figure设置图表的宽度,高度,分辨率和背景色,设置宽高度需要传入一个元组,单位为英寸 '''
plt.figure(dpi=128,figsize=(10,6))
plt.scatter(rw.x_values,rw.y_values,c=rw.y_values,cmap=plt.cm.Blues,edgecolors='none',s=5)   
plt.scatter(0,0,c='green',edgecolors='none',s=100)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c='green',edgecolors='none',s=100)
''' 隐藏x轴,隐藏y轴 '''
plt.axes().get_xaxis().set_visible(False) 
plt.axes().get_yaxis().set_visible(False)
plt.show()