class Op:
    def __init__(self, x):
        self.x = x

    def __le__(self, other):
        if self.x <= other.x:
            return other.x
        else:
            return self.x


n1 = Op(4)
n2 = Op(5)
print(n1 <= n2)
