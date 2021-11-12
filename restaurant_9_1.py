class Restaurant():
    def __init__(self,restaurant_name ,cuisine_type ):
        self.restaurant_name =restaurant_name
        self.cuisine_type =cuisine_type
        self.number_served =0

    def describe_restaurant(self):
        print('My restuarant name is %s, cuisine_type  is %s'% (self.restaurant_name,self.cuisine_type))

    def open_restaurant(self):
        print('The restuarant is open')

    def set_number_served(self,guest):
        self.number_served=guest

    def get_number_served(self):
        print('served guest: %s'%self.number_served)

class Money():
    def __init__(self,rmb):
        self.rmb=rmb

    def get_today_money(self):
        print(self.rmb)

class ChineseRestaurant(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,menu):
        super().__init__(restaurant_name,cuisine_type)
        self.menu=menu
        self.money=Money(50)

    def get_menu(self):
        print(self.menu)


cr=ChineseRestaurant('nameofres','none','1')
# cr.money=Money(50)
cr.money.get_today_money()
# cr.get_number_served()
# cr.get_menu()





# res=Restaurant('yxs restaurant','noneType')
# res.describe_restaurant()
# res.open_restaurant()
# res.get_number_served()
# res.set_number_served(200)
# res.get_number_served()
