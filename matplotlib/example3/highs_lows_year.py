import csv 
import matplotlib.pyplot as plt
from datetime import datetime 
''' 当文件有缺失数据的时候会报错,所以需要加上try-expect-else语句块来出来异常
    异常是ValueError
'''
filename = 'death_valley_2014.csv'
dates = []
highs = []
lows = []
with open(filename) as file :
    reader = csv.reader(file)
    head_row = next(reader)
    for row in reader :
        try:
            high = int(row[1])
            low = int(row[3])
        except ValueError :
            print(datetime.strptime(row[0],"%Y-%m-%d"),"Empty Data!")
        else:
            dates.append(datetime.strptime(row[0],"%Y-%m-%d"))
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5) # 绘制最高气温折线,alpha参数设置颜色的透明度,值为0时完全透明,默认是1
plt.plot(dates,lows,c='blue',alpha=0.5)  # 绘制最低气温折线
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
plt.title("Daily high temperatures,2014",fontsize=24)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate() # 绘制斜的date标签,防止重叠不好看
plt.ylabel("Temperature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()