# Python 学习之抓取Github数据,分析出最受欢迎的项目

> 本次学习目的:学习使用**`web_api`**的使用
>
> 本次所用模块:`requests` `pygal`
>
> Python版本:`3.5`

## 1.配置环境

> - 安装requests
>
>   - Linux
>
>   > ```sh
>   > pip install --user requests
>   > ```
>
>   - Windows
>
>   > python -m pip install --user requests
>
> - 安装pygal
>
> > 详情请见[Python之matplotlib基础学习(绘制折线图、散点图、直方图](https://www.linuxstudy.cn/archives/23.html)

## 2.实战练习

- `get_info.py`

> ```Python
> import requests
> import pygal
> ''' 定义查询类 '''
> class GetRepo():
>     ''' 获取查询的api接口地址 '''
>     def get_url(self,language):
>         url = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=stars'
>         return url
> 
>     ''' 通过API请求获取数据,并进行数据分析 '''
>     def get_data(self,url):
>         ''' 定义获取项目名字的列表,以及要传入的y轴数据列表,y轴数据列表是每一个是字典的元素,包含了y轴的值,标签,以及链接 '''
>         names = []
>         plot_dicts_stars = []
>         plot_dicts_forks = []
> 
>         ''' 获取API返回的数据:'''
>         r = requests.get(url)
> 
>         ''' 查看是否获取成功,返回200即为成功 '''
>         print("Status code:",r.status_code) 
> 
>         ''' 将获取到的数据进行json格式化,返回的是一个字典格式
>             dict_keys(['total_count', 'incomplete_results', 'items'])
>         '''
>         response_dict = r.json() 
> 
>         ''' 获取的仓库的条目,返回的条目是一个字典 '''
>         repo_dicts = response_dict['items']
>         ''' 遍历条目字典 '''
>         for repo_dict in repo_dicts :
> 
>             ''' 获得每个仓库的名字,并保存在列表中 '''
>             names.append(repo_dict['name'])
> 
>             ''' 获得每个仓库的star数量 简介 项目地址,保存在一个字典中是因为要传给pygal图表的y轴 '''
>             plot_dict_star = {
>                 'value':repo_dict['stargazers_count'],
>                 'label':str(repo_dict['description']),
>             } 
>             ''' 获得每个仓库的fork数量 简介 项目地址,保存在一个字典中是因为要传给pygal图表的y轴 '''
>             plot_dict_fork = {
>                 'value':repo_dict['forks'],
>                 'label':str(repo_dict['description']),
>             } 
> 
>             ''' 将获取到的数据加入到列表中 '''
>             plot_dicts_stars.append(plot_dict_star)
>             plot_dicts_forks.append(plot_dict_fork)
> 		'''返回分析出的项目名字,星星数量,fork数量'''
>         return names,plot_dicts_stars,plot_dicts_forks
> 	'''获取对图表的设置参数'''
>     def get_config(self):
>         my_config = pygal.Config()
>         my_config.x_label_rotation = 45 # 设置x轴标签旋转45度
>         my_config.title_font_size = 24 # 设置图标标题字体大小
>         my_config.label_font_size = 14 # 设置标签字体大小 主标签
>         my_config.major_label_font_size = 18 # 设置 副标签字体大小
>         my_config.truncate_label = 15  # 将较长的项目名称截断为15个字符
>         my_config.show_y_guides = False #隐藏表中的水平线
>         my_config.width = 1000 #设置图表宽度
>         return my_config
> ```

- `draw_chart.py`

> ```Python
> '''导入需要的模块'''
> import pygal
> '''导入自己写的类'''
> from get_info import GetRepo
> '''要求用户输入想要分析的语言名称:(C,PHP,Python等)'''
> language = input("Please Input The Language:")
> '''新建类'''
> get_repo = GetRepo()
> '''获取api地址'''
> url = get_repo.get_url(language)
> '''通过api进行数据分析,返回分析的结果'''
> result = get_repo.get_data(url)
> '''画图'''
> chart = pygal.Bar(get_repo.get_config()) #初始化图表对象
> '''设置图表标题'''
> chart.title = "Most-Starred " + language + " Projects on Github" #初始化图标标题
> '''传入x轴y轴数据'''
> chart.x_labels = result[0]
> chart.add("stars",result[1]) #传入y轴参数
> chart.add("forks",result[2])
> '''保存图表文件'''
> chart.render_to_file("repos_" + language + ".svg")
> ```

## C
![C语言](https://ws3.sinaimg.cn/large/005BYqpgly1fxxao8sv14j31f60poq48.jpg)

## C++

![C++](https://ws3.sinaimg.cn/large/005BYqpgly1fxxaqt9vxcj31cd0ph75k.jpg)

## Java

![Java](https://ws3.sinaimg.cn/large/005BYqpgly1fxxarbjsa1j31cs0pn403.jpg)

## PHP

![PHP](https://ws3.sinaimg.cn/large/005BYqpgly1fxxarbjsa1j31cs0pn403.jpg)

## Python

![Python](https://ws3.sinaimg.cn/large/005BYqpgly1fxxashfnnqj31bn0pv400.jpg)