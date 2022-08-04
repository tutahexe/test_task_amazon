from datetime import datetime


class Item:

    def __init__(self, name, rate, date):
        self.name = name
        self.rate = float(rate)
        self.date = datetime.strptime(date, '%b %d, %Y')

    def __str__(self):
        return f"Item {self.name} with {self.rate} rate released on {self.date}"
