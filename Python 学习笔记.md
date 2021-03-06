1. 2/2 -->>整数/整数 得到浮点数类型 float类型
2. 2//2 -->整数//整数 得到整数类型 int类型[[]]
3. 0b 二进制
4. 0x 十六进制
5. 0o 八进制
6. bin()转换为二进制
7. type()查看数据类型
8. int()转换为十进制
9. hex()转换为十六进制
10. oct()转换为八进制
11. 0表示为假False,其他数字都表示为真True
12. [] 列表
13. {} 字典
14. 用 单引号' ' 双引号" " 三引号''' '''表示字符串
15. 三引号'''可以支持str字符串换行

```Python
'''
hello world
hello world
'''
```

16. 单引号与双引号也可以实现字符串换行,但是必须得加上\\
17. 转义字符

>\n 换行
>
>\\' 单引号
>
>\\t 横向制表符
>
>\\r 回车

18. 当一个字符串前加上一个r,代表是原始字符串

> 例如: r'hello \n world'

19. 字符串的运算

>\+ 拼接字符串
>
>\* 多次重复字符串
>
>字符串[序号] 访问字符串的序号个字符
>
>注:序号从0开始,-n代表倒数第n个字符
>
>[0:n] 从第一个到第n个字符
>
>[n:]从第n个字符到最后
>
> [-n:]从倒数第n个字符到最后

# 组

1. 列表(list)

> [元素,元素,元素]

2. 访问列表元素

> [元素,元素,元素]\[序号]
>
> 注:[元素,元素,元素]\[序号] 返回的是元素数据类型
>
> [元素,元素,元素]\[序号:](带有截取符号)返回的是列表类型

3. 列表操作

> \+ 合并列表
>
> \* 重复列表

4. 元组(tuple)

> (元素,元素,元素),其他操作与列表相似
>
> 注:当元组中只有一个元素时候,返回数据类型为这个元素的数据类型
>
> 定义一个元素的元组: **(元素,)** 
>
> 定义一个空元组: **()**

5. 集合(set)

> {元素,元素,元素}
>
> 特点: 无序,不重复 切片和序列都不支持
>
> \- 集合A - B表示剔除A中含有的B中的元素
>
> & 集合A & B表示A和B的交集,返回一个集合类型
>
> \| 集合A | B表示A和B的并集,返回一个集合类型

6. 字典(dict)

> {key1:value1,key2:value2,key3:value3....}
>
> 通过key来访问value
>
> {}[key]
>
> key是唯一的
>
> key必须是不可变的类型(int,str)

# 数据类型总结

1. str list tuple 序列

> 数据类型 [序号] 返回相应序号位置的元素
>
> \* \+ 运算

2. 切片 **:**

>

3. kaitouin 和 not in

> 判断元素是否存在

4. 常用函数

> max() 
>
> min() 
>
> id()显示某一个变量在内存中的地址
>
> len() 数据类型 长度
>
> ord() 转换为 ascII 码

# 变量与运算符

1. 命名规则

> - 不能用保留关键字
> - 字母、下划线、数字组成，但是不能由数字开头
> - 变量名区分**大小写**

2. 比较有意思的几种情况

```Python
a = 1
b = a
a = 3
print(b)
```

```Python
1
```
```python
a = [1,2,3,4,5]
b = a
a[0] = '1'
print(b)
```

```Python
['1',2,3,4,5]
```

> 造成以上两种情况的原因:
>
> int str tuple 值类型(不可变) list dict set 引用类型(可变)
>
> 引用类型的数值是可以改变的,值类型是不可变的.

3. 运算符

> \+ 连接,相加
>
> \* 重复 
>
> \- 相减
>
> / 相除
>
> // 整除
>
> % 求余数
>
> ** 乘方
>
> is 与 ==的关系
>
> ==比较值相等 is比较身份是否相等
>
> isinstance(变量,(类型,类型,类型)),判断变量和类型是否一致

4. range(a,b)

> 生成从a到b的序列

5. range(a,b,c)

> a到b的序列,c为步长,就是每两个元素的距离

6. 如何让一个文件夹成为一个包

> 文件夹下新建文件\__init__.py,而且这个文件的模块名称是包的名字,即是文件夹的名字

7. 将包别名

> import 包 as 别名

8. 需要引入包中的某一个变量或者函数的方法

> from 包.模块 import 变量名,函数名 
例子(导入t包中c7模块中的a变量):
from t.c7 import a

9. 系统常用的内库

> sys
> datetime
> io

# 函数

1. round()函数

> 保留指定小数位数
>
> 例如:
>
> a = 1.234
>
> round(a,2) = 1.23

2. Python函数的返回值默认为none
3. Python函数返回多个返回值,最后返回的是一个元组类型
4. 序列解包

> a,b,c = 1,1,1
>
> 或者 d = (1,1,1)
>
> a,b,c = d

5. 必须参数与关键字参数

> 必须参数:是指函数的参数必须按照顺序传进去,例如:add(x,y),你如果这样传的话add(1,2),x=1,y=2
>
> 关键字参数:是指指定每个参数是啥,例如add(x,y) add(x = 1,y = 2)

6. 默认参数

> 默认参数是指在定义函数时候就把参数的值定义,在调用函数的时候,如果不传进去参数的话,那么参数的值就是预定义时候的值
>
> 例:
>
> ```Python
> def print_stu_message(name,age=18,college="北华航天工业学院"):
>     print("我叫:"+name+"我的年龄是:"+str(age)+"我的大学是:"+college)
> print(print_stu_message("tianchao"))
> ```

7. 函数和方法的区别

>方法:设计层面
>函数:程序运行、过程式的一种概念

8. 局部变量与全局变量

> 局部变量与全局变量同名时不会覆盖全局变量,一旦出去函数作用域,全局变量立马恢复原先值

9. 几个常用的函数

> title() 将英文单词第一个字母大写

10. 函数中传递列表,如果不想修改列表的值,请这样传**列表名[:]**
21. 函数中想传入不限数量个参数,def 函数名(*变量名),在函数调用的时候,传入多个参数,函数会自动将这些参数封装成一个元组,利用元组去访问各个参数
22. 函数中使用任意数量的关键字实参

> def 函数名(**变量名)
>
> ```Python
> # 使用任意数量的关键字实参
> 
> def student(**infos):
>     infomation = {}
>     for key,value in infos.items() :
>         infomation[key] = value
> 
>     return infomation
> 
> print(student(name='tianchao',age='23',college='NCIAE'))
> 
> ```
>
> ```Python
> {'name': 'tianchao', 'college': 'NCIAE', 'age': '23'}
> ```

# 类

> 定义:
>
> class 类名():
>
> ​	对象
>
> ​	函数等等
>
> 构造函数:
>
> def \__init__() 
>
> 类内部的方法需要使用自己的对象内部定义的变量的话,需要引入**self**关键字,调用方式为:**self.变量**

1. 继承

> Python3: 
>
> ```Python
> class 类名(父类名):
>     def __init__(self,变量,变量):
>         super().__init__(变量,变量)
> ```
>
> Python2.7:
>
> ```Python
> class 类名(父类名):
>     def __init__(self,变量,变量):
>         super(类名,self).__init__(变量,变量)
> ```
>

2. OrderedDict()类

> 初始化一个有顺序的字典

3. 驼峰命名法

> 类名中的每个单词的首字符都大写,而不使用下划线.实例名和模块名都采用小写格式,并在单词之间加上下划线

# 文件和异常

1. 读入整个文件

> - open("文件路径")
>
> - open()返回一个表示文件的对象,下方的**with**表示系统会自动在合适的时候去关闭文件,以避免文件数据的丢失
> - 这样读取,结果会多输出一个空行,原因是:read()到达文件末尾时候会返回一个空字符串,而将这个空字符串显示出来就是一个空行
> - 这个空行可以用方法rstrip()去进行删除
>
> ```Python
> with open("./pi.txt") as file:
> #file = open("./pi.txt") (也可以这么定义)
> 	contents = file.read()
> 	print(contents)
> ```
>
> ```Python
> 3.1415926535
>   8979323846
>   2643383279
> 
> ```

2. 逐行读取

> - 利用for循环语句
> - 输出结果会出现空行,是因为每一行都会有一个\n换行符,所以输出出来就会有空行
> - 空行可以用方法rstrip()去进行删除
>
> ```Python
> with open("./pi.txt") as file:
>     for line in file :
>         print(line)
> ```

3. 将文件读出来的每行内容保存成一个列表

> - readlins()
> - 多余的空格可以用strip()删除
>
>  ```Python
> with open("./pi.txt") as file:
>     lines = file.readlines()    
> print(lines)    
>  ```
>

4. replace(原单词,替换单词)

>功能:替换字符串中的特定单词

5. 异常

> - ZeroDivisionError 异常处理
>
> > 这种异常是在0作为被除数时候会出现,一般解决异常的思路就是用try-except代码块
> >
> > ```python
> > try:
> >     pass
> > except 异常名称:
> >      pass
> > ```
>
> - try-except-else代码块
>
> >工作原理:Python尝试执行try代码块中的代码,而且只有try代码块中存在的代码才可能引发异常,except代码块中的代码表示如果出现某种异常时候系统该怎么办,而else代码块中的代码是try代码块中的代码执行成功之后才能运行
>
> >```python
> >try:
> >    pass
> >except 异常名称:
> >    pass
> >else:
> >     pass
> >```
>
> - FileNotFoundError异常
>
> > 找不到文件会出现这种异常
>
> - split()函数
>
> > 将字符串按照空格分隔成n个元素,并将这些元素存储在列表中,可以用于去统计一篇文章的单词数量
>
> - count()函数
>
> > 计算字符串中字串的个数
> - lower()函数
> > 将字符串全部转换为小写格式

6. 存储数据

> JSON
>
> json模块可以使Python创建json格式文件,下面介绍两个函数,一般使用的时候需要在文件中导入json模块
>
> ```python
> import json
> ```
>
> - json.dump()
>
> > json.dump(参数一,参数二)
> >
> > 参数一是指你需要写入的内容,参数二是你要写入的文件对象名字
> >
> > 示例代码:
> >
> > ```Python
> > numbers = [2,4,6,8,10]
> > filename = "number.json"
> > with open(filename,"w") as file :
> >     json.dump(numbers,file)
> > ```
>
> - json.load()函数
>
> >功能是读取json格式文件内容
> >
> >使用方法是json.load(文件名),这将返回一个字符串
> >
> >```Python
> >with open(filename) as file :
> >    content = json.load(file)
> >```

# 测试代码

1. 单元测试

>核实函数某个方面没有问题

2. 测试用例

> 一组单元测试,核实函数在各种情形下的行为都符合要求

3.全覆盖测试

> 全部测试一遍,了解即可

> 此为测试修改
