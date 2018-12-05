''' 使用Pygal去创建图表,要了解Pypal可以创建什么样的图表,访问http://www.pypal.org
    单击Documentation,再单击Chart types,会有示例
'''

from die import Die
import pygal

die = Die()
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar() # Bar是直方图类型
hist.title = "Results of rolling D6 1000 times" #设置直方图题目
hist.x_title = "Result" # 设置直方图x轴标题
hist.y_title = "Frequency of Result" # 设置直方图y轴标题
hist.add('D6',frequencies) # 将标签和数据传入
hist.render_to_file('die_visual.svg') # 将直方图进行渲染成svg格式