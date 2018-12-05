''' 解析json文件 '''
import json

''' 导入画地图的模块 '''
import pygal.maps.world

''' 设置世界地图样式 '''
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle
''' 初始化一个地图对象 '''
# wm_style = RotateStyle('#336699') # 返回一个RGB十六进制颜色对象,等会传给地图对象的style属性
# wm_style = LightColorizedStyle # 亮色主题,但是不能修改颜色,只能是pygal给你指定颜色
wm_style = RotateStyle('#336699',base_style=LightColorizedStyle) # 这样就可以用亮色主题和修改颜色了
wm = pygal.maps.world.World()
wm.title = 'The World Population in 2010'
wm.style = wm_style
from countries import get_country_code
''' 要解析的json格式
    {
        "Country Name": "Arab World",
        "Country Code": "ARB",
        "Year": "1960",
        "Value": "96388069"
    },
'''
filename = 'population_data.json'
world_population = {} # 保存国家和人口对应的字典
with open(filename) as file:
    pop_data = json.load(file) # 将json文件读取并返回一个列表，列表的元素就是一个个字典

for pop_dict in pop_data: # 循环从列表中获取每个键值对
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code :
            world_population[code] = population
        else :
            print("ERROR - " + country_name)
''' 收集好信息之后,为了让地图更加直观一点,将人口信息按照数量分组 '''            
level_1 = {}
level_2 = {}
level_3 = {}
for code,population in world_population.items():
    if population < 10000000:
        level_1[code] = population
    elif population < 1000000000:
        level_2[code] = population
    else:
        level_3[code] = population

wm.add('0-10m',level_1)
wm.add('10m-1bn',level_2)
wm.add('>1bn',level_3)
wm.render_to_file('world.svg')