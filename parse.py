from exp import Val,Add
def parse(s:str):
    pos=s.find('+')
    if pos==-1:
        num=int(s)
        return Val(num)
    else:
        s1=s[0:pos]
        s2=s[pos+1:]
        return Add(parse(s1),parse(s2))

e=parse("123+456+789")
print(e)