class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
h1 = House("Gangnam", "apartment", "sell", "1 billion", 2010)
h2 = House("Mapo", "studio", "full rent", "500 million", 2007)
h3 = House("Songpa", "villa", "monthly rent", "500/50", 2000)
houses.append(h1)
houses.append(h2)
houses.append(h3)

print("There are {0} houses.".format(len(houses)))
for i in houses:
    i.show_detail()