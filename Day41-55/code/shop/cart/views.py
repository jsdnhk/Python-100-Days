from django.core import serializers
from django.shortcuts import render, redirect

from cart.models import Goods


def index(request):
    goods_list = list(Goods.objects.all())
    return render(request, 'goods.html', {'goods_list': goods_list})


class CartItem(object):
    """購物車中的商品項"""

    def __init__(self, goods, amount=1):
        self.goods = goods
        self.amount = amount

    @property
    def total(self):
        return self.goods.price * self.amount


class ShoppingCart(object):
    """購物車"""

    def __init__(self):
        self.items = {}
        self.index = 0

    def add_item(self, item):
        if item.goods.id in self.items:
            self.items[item.goods.id].amount += item.amount
        else:
            self.items[item.goods.id] = item

    def remove_item(self, id):
        if id in self.items:
            self.items.remove(id)

    def clear_all_items(self):
        self.items.clear()

    @property
    def cart_items(self):
        return self.items.values()

    @property
    def total(self):
        val = 0
        for item in self.items.values():
            val += item.total
        return val


def add_to_cart(request, id):
    goods = Goods.objects.get(pk=id)
    # 通過request對象的session屬性可以獲取到session
    # session相當於是服務器端用來保存用戶數據的一個字典
    # session利用了Cookie保存sessionid
    # 通過sessionid就可以獲取與某個用戶對應的會話(也就是用戶數據)
    # 如果在瀏覽器中清除了Cookie那麼也就清除了sessionid
    # 再次訪問服務器時服務器會重新分配新的sessionid這也就意味着之前的用戶數據無法找回
    # 默認情況下Django的session被設定爲持久會話而非瀏覽器續存期會話
    # 通過SESSION_EXPIRE_AT_BROWSER_CLOSE和SESSION_COOKIE_AGE參數可以修改默認設定
    # Django中的session是進行了持久化處理的因此需要設定session的序列化方式
    # 1.6版開始Django默認的session序列化器是JsonSerializer
    # 可以通過SESSION_SERIALIZER來設定其他的序列化器(例如PickleSerializer)
    cart = request.session.get('cart', ShoppingCart())
    cart.add_item(CartItem(goods))
    request.session['cart'] = cart
    return redirect('/')


def show_cart(request):
    cart = serializers.deserialize(request.session.get('cart'))
    return render(request, 'cart.html', {'cart': cart})
