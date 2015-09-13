import re
import sys
import operator
input=sys.stdin.read()
words=[]
k=0
words=re.split('\n+',input)
map={}
for word in words:
	find=[]
	find=re.findall(r'HTTP.*',word)
	for f in find:
		list=f.split(' ')
		key=list[1]
		if(key in map):
			map[key]+=int(1)
		else:
			map[key]=int(1)
#for key,value in map.iteritems():
#	print key,value

#sorted_x = sorted(map.items(), key=operator.itemgetter(1))
#sorted(map.iteritems(), key=lambda item: -item[1])
for key,value in sorted(map.iteritems(), key=lambda item: item[1], reverse=True):
	print key,value
