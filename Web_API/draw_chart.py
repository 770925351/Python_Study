import pygal
from get_info import GetRepo

language = input("Please Input The Language:")
get_repo = GetRepo()
url = get_repo.get_url(language)
result = get_repo.get_data(url)
chart = pygal.Bar(get_repo.get_config()) #初始化图表对象
chart.title = "Most-Starred " + language + " Projects on Github" #初始化图标标题
chart.x_labels = result[0]
chart.add("stars",result[1]) #传入y轴参数
chart.add("forks",result[2])
chart.render_to_file("repos_" + language + ".svg")