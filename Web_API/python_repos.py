import requests
import pygal
# from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

# url = http://ip.taobao.com/service/getIpInfo.php?ip= # 获取ip归属地的接口
# 执行API调用并存储响应
names = []
plot_dicts_stars = []
plot_dicts_forks = []
url = 'https://api.github.com/search/repositories?q=language:PHP&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code) # 状态码200 表示成功
response_dict = r.json() # 返回信息为json格式
repo_dicts = response_dict['items'] # 获取查询到的仓库列表
for repo_dict in repo_dicts :
    names.append(repo_dict['name'])
    plot_dict_star = {
        'value':repo_dict['stargazers_count'],
        'label':str(repo_dict['description']),
    } 
    plot_dicts_stars.append(plot_dict_star)
    plot_dict_fork = {
        'value':repo_dict['forks'],
        'label':str(repo_dict['description']),
    } 
    plot_dicts_forks.append(plot_dict_fork)
    
# my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45 # 设置x轴标签旋转45度
my_config.title_font_size = 24 # 设置图标标题字体大小
my_config.label_font_size = 14 # 设置标签字体大小 主标签
my_config.major_label_font_size = 18 # 设置 副标签字体大小
my_config.truncate_label = 15  # 将较长的项目名称截断为15个字符
my_config.show_y_guides = False #隐藏表中的水平线
my_config.width = 1000 #设置图表宽度
chart = pygal.Bar(my_config) #初始化图表对象
chart.title = "Most-Starred Python Projects on Github" #初始化图标标题
chart.x_labels = names #传入x轴参数
chart.add("stars",plot_dicts_stars) #传入y轴参数
chart.add("forks",plot_dicts_forks)
chart.render_to_file("python_repos_PHP.svg")