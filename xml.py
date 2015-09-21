import fileinput
import sys
import re
filename= sys.argv[1]
fp=open(filename)
content=fp.read()
item=re.findall(r'<sum>.*</sum>',content,re.DOTALL|re.MULTILINE)
if(item):
	for it in item:
		numbers=re.findall(r'[0-9]+',it,re.DOTALL|re.MULTILINE)
		s=0
		for no in numbers:
			s+=int(no)
		print s
item=re.findall(r'<prod>.*</prod>',content,re.DOTALL|re.MULTILINE)
if(item):
	for it in item:
		numbers=re.findall(r'[0-9]+',it,re.DOTALL|re.MULTILINE)
		s=1
		for no in numbers:
			s*=int(no)
		print s
item=re.findall(r'<sub>.*</sub>',content,re.DOTALL|re.MULTILINE)
if(item):
	for it in item:
		numbers=re.findall(r'[0-9]+',it,re.DOTALL|re.MULTILINE)
		s=0
		for no in numbers:
			if(s==0):
				s=int(no)
			else:
				s-=int(no)
		print s
item=re.findall(r'<div>.*</div>',content,re.DOTALL|re.MULTILINE)
if(item):
	for it in item:
		numbers=re.findall(r'[0-9]+',it,re.DOTALL|re.MULTILINE)
		s=0
		for no in numbers:
			if(s==0):
				s=int(no)
			else:
				s/=int(no)
		print s
