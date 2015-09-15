
import math
f=math.factorial
t=int(raw_input())
for i in t:
	s=0
	n=int(raw_input())
	word=str(f(n))
	for j in range(1,10):
		s=s+j*word.count(j)
	print s
