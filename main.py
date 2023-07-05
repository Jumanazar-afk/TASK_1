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


a = input(People.nsf)
b = input(People.born)
c = input(People.phone)
d = input(People.city)
e = input(People.country)
f = input(People.adress)

print(a,"My name is:",
      b,"i was born:",
      c,"my phone = ",
      d,"my city:",
      e,"my country:",
      f,"my adress:")