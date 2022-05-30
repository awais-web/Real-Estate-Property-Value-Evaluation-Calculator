'''
This app will evaluate the value of your property with respect to your society general facilities and
location of your plot.

First it will ask
general your property society information
than ask about your property distance with basic facilities
than evaluate the value of your property.
'''

class Bwp():

    # To ask some general information of Your property area
    def __init__(self):
        self.rate = int(input("Per Marla Land Rates in your Area?"))
        self.shops = input("\nGrocery Shops  available? [y/n]: ")
        self.StreetSize = int(input("General Street Size? [in Feet]"))
        self.garder = input("Garden or Children Play Area? [y/n]: ")
        self.double = input("Your Plot have two Street Facing? [y/n]: ")



    # To ask some specific information about your property and compare it with our defined standards
    def MyPlotRate(self):
        FivePercent = (self.rate / 100) * 5

        self.MD = int(input("\nYour Plot Distance from Mosque? [in meters]: "))
        if self.MD <= 500:
            self.rate = self.rate + FivePercent

        self.SS = int(input("\nYour House Front Street Size? [in Feet]: "))
        if self.SS >= self.StreetSize:
            self.rate = self.rate + FivePercent

        if self.shops == 'y':
            self.SD = int(input("Your Plot Distance from Grocery Shop? [in meters]: "))
            if self.SD <= 500:
                self.rate = self.rate + FivePercent

        if self.double:
            self.rate = self.rate + (2 *FivePercent)

        if self.garder == 'y':
            self.GD = int(input("Your Plot Distance from Garden or Play Area? [in meters]: "))
            if self.GD <= 500:
                self.rate = self.rate + FivePercent

        # Representing the value of your property
        p = "\nYour Expected Plot Per Marla Rates on the basis of your Plot Location is: {}"
        print(p.format(self.rate))














Myhome = Bwp()
# RehmatColony.SocietyInfo()
Myhome.MyPlotRate()


