print("-------（一）类的例子-------")


# class表示要创建类，Song是类的名称
class Song(object):
    # 构造方法，根据类创建对象时自动执行
    # 为什么要使用self?在构造方法和Song函数的参数列表中？
    # 因为使用self可以使表达更明确，具体来说
    # 可以通过变量前加self.来表达这是一个实例属性而不是一个局部变量。
    def __init__(self, lyrics):
        self.lyrics = lyrics

    # 获取每一句歌词并打印出来
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_boday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])
happy_boday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

# 自己的例子
oneSong = Song(["去吗？", "去啊！以最卑微的梦。", "战吗？", "战啊！以最孤高的梦。"])
oneSong.sing_me_a_song()
song = ["去吗？", "去啊！以最卑微的梦。", "战吗？", "战啊！以最孤高的梦。"]
songSecond = Song(song)

print("-------（二）学着去说面向对象-------")
# 类（class）:告诉Python创建一个新类型的东西。
# 对象（Object）:最基本类型的东西，任何实例。
# 实例（instance）:当你告诉Python创建一个类的时候你所得到的东西。
# def ：在类里面定义一个函数
# self :在一个类的函数里面，self是被访问的实例、对象的一个变量。
# 继承（inheritance）:关于一个类能从另一个类那里继承它的特征的概念，很像父母和你的关系。
# 组合（composition）:关于一个类可以由其他一些类构成的概念，很像一辆车包含几个轮子。
# 属性（attribute）:类所拥有的从组合那里得到的特性，通常是变量。
# is-a:一种用来表达某物继承自一种东西的表述，就像是“三文鱼是一种鱼”。
# has-a:一种用来表达某物是由一些东西组成或具有某种特性的表述，就像“三文鱼有一个嘴巴。”
# classX(Y):创建一个名为X并继承自Y的类
# class X(object):def init(self,J):创建一个名为X的类，类中定义了一个含J参数的init（）函数。
# class X(object):def M(self,J):创建了一个名为X的类，类中定义了一个含self和J参数的M()函数。
# foo = X():foo为X的一个实例。
# foo.K = Q:从foo那里获取一个K属性并设置为Q。
