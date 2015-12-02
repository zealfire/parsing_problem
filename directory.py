import os
import re
'''print os.getcwd()
print os.path.isfile('directory.py')
print os.listdir(os.getcwd())'''
file_name="browserstack-python-master"#raw_input()
direc=0
files=0
def formulate(file_name,flag):
	global direc,files
	for content in os.listdir(file_name):

		content=file_name+"/"+content
		if os.path.isfile(content) or (not os.path.isdir(content)):
			files+=1
			str1=""
			for j in range(flag):
				str1+="|   "
			for k in range(len(content)):
				if(content[k]=='/'):
					index=k
			print str1+"| -- "+content[index+1:]
		else:
			direc+=1
			str1=""
			for j in range(flag):
				str1+="|   "
			for k in range(len(content)):
				if(content[k]=='/'):
					index=k
			print str1+"| -- "+content[index+1:]
			formulate(content,flag+1)

if(os.path.isfile(file_name)):
	files+=1
	print "| -- "+file_name
	print "\n"
	print "%d directories, %d files"%(direc,files)
else:
	formulate(file_name,0)
	print "%d directories, %d files"%(direc,files)
