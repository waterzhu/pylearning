a=0
b=1
sum=[1]
times = input('intput your number: ')
for i in range(times):
	c=a+b
	a=b
	b=c
	sum.append(c)
print(sum[times])
