# Object : variables + Methods

class Account:
    def __init__(self, numID):
        self.number = numID
        self.account_type()

    def account_type(self):
        if str(self.number).startswith("1"):
            self.type = "current"
        elif str(self.number).startswith("2"):
            self.type = "saving"

    def account_rate(self):
        if str(self.type) == "current":
            self


acc = Account(1001, 2001)
print(acc.type)
