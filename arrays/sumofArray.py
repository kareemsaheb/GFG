
def sum(data):
    sum=0
    for i in data:
        sum=sum+i
    return(sum)

# Below code common for most of the test cases 
# Add above defenition according to requirement
TC = int(input()) #Reading test case count 
result = []

for j in range(TC):
    size = int(input()) #Reading array size
    A = input()
    data = list(map(int, A.split(' ')))
    result.append(sum(data))
print(result)