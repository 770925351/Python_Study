''' 绘制散点图 '''
import matplotlib.pyplot as plt

input_squares = list(range(1001))
squares = [x**2 for x in input_squares]

''' 显示点,需要传入一对x,y坐标值 '''
plt.scatter(input_squares,squares,s=10,edgecolors='none',c='red') 
# s参数代表点的大小,edgecolors='none'代表弄掉点的轮廓,c代表点的颜色
# 设置颜色映射,用法: 将数据集传给c,然后增加cmap参数,设置整个数据集怎么变
# plt.cm.Blues 代表值小的点颜色浅,值大的点颜色深

''' 要了解pyplot中所有的颜色映射,访问:http://matplotlib.org/,单机Examples,向下滚动到
    Color Examples,再点击colormaps_reference 
'''
plt.scatter(input_squares,squares,s=10,edgecolors='none',c=squares,cmap=plt.cm.Blues)
''' 设置图参数 '''
plt.title("Square Numbers",fontsize=24) # 设置图像的标题
plt.xlabel("Value",fontsize=14) # 设置x轴的标签 
plt.ylabel("Square of Value",fontsize=14) # 设置y轴的标签

''' 设置刻度标记的大小 '''
plt.tick_params(axis='both',which='major',labelsize=14)
''' 显示散点图 '''
plt.show()

''' 保存图表 '''
#plt.savefig('1.png',bbox_inches='tight')
''' 第一个参数是以什么名字保存,第二个参数是省去空白部分 '''