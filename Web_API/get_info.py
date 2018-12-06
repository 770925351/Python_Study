import requests
import pygal
class GetRepo():

    ''' 获取查询的api接口地址 '''
    def get_url(self,language):
        url = 'https://api.github.com/search/repositories?q=language:' + language + '&sort=stars'
        return url

    ''' 通过API请求获取数据,并进行数据分析 '''
    def get_data(self,url):
        ''' 定义获取项目名字的列表,以及要传入的y轴数据列表,y轴数据列表是每一个是字典的元素,包含了y轴的值,标签,以及链接 '''
        names = []
        plot_dicts_stars = []
        plot_dicts_forks = []

        ''' 获取API返回的数据:'''
        r = requests.get(url)

        ''' 查看是否获取成功,返回200即为成功 '''
        print("Status code:",r.status_code) 

        ''' 将获取到的数据进行json格式化,返回的是一个字典格式
            dict_keys(['total_count', 'incomplete_results', 'items'])
        '''
        response_dict = r.json() 

        ''' 获取的仓库的条目,返回的条目是一个字典 '''
        repo_dicts = response_dict['items']
        ''' 遍历条目字典 '''
        for repo_dict in repo_dicts :

            ''' 获得每个仓库的名字,并保存在列表中 '''
            names.append(repo_dict['name'])

            ''' 获得每个仓库的star数量 简介 项目地址,保存在一个字典中是因为要传给pygal图表的y轴 '''
            plot_dict_star = {
                'value':repo_dict['stargazers_count'],
                'label':str(repo_dict['description']),
            } 
            ''' 获得每个仓库的fork数量 简介 项目地址,保存在一个字典中是因为要传给pygal图表的y轴 '''
            plot_dict_fork = {
                'value':repo_dict['forks'],
                'label':str(repo_dict['description']),
            } 

            ''' 将获取到的数据加入到列表中 '''
            plot_dicts_stars.append(plot_dict_star)
            plot_dicts_forks.append(plot_dict_fork)

        return names,plot_dicts_stars,plot_dicts_forks

    def get_config(self):
        my_config = pygal.Config()
        my_config.x_label_rotation = 45 # 设置x轴标签旋转45度
        my_config.title_font_size = 24 # 设置图标标题字体大小
        my_config.label_font_size = 14 # 设置标签字体大小 主标签
        my_config.major_label_font_size = 18 # 设置 副标签字体大小
        my_config.truncate_label = 15  # 将较长的项目名称截断为15个字符
        my_config.show_y_guides = False #隐藏表中的水平线
        my_config.width = 1000 #设置图表宽度
        return my_config