''' 绘制简单的折线图 '''

import matplotlib.pyplot as plt
input_squares = [1,2,3,4,5,6]
squares = [1,4,9,16,25,36] 
''' 默认情况下,你只是传入y值的组,plot()方法默认绘制会让第一个点的x值为0
    所以当你的数据不是从0开始的话,需要传入x值的组
'''
plt.plot(input_squares,squares,linewidth=5) # 设置折线的粗细
plt.title("Square Numbers",fontsize=24) # 设置图像的标题
plt.xlabel("Value",fontsize=14) # 设置x轴的标签 
plt.ylabel("Square of Value",fontsize=14) # 设置y轴的标签
plt.tick_params(axis='both',labelsize=14) #设置刻度标记的大小
plt.show() #显示折线图