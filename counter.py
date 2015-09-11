from collections import Counter
list=[]
list= (raw_input().split(' '))
#print list
q = int(raw_input())
ans1=0
ans2=0
for i in range(q):
	str1=raw_input()
	str2=raw_input()
	map1 = Counter(str1)
	map2 = Counter(str2)
    
	for key, value in map1.iteritems():
		#print type(map2[key])
		if((map2[key])):
			map2[key]-=1
			map1[key]-=1
	for key, value in map1.iteritems():
		#print list[ord(key)-97]
		ans1=ans1+int(list[ord(key)-97])*int(value)
	for key, value in map2.iteritems():
		ans2+=int(list[ord(key)-97])*int(value)
if(ans1>ans2):
	print "Marut"
elif(ans2>ans1):
	print "Devil"
else:
	print "Draw"
