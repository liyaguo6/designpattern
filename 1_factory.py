# coding : utf-8
# create by ztypl on 2017/5/24

from abc import abstractmethod, ABCMeta

class Payment(metaclass=ABCMeta):  #抽象产品角色（Product）

    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):   #具体产品角色（Concrete Product）

    def __init__(self, enable_yuebao=False):
        self.enable_yuebao = enable_yuebao

    def pay(self, money):
        if self.enable_yuebao:
            print("余额宝支付%s元" % money)
        else:
            print("支付宝支付%s元" % money)


class ApplePay(Payment):    #具体产品角色（Concrete Product）
    def pay(self, money):
        print("苹果支付%s元" % money)


class PaymentFactory:  #工厂角色（Creator）

    def create_payment(self, method):
        if method == "alipay":
            return Alipay()
        elif method == "applepay":
            return ApplePay()
        elif method == "yuebao":
            return Alipay(enable_yuebao=True)
        else:
            raise NameError(method)

f = PaymentFactory()
p = f.create_payment("alipay")
p.pay(100)