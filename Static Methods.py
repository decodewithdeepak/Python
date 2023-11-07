class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b): # no need to pass self as parameter
        return a + b


a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

# print(a.add(7, 2))
print(Math.add(7, 2))
