class Katsuo(Nigiri):
    top = "かつお"
    topping = "生姜と握り"
    price = 100


def show_attributes(Self):
    super().show_attridutes()
    print("topping: {}".format(self.topping))


K1 = Katsuo()
K1.show_attributes()
