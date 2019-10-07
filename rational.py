class Q(object):
    def __init__(self,a,b):#コンストラクタ
        self.a=a
        self.b=b

    def __repr__(self):
        if self.b==1:
            return str(self.a)
        else:    
            return f'{self.a}/{self.b}'

    def add(self,q):
        a=self.a
        b=self.b
        c=q.a
        d=q.b
        return Q(a*d+b*c,b*d)

q=Q(1,2)
q=Q(2,1)
q1=Q(1,2)
q2=Q(1,3)
print(q1.add(q2))
print(q)
