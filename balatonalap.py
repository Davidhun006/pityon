class balaton():
    def __init__(self, település, fekvés, szám):
        self.település = település
        self.fekvés = fekvés
        self.szám = szám
    def fugg(self):
        if self.fekvés == "é":
            return 'északi'
        else:
            return 'déli'
    def elotag(self):
        if self.szám <= 5000:
            return 'falu'
        elif self.szám >= 5000 and self.szám <= 10000:
            return 'nagyközség'
        else:
            return 'város'
