import re
import sys
#sentinel = '' # ends when this string is seen
#for line in iter(raw_input, sentinel):
#	print line+"hello"
   # '\n'.join(iter(raw_input, sentinel))
#print sentinel
#browser stack interview set 7
#print "world"
input=sys.stdin.read()
words=[]
k=0
words=re.split('\n+',input)
#print words
for word in words:
	single=word.split(' ')
	if(single[0]=='GET'):
		print "request"
		print single[1]
		k=1
	elif(single[0]!='GET' and k!=1 and k!=2):
		print "response"
		k=2
	if('Accept-Language:' in single):
		print single[1]
	elif('Content-Type:' in single):
		print single[1]
