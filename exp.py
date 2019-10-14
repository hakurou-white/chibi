class Expr(object):
    pass

class Val(Expr):
    __slots__= ['value']
    def __init__(self,value=0):
        self.value=value

    def __repr__(self):
        return f'Val({self.value})'
        
    def eval(self):
        return self.value

class Binary(Expr):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b

    def __repr__(self):
        classname=self.__class__.__name__
        return f'{classname}({self.left},{self.right})'
v=Val(1)
print(v)
assert v.eval()==1

assert isinstance(v,Expr) #==>T
assert isinstance(v,Val) #==>T
assert not isinstance(v,int) #==>F

def toExpr(a):
    if not isinstance(a,Expr):
        a=Val(a)
    return a

class Add(Expr):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval()+self.right.eval()

e=Add(1,2)
assert e.eval()==3

e=Add(1,Add(2,3))
assert e.eval()==6


class Mul(Expr):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval()*self.right.eval()
e=Mul(1,2)
assert e.eval()==2
e=Mul(1,Mul(2,3))
assert e.eval()==6        

class Sub(Expr):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval()-self.right.eval()
e=Sub(1,2)
assert e.eval()==-1

class Div(Expr):
    __slots__=['left','right']
    def __init__(self,a,b):
        self.left=a
        self.right=b
    def eval(self):
        return self.left.eval()/self.right.eval()
e=Div(7,2)
assert e.eval()==3
