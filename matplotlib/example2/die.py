
from random import randint

class Die():
    ''' 创建一个表示骰子的类 '''
    def __init__(self,num_sides=6):
        self.num_sides = num_sides # 默认骰子有六面
    
    def roll(self):
        return randint(1,self.num_sides) # 模拟掷骰子,返回点数
    
    