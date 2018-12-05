''' 模拟随机漫步 '''

from random import choice

class RandomWalk():
    ''' 一个生成随机漫步数据的类 '''
    def __init__(self,num_points=5000):
        ''' 初始化自己的点属性 '''
        self.num_points = num_points
        ''' 使得x,y坐标都从0开始 '''
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        ''' 计算随机漫步的点 '''
        while len(self.x_values) < self.num_points :
            x_direction = choice([1,-1]) # 随机选择前进方向    
            x_distance = choice([0,1,2,3,4,5]) # 随机选择前进距离
            x_step = x_direction * x_distance # 计算前进距离

            y_direction = choice([1,-1]) # 随机选择前进方向    
            y_distance = choice([0,1,2,3,4,5]) # 随机选择前进距离
            y_step = y_direction * y_distance # 计算前进距离

            ''' 拒绝原地踏步 '''
            if x_step ==0 and y_step ==0 :
                continue

            ''' 计算点的坐标 '''
            next_x = self.x_values[-1] + x_step # -1是表示列表最后的一个点
            next_y = self.y_values[-1] + y_step

            ''' 将计算出来的点加入列表中 '''
            self.x_values.append(next_x)
            self.y_values.append(next_y)
