
def calc(s):
    print("s=",s)
    nums=s.split("+")
    m=len(nums)
    for i in range(m):
      a=1
      if "*" in nums[i]:
        num=nums[i].split("*")
        n=len(num)
        for j in range(n):
          num[j]=int(num[j])
          a=a*num[j]
          if j==n-1:
            nums[i]=int(a)
            
      else:
        nums[i]=int(nums[i])
          
    return sum(nums)

print(calc("1"))
print(calc("2"))
print(calc("1+2"))
print(calc("1*2+3"))
print(calc("1+2*3"))