
def calc(s):
    if s[1]=="+":
        a=int(s[0])
        b=int(s[2])
        s=a+b
        
    return int(s)

print(calc("1+2"))