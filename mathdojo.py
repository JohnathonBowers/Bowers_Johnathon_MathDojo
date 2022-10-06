class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        sum = num
        for x in nums:
            sum += x
        self.result += sum
        return self
    def subtract(self, num, *nums):
        diff = num
        for x in nums:
            diff += x
        self.result -= diff
        return self

md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)