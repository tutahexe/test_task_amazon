from datetime import datetime


class Item:

    def __init__(self, name, rate, date):
        self.__name = name
        self.__rate = float(rate)
        #self.__date = datetime.strptime(date, '%b %d, %Y')
        self.__date = date

    def get_name(self):
        return self.__name

    def get_rate(self):
        return self.__rate

    def get_date(self):
        return self.__date

    def __str__(self):
        return f"Item {self.__name} with {self.__rate} rate released on {self.__date}"

    def __eq__(self, other):
        return self.__name == other.__name

    def __lt__(self, other):
        return self.__date < other.__date
