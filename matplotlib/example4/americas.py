''' 绘制北美的人口地图 '''

import pygal.maps.world

wm = pygal.maps.world.World()
wm.title = "North,Central,and South America"
wm.add("North America",{'ca':34126000,'mx':113423000,'us':309349000})
''' add方法接受两个参数,标签加一个有着国别码的字典,也可以是只有国别码的列表 '''
# wm.add("Central America",['bz','cr','gt','hn','ni','pa','sv'])
# wm.add("South America",['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])
wm.render_to_file('americas.svg')