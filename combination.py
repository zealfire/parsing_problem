fac=[]
def fact(p):
	i=1
	ans=1
	fac.append(1)
	mod=1000000007
	p=50
	while i<p+1:
		ans=((ans%mod)*(i%mod))%mod
		fac.append(ans)
		i+=1
	#return ans
t=int(raw_input())
fact(50)
for i in range(t):
	list1=raw_input().split(' ')
	m=int(list1[0])
	n=int(list1[1])
	mod=1000000007
	if(m==1 and n==1):
		print "2"
		continue
	if(m<n-1):
		print "-1"
	else:
		p=fac[m]
		q=m+2-n
		while q<=m+1:
			p=((p%mod)*(q%mod))%mod
			q+=1
		print p
		
