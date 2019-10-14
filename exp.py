class Val(object):
class Expr(object):
    pass

class Val(Expr):
    __slots__ = ['value']
    def __init__(self, value = 0):
        self.value = value
@@ -13,18 +16,39 @@ def eval(self):
print(v)
assert v.eval() == 1

class Add(object):
assert isinstance(v, Expr)
assert isinstance(v, Val)
assert not isinstance(v, int)


def toExpr(a):
    if not isinstance(a, Expr):
        a = Val(a)
    return a


class Add(Expr):
    __slots__=['left', 'right']
    def __init__(self, a, b):
        if not isinstance(a, Expr):
            a = Val(a)
        if not isinstance(b, Expr):
            b = Val(b)
        self.left = a
        self.right = b
    def eval(self):
        return self.left.eval() + self.right.eval()


e = Add(1,Add(1,2))
print(e.eval())
assert e.eval() == 4

e = Add(Val(1), Val(2))
assert e.eval() == 3
print(e.eval())
assert e.eval() == 3


e = Add(Val(1), Add(Val(2),Val(3)))
e = Add(Val(1),Add(Val(2),Val(3)))
print(e.eval())
assert e.eval() == 6
print(e.eval()) 