class Account:
    def __init__(self, numID):
        # Step 1: Initialize instance variables
        self.number = numID
        self.account_type()  # Step 2: Determine and set account type
        self.account_rate()  # Step 3: Set interest rate based on account type

    def account_type(self):
        # Step 4: Determine account type based on the account number
        if str(self.number).startswith("1"):
            self.type = "current"
        elif str(self.number).startswith("2"):
            self.type = "saving"

    def account_rate(self):
        # Step 5: Set interest rate based on account type
        if str(self.type) == "current":
            self.rate = 0
        if str(self.type) == "saving":
            self.rate = 5


# Step 6: Create an instance of the Account class with account number 2001
acc = Account(2001)

# Step 7: Print the account type
print(acc.type)
