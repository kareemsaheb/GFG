def mul(mylist):
	result = 1
	for x in mylist:
		result = result*x
	return result

list1=[1,5,6]
list2=[2,5,8]
print(mul(list1))
print(mul(list2))
