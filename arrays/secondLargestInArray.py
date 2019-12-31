def find_second_largest(data):
    if len(data) > 2:
        L1 = data[0]
        L2 = data[1]
        if L2 > L1:
            L1, L2 = L2, L1
            
        for i in data[2:]: #it will start iterating from 3rd element
            if i < L2:
                continue
            elif i < L1:
                L2, i = i, L2
            else:
                L2, L1 = L1, L2
                L1, i = i, L1
        return(L2)

# Below code common for most of the test cases 
# Add above defenition according to requirement
TC = int(input()) #Reading test case count 
result = []

for j in range(TC):
    size = int(input()) #Reading array size
    A = input()
    data = list(map(int,input().split()))
    result.append(find_second_largest(data))
print(result)
