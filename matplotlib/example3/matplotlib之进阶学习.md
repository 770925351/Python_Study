# matplotlib之进阶学习(解析csv文件并根据数据画出图像)

> 本次学习目的:学习如何解析csv文件,并将解析的数据以图像表示出来
>
> 本次用到的模块 `csv` `matplotlib.plot` `datetime`

## 1.导入模块

> ```Python
> import csv
> import matplotlib.pyplot as plt
> from datetime import datetime 
> ```

## 2.datetime简介

> 本次使用的是`datetime`中的`strptime()`方法
>
> 使用方式:`strptime("时间字符串","格式化形式")`
> |实参|含义|
> |-------|------|
> |%A|星期的名称|
> |%B|月份名|
> |%m|用数字表示月份(01-12)|
> |%d|用数字表示月份的一天(01-31)|
> |%Y|四位年份(2018)|
> |%y|两位年份(18)|
> |%H|24小时制的小时数(00-23)|
> |%I|12小时制的小时数(01-12)|
> |%p|am或者pm|
> |%M|分钟数(00-59)|
> |%S|秒数(00-61)|
>

## 3.Demo1(解析一个月的最高温度情况)

> `highs_lows.py`
>
> ```Python
> ''' 导入相关模块 '''
> import csv
> import matplotlib.pyplot as plt
> from datetime import datetime
> 
> ''' 初始化文件名称 '''
> filename = 'sitka_weather_07-2014.csv'
> 
> ''' 获取时间、最高气温 '''
> highs = []
> datatimes = []
> with open(filename) as file:
>     reader = csv.reader(file) # 将文件传递给reader函数,获得一个与之相关的阅读器对象
>     head_row = next(reader)
>     for row in reader :  # 从第二行开始,遍历阅读器的每一行
>         highs.append(int(row[1])) # 获得每一行索引为1的值
>         datatimes.append(datetime.strptime(row[0],"%Y-%m-%d")) #格式化获得的日期
> 
> ''' 画图 '''
> fig = plt.figure(dpi=128,figsize=(10,6)) #获取背景对象
> plt.plot(datatimes,highs,c='red') #设置折线属性
> plt.title("Daily high temperatures,July 2014",fontsize=24) #设置折线标题和字体大小
> plt.xlabel("",fontsize=16) #设置x轴标签及字体大小
> fig.autofmt_xdate() # 绘制斜的date标签,防止标签过长重叠不好看
> plt.ylabel("Temperature (F)",fontsize=16) #设置y轴标签及字体大小
> plt.tick_params(axis='both',which='major',labelsize=16) #设置刻度 
> plt.show() #显示图标
> ```

## 4.Demo2(解析一年的最高最低温度情况)

> `highs_lows_year,py`
>
> ```Python
> ''' 导入相关模块 '''
> import csv
> import matplotlib.pyplot as plt
> from datetime import datetime
> 
> ''' 初始化文件名称 '''
> filename = 'death_valley_2014.csv'
> 
> ''' 解析csv文件,获得最高最低气温信息及时间 ''' 
> dates = []
> highs = []
> lows = []
> with open(filename) as file :
>     reader = csv.reader(file)
>     head_row = next(reader)
>     ''' 在这里用了一个 try-expect-else 模块,防止数据为空,程序报错 '''
>     for row in reader :
>         try:
>             high = int(row[1])
>             low = int(row[3])
>         except ValueError :
>             print(datetime.strptime(row[0],"%Y-%m-%d"),"Empty Data!")
>         else:
>             dates.append(datetime.strptime(row[0],"%Y-%m-%d"))
>             highs.append(high)
>             lows.append(low)
> 
> ''' 画图 '''            
> fig = plt.figure(dpi=128,figsize=(10,6)) # 获取背景图像
> plt.plot(dates,highs,c='red',alpha=0.5) # 绘制最高气温折线,alpha参数设置颜色的透明度,值为0时完全透明,默认是1
> plt.plot(dates,lows,c='blue',alpha=0.5)  # 绘制最低气温折线
> plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1) #填充两条折线之间的区域
> plt.title("Daily high temperatures,2014",fontsize=24) #设置图像标题
> plt.xlabel("",fontsize=16) #设置图像x轴标签及字体大小
> fig.autofmt_xdate() # 绘制斜的date标签,防止重叠不好看
> plt.ylabel("Temperature (F)",fontsize=16) #设置图像y轴标签及字体大小
> plt.tick_params(axis='both',which='major',labelsize=16) #设置刻度
> plt.show() #显示图像
> ```