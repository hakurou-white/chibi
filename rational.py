class Q(object):
    def __init__(self,a,b):#コンストラクタ
        self.a=a
        self.b=b

    def __repr__(self):
        if self.b==1:
            return str(self.a)
        else:    
            return f'{self.a}/{self.b}'

q=Q(1,2)
q=Q(2,1)
print(q)
