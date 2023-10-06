
i=0
a=[1]

while i<100:
	result=a[i]+a[i-1]
	a.append(result)
	i=i+1
	print(a[i])
