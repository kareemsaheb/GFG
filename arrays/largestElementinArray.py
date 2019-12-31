def large(data):
    max = data[0]
    for i in range(0,len(data)):
        if(data[i]>max):
            max = data[i]
    return(max)

#Below code common for most of the test cases 
# Add above defenition according to requirement
TC = int(input()) #Reading test case count 
result = []

for j in range(TC):
    size = int(input()) #Reading array size
    A = input()
    data = list(map(int, A.split(' ')))
    result.append(large(data))
#print(result)
for i in result:
    print(i)
