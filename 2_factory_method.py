# coding : utf-8
# create by ztypl on 2017/5/25

from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):  #抽象产品角色（Product）

    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):  #具体产品角色（Concrete Product）
    def pay(self, money):
        print("支付宝支付%s元" % money)


class ApplePay(Payment):
    def pay(self, money):
        print("苹果支付%s元"%money)


class PaymentFactory(metaclass=ABCMeta):  #抽象工厂角色（Creator）
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):   #具体工厂角色（Concrete Creator）
    def create_payment(self):
        return Alipay()

class ApplePayFactory(PaymentFactory):
    def create_payment(self):
        return ApplePay()




# 用户输入
# 支付宝，120

af = AlipayFactory()
ali = af.create_payment()
ali.pay(120)