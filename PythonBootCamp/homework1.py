class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((y2 - y1) / (x2 - x1))


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
print(li.distance())
print(li.slope())


class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return Cylinder.pi * self.height * (self.radius)**2

    def surface_area(self):
        return (2 * Cylinder.pi *((self.height * self.radius) + (self.radius)**2))


# EXAMPLE OUTPUT
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())



class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return (f"Account owner: {self.owner} \nAccount balance: {self.balance}")

    def deposit(self, fund):
        self.balance += fund
        print(f"Deposit of {fund} accepted; Your balance is {self.balance}")

    def withdraw(self, funds):
        if funds > self.balance:
            print("Funds Unavailable!")
        else:
            self.balance -= funds
            print(f"Withdrawal of {funds} accepted; Your balance is {self.balance}")

# 1. Instantiate the class
acct1 = Account('Jose', 100)
# 2. Print the object
print(acct1)
# 3. Show the account owner attribute
print(acct1.owner)
# 4. Show the account balance attribute
print(acct1.balance)
# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)
# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


