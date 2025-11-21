
class Bike:

    def __init__(self,name,color,price,company):
        self.Name = name
        self.Color = color
        self.Price = price
        self.Company = company

    def companys(self):
        print(f'bike company is : {self.Company}')

    def details(self):
        self.companys()
        print('Name : ',self.Name)
        print('Color : ',self.Color)
        print('Price : ',self.Price)
        print('\n')


bike1 = Bike('FZ-s','Blue',150000,'Yamaha')
bike2 = Bike('Classic-35','Black',350000,'Royal Enfield')
bike3 = Bike('Splendor +','Police patto',90000,'Hero')
bike4 = Bike('MT-15','White',250000,'Yamaha')



bike1.details()
bike2.details()
bike3.details()
bike4.details()
