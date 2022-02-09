arr=[2,3,4,1,4,5]
n=len(arr)
for i in range(1,n):
	suml=0
	sumr=0
	for j in range(0,i):
		suml=suml+arr[j]
	for k in range(i+1,n):
		sumr=sumr+arr[k]
	if sumr==suml:
		print(arr[i])