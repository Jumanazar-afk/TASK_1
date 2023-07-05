class People():
    def __init__(self, NSF, born, phone, city, country, adress):
        self.NSF = NSF
        self.born = born
        self.phone = phone
        self.city = city
        self.country = country
        self.adress = adress

    def nsf(self):
        return self.NSF()

    def born(self):
        return self.born()

    def phone(self):
        return self.phone()

    def city(self):
        return self.city()

    def country(self):
        return self.country()

    def adress(self):
        return self.adress()


p1 = People("agzam", "41.23.2200", "941354996898", "tashkent", "uzb", "street-6")
print(p1.NSF)