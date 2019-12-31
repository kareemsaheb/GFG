def printAl(arr,n):
        for i in range(len(arr)):
                if(i%2==0):
                        print(arr[i],end=" ")
if __name__=="__main__":
        
	t=int(input())
	for i in range(t):
		n=int(input())
		arr=list(map(int,input().split()))
		printAl(arr,n)
		print()
