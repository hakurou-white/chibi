class Val(object):
    __slots__= ['value']
    def __init__(self,v=0):
        self.value=v
    def eval(self):
        return self.value

e=Val(1)
assert e.eval()==1