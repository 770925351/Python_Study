# Python学习之matplotlib之制作世界人口地图(解析json文件)

> - 本次学习目的: 
>
>   > 学习如何解析json文件,并将数据用pygal渲染
>
> - 本次所用模块:
>
>   > `json `：解析json文件
>   >
>   >  `pygal.maps.world` ：获取世界地图渲染对象
>   >
>   >  `pygal.style` ：更改世界地图格式
>   >
>   > `pygal_maps_world.i18n` ：获取世界各国两位字母编码
>
> - Python版本:`3.5`

## 1.配置环境

> - 安装`matplotlib`和`pygal`
>
>   > 详情见 [Python之matplotlib基础学习(绘制折线图、散点图、直方图)](https://www.linuxstudy.cn/archives/23.html)
>
> - 安装`pygal.maps.world`
>   - Linux
>     > ```sh
>     > pip install pygal_maps_world
>     > ```
>   - Windows
>
>     > python -m pip install --user pygal_maps_world

## 2.Demo1(解析json文件)

> `world_population.py`
>
> ```python
> import json
> 
> ''' 要解析的json格式
>     {
>         "Country Name": "Arab World",
>         "Country Code": "ARB",
>         "Year": "1960",
>         "Value": "96388069"
>     },
> '''
> filename = 'population_data.json' #初始化文件名字
> world_population = {} # 保存国家和人口对应的字典
> with open(filename) as file:
>     pop_data = json.load(file) # 将json文件读取并返回一个列表，列表的元素就是一个个字典
> 
> for pop_dict in pop_data: # 循环从列表中获取每个键值对
>     if pop_dict['Year'] == '2010': #从每个字典中中挑选出时间为2010年份数据
>         country_name = pop_dict['Country Name'] # 获取国家名字
>         population = int(float(pop_dict['Value'])) #获取人口数量
>         code = get_country_code(country_name) #获取国家识别码,在这里是自己写的一个函数在后面的例子里会有,这里不多做赘述
>         if code : #用if-else判断是因为数据中有些数据是一个国家分不同地区展示,所以只需要正经有识别码的消息就好,具体逻辑需要视实际json文件而定
>             world_population[code] = population
>         else :
>             print("ERROR - " + country_name)
> ```

## 3.Demo2(绘制人口地图)

> `counties.py`
>
> ```Python
> ''' 导入COUNTRIES,COUNTRIES是一个识别码和国家组成的字典,一个识别码和一个国家是一个键值对 '''
> from pygal_maps_world.i18n import COUNTRIES
> 
> def get_country_code(country_name): # 通过遍历COUNTRIES,通过国家名字获取国家识别码
>     for code,name in COUNTRIES.items():
>         if name == country_name :
>             return code
>     return None        
> ```
>
> `world_population.py`
>
> ```Python
> ''' 解析json文件 '''
> import json
> 
> ''' 导入画地图的模块 '''
> import pygal.maps.world
> 
> ''' 设置世界地图样式 '''
> import pygal
> from pygal.style import RotateStyle # 通过 RotateStyle 可以制定地图颜色主题
> from pygal.style import LightColorizedStyle # 亮色主题
> 
> ''' 初始化一个地图对象 '''
> # wm_style = RotateStyle('#336699') # 返回一个RGB十六进制颜色对象,等会传给地图对象的style属性
> # wm_style = LightColorizedStyle # 亮色主题,但是不能修改颜色,只能是pygal给你指定颜色
> wm_style = RotateStyle('#336699',base_style=LightColorizedStyle) # 这样就可以用亮色主题和修改颜色了
> wm = pygal.maps.world.World() # 初始化一个地图对象
> wm.title = 'The World Population in 2010' # 设置地图的题目
> wm.style = wm_style # 设置地图的风格
> 
> ''' 解析json '''
> from countries import get_country_code # 导入自己写的方法
> filename = 'population_data.json' # 初始化文件名字
> world_population = {} # 保存国家和人口对应的字典
> 
> with open(filename) as file:
>     pop_data = json.load(file) # 将json文件读取并返回一个列表，列表的元素就是一个个字典
> 
> for pop_dict in pop_data: # 循环从列表中获取每个键值对
>     if pop_dict['Year'] == '2010': # 获取2010年数据
>         country_name = pop_dict['Country Name'] # 获取国家名字
>         population = int(float(pop_dict['Value']))# 获取国家人口
>         code = get_country_code(country_name) # 获取国家识别码
>         if code :
>             world_population[code] = population # 将国家和人口键值对填入字典
>         else :
>             print("ERROR - " + country_name)
>             
> ''' 收集好信息之后,为了让地图更加直观一点,将人口信息按照数量分组 '''            
> level_1 = {} # 小于1000万人口
> level_2 = {} # 大于1000万小于10亿人口
> level_3 = {} # 大于10亿人口
> 
> for code,population in world_population.items():
>     if population < 10000000:
>         level_1[code] = population
>     elif population < 1000000000:
>         level_2[code] = population
>     else:
>         level_3[code] = population
> ''' add方法接受两个参数,标签加一个有着国别码的字典,也可以是只有国别码的列表 '''
> wm.add('0-10m',level_1)
> wm.add('10m-1bn',level_2)
> wm.add('>1bn',level_3)
> wm.render_to_file('world.svg') # 将图像保存为svg文件
> ```

