

def ispalndrome(n):
    num=n
    d=0
    rev=0
    while num>0:
        
        d=n%10
        n=n//10
        rev=rev*10+d
    if(num==rev):
        return True
    else:
        return False

TC = int(input()) #Reading test case count 
result = []

for j in range(TC):
    size = int(input()) #Reading array size
    A = input()
    data = list(map(int,input().split()))
    result.append(ispalndrome(n))
print(result)
