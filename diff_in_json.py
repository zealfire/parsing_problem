#import fileinput
#{"sad":"asdsa","ada":"asdas"}
#{"sad":"asds","ada":"asdas"}
import re
import sys
data = sys.stdin.read()
#print data
if(re.split('\n+',data)):
	lines=re.split('\n+',data)
map1={}
map2={}
k=0
for line in lines:
	#print line
	k+=1
	line=re.split(",",line)
	#print line
	for indi in line:
		splits=re.findall(r'["].*["][:]["].*["]',indi)
		#print splits
		for split in splits:
			mid=re.split(":",split)
			key=mid[0]
			value=mid[1]
			if(k==1):
				map1[key]=value
			else:
				map2[key]=value
for key,value in map1.iteritems():
	if(map1[key]<>map2[key]):
		print (key)

