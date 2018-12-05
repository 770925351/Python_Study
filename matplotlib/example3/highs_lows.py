import csv
import matplotlib.pyplot as plt
from datetime import datetime 
''' 重点介绍一下datetime中的strptime()方法
    使用:strptime("时间字符串","格式化形式")
    格式化形式:
    |实参|含义|
    |%A|星期的名称|
    |%B|月份名|
    |%m|用数字表示月份(01-12)|
    |%d|用数字表示月份的一天(01-31)|
    |%Y|四位年份(2018)|
    |%y|两位年份(18)|
    |%H|24小时制的小时数(00-23)|
    |%I|12小时制的小时数(01-12)|
    |%p|am或者pm|
    |%M|分钟数(00-59)|
    |%S|秒数(00-61)|
 '''
filename = 'sitka_weather_07-2014.csv'
# with open(filename) as file:
#     reader = csv.reader(file) # 将文件传递给reader函数,获得一个与之相关的阅读器对象
#     header_row = next(reader) # next是读取阅读器的一行,返回一个列表,列表中的元素是根据csv文件中逗号所区分

# for index,values in enumerate(header_row): # enumerate获取列表的索引和值
#     print(index,values)

''' 获取最高气温 '''
highs = []
datatimes = []
with open(filename) as file:
    reader = csv.reader(file) # 将文件传递给reader函数,获得一个与之相关的阅读器对象
    head_row = next(reader)
    for row in reader :  # 从第二行开始,遍历阅读器的每一行
        highs.append(int(row[1])) # 获得每一行索引为1的值
        datatimes.append(datetime.strptime(row[0],"%Y-%m-%d"))

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(datatimes,highs,c='red')
plt.title("Daily high temperatures,July 2014",fontsize=24)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate() # 绘制斜的date标签,防止重叠不好看
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()

