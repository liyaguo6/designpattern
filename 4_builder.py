# coding : utf-8
# create by ztypl on 2017/5/25

from abc import abstractmethod, ABCMeta

#------产品------

class Player:
    def __init__(self, face=None, body=None, arm=None, leg=None):
        self.face = face
        self.arm = arm
        self.leg = leg
        self.body = body

    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.arm, self.body, self.leg)
# p=Player(12)
# print(type(p)) <class '__main__.Player'>
#------建造者------

class PlayerBuilder(metaclass=ABCMeta):  #抽象建造者
    @abstractmethod
    def build_face(self):
        pass
    @abstractmethod
    def build_arm(self):
        pass
    @abstractmethod
    def build_leg(self):
        pass
    @abstractmethod
    def build_body(self):
        pass
    @abstractmethod
    def get_player(self):
        pass


class BeautifulWomanBuilder(PlayerBuilder):  #具体建造者
    def __init__(self):
        self.player = Player()
    def build_face(self):
        self.player.face = "漂亮脸蛋"
    def build_arm(self):
        self.player.arm="细胳膊"
    def build_body(self):
        self.player.body="细腰"
    def build_leg(self):
        self.player.leg="长腿"
    def get_player(self):
        return self.player


class PlayerDirector:                  #指挥者
    def build_player(self, builder):
        builder.build_body()
        builder.build_arm()
        builder.build_leg()
        builder.build_face()
        return builder.get_player()




director = PlayerDirector()
builder = BeautifulWomanBuilder()
p = director.build_player(builder)
print(p)



