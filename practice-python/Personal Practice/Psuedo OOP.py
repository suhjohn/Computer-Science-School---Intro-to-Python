#pseudo_constructor
#initialize object members



def person_init(name, money):
    obj = {name : money}
    obj['give_money'] = Person[1]
    obj['get_money'] = Person[2]
    obj['show'] = Person[3]
    return obj

def give_money(self, other, money):
    get_money(other, money)
    self.value = self.value - money
    return self

def get_money(self, money):
    self.value += money
    return self

def show(self):
    print(self)

Person = person_init, give_money, get_money, show

if __name__ == "__main__":

    # object creation
    g = Person[0]('greg', 5000)
    j = Person[0]('john', 2000)

    g['show'](g)
    j['show'](j)
    print('')

    # message passing
    g['give_money'](g, j, 2000)

    # does it work?

    g['show'](g)
    j['show'](j)

