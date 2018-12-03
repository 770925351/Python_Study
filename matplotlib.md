# matplotlib学习

## 1.配置环境

> - 安装matplotlib
>
>   - Linux
>
>   > ```sh
>   > sudo apt-get install python3-matplotlib
>   > ```
>
>   - Windows
>
>   > 1.[下载whl文件](https://files.pythonhosted.org/packages/c6/a6/75a4ccad919388fc3ef578d8e5ccadd12dbf6257cb79f12b11508f074b49/matplotlib-3.0.2-cp35-cp35m-win32.whl)
>   >
>   > 2.去Windows自带终端运行
>   >
>   > ```sh
>   > python -m pip install --user matplotlib-3.0.2-cp35-cp35m-win32.whl
>   > ```
>
> - 安装pygal
>
>   - Linux
>
>   > ```Python
>   > pip install --user pygal
>   > ```
>
>   - Windows
>
>   > ```sh
>   > python -m pip install --user pygal
>   > ```

## 2.绘制折线图

> ```Python
> ''' 绘制简单的折线图 '''
> import matplotlib.pyplot as plt
> input_squares = [1,2,3,4,5,6]
> squares = [1,4,9,16,25,36] 
> ''' 默认情况下,你只是传入y值的组,plot()方法默认绘制会让第一个点的x值为0
>     所以当你的数据不是从0开始的话,需要传入x值的组
> '''
> plt.plot(input_squares,squares,linewidth=5) # 设置折线的粗细
> plt.title("Square Numbers",fontsize=24) # 设置图像的标题
> plt.xlabel("Value",fontsize=14) # 设置x轴的标签 
> plt.ylabel("Square of Value",fontsize=14) # 设置y轴的标签
> plt.tick_params(axis='both',labelsize=14) #设置刻度标记的大小
> plt.show() #显示折线图
> ```

## 3.绘制散点图

> ```Python
> ''' 绘制散点图 '''
> import matplotlib.pyplot as plt
> 
> input_squares = list(range(1001))
> squares = [x**2 for x in input_squares]
> 
> ''' 显示点,需要传入一对x,y坐标值 '''
> plt.scatter(input_squares,squares,s=10,edgecolors='none',c='red') 
> # s参数代表点的大小,edgecolors='none'代表弄掉点的轮廓,c代表点的颜色
> # 设置颜色映射,用法: 将数据集传给c,然后增加cmap参数,设置整个数据集怎么变
> # plt.cm.Blues 代表值小的点颜色浅,值大的点颜色深
> 
> ''' 要了解pyplot中所有的颜色映射,访问:http://matplotlib.org/,单机Examples,向下滚动到
>     Color Examples,再点击colormaps_reference 
> '''
> plt.scatter(input_squares,squares,s=10,edgecolors='none',c=squares,cmap=plt.cm.Blues)
> ''' 设置图参数 '''
> plt.title("Square Numbers",fontsize=24) # 设置图像的标题
> plt.xlabel("Value",fontsize=14) # 设置x轴的标签 
> plt.ylabel("Square of Value",fontsize=14) # 设置y轴的标签
> 
> ''' 设置刻度标记的大小 '''
> plt.tick_params(axis='both',which='major',labelsize=14)
> ''' 显示散点图 '''
> plt.show()
> 
> ''' 保存图表 '''
> #plt.savefig('1.png',bbox_inches='tight')
> ''' 第一个参数是以什么名字保存,第二个参数是省去空白部分 '''
> ```

## 练习小项目(模拟随机漫步)

> 利用Python随机数生成,模拟出5000个坐标,并把这些坐标在散点图中表示出来

- `radom_walk.py`

> ```Python
> ''' 模拟随机漫步 '''
> 
> from random import choice
> 
> class RandomWalk():
>     ''' 一个生成随机漫步数据的类 '''
>     def __init__(self,num_points=5000):
>         ''' 初始化自己的点属性 '''
>         self.num_points = num_points
>         ''' 使得x,y坐标都从0开始 '''
>         self.x_values = [0]
>         self.y_values = [0]
> 
>     def fill_walk(self):
>         ''' 计算随机漫步的点 '''
>         while len(self.x_values) < self.num_points :
>             x_direction = choice([1,-1]) # 随机选择前进方向    
>             x_distance = choice([0,1,2,3,4,5]) # 随机选择前进距离
>             x_step = x_direction * x_distance # 计算前进距离
> 
>             y_direction = choice([1,-1]) # 随机选择前进方向    
>             y_distance = choice([0,1,2,3,4,5]) # 随机选择前进距离
>             y_step = y_direction * y_distance # 计算前进距离
> 
>             ''' 拒绝原地踏步 '''
>             if x_step ==0 and y_step ==0 :
>                 continue
> 
>             ''' 计算点的坐标 '''
>             next_x = self.x_values[-1] + x_step # -1是表示列表最后的一个点
>             next_y = self.y_values[-1] + y_step
> 
>             ''' 将计算出来的点加入列表中 '''
>             self.x_values.append(next_x)
>             self.y_values.append(next_y)
>  
> ```

- `rw_visual.py`

> ```Python
> import matplotlib.pyplot as plt
> from radom_walk import RandomWalk
> 
> rw = RandomWalk()
> rw.fill_walk()
> ''' figure设置图表的宽度,高度,分辨率和背景色,设置宽高度需要传入一个元组,单位为英寸 '''
> plt.figure(dpi=128,figsize=(10,6))
> plt.scatter(rw.x_values,rw.y_values,c=rw.y_values,cmap=plt.cm.Blues,edgecolors='none',s=5)   
> plt.scatter(0,0,c='green',edgecolors='none',s=100)
> plt.scatter(rw.x_values[-1],rw.y_values[-1],c='green',edgecolors='none',s=100)
> ''' 隐藏x轴,隐藏y轴 '''
> plt.axes().get_xaxis().set_visible(False) 
> plt.axes().get_yaxis().set_visible(False)
> plt.show()
> ```

## 4.用Pygal绘制直方图

> 模拟掷骰子,统计每个数字出现的个数,并把这些情况用直方图表示出来

- `die.py`

> ```Python
> 
> from random import randint
> 
> class Die():
>     ''' 创建一个表示骰子的类 '''
>     def __init__(self,num_sides=6):
>         self.num_sides = num_sides # 默认骰子有六面
>     
>     def roll(self):
>         return randint(1,self.num_sides) # 模拟掷骰子,返回点数
> ```

- `die_visual.py`

> ```Python
> ''' 使用Pygal去创建图表,要了解Pypal可以创建什么样的图表,访问http://www.pypal.org
>     单击Documentation,再单击Chart types,会有示例
> '''
> 
> from die import Die
> import pygal
> 
> die = Die()
> results = []
> 
> for roll_num in range(1000):
>     result = die.roll()
>     results.append(result)
> 
> frequencies = []
> for value in range(1,die.num_sides+1):
>     frequency = results.count(value)
>     frequencies.append(frequency)
> 
> hist = pygal.Bar() # Bar是直方图类型
> hist.title = "Results of rolling D6 1000 times" #设置直方图题目
> hist.x_title = "Result" # 设置直方图x轴标题
> hist.y_title = "Frequency of Result" # 设置直方图y轴标题
> hist.add('D6',frequencies) # 将标签和数据传入
> hist.render_to_file('die_visual.svg') # 将直方图进行渲染成svg格式
> ```