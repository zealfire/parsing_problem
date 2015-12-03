#writting sql queries
#http://www.geeksforgeeks.org/browserstack-interview-set-7-online-coding-questions/
import re
import shlex
#print "2014-10-23 11:55">"2014-10-23 11:54"
array=(raw_input().split(' '))
n=int(array[0])
m=int(array[1])
#print n
#print m

def remove_bad_substrings(s):
    badSubstrings = ["\""]
    for badSubstring in badSubstrings:
        s = s.replace(badSubstring, "")
    return s
column=raw_input()
columns=re.split(',',column)
columns=[remove_bad_substrings(s) for s in columns]#column.split(',')
#print columns
map={}
result_row=[]
def singlequery(query_size):
	global result_row
	left=query_size[0]
	operator=query_size[1]
	right=query_size[2]
	left_i=columns.index(left)
	for i in range(n):
		if(operator=='>'):
			if(map[i][left_i]>right):
				#print map[i][left_i]
				result_row.append(i)
		elif(operator=='<'):
			if(map[i][left_i]<right):
				result_row.append(i)
		else:
			if(map[i][left_i]==right):
				result_row.append(i)
	print len(result_row)

def resultand(query_size,conditions):
	print "hello"
def resultor(query_size,conditions):
	print "world"
for i in range(n):
	row=raw_input()
	map[i]=row.split(',')
	map[i]=[remove_bad_substrings(s) for s in map[i]]
	#print map
#print map
for j in range(m):
	query=raw_input()
	query_size=shlex.split(query)
	#print query_size
	query_size=[remove_bad_substrings(s) for s in query_size]
	length=len(query_size)
	conditions=length/3
	if(conditions>1):
		joining=query_size[3]
		if joining=='and':
			resultand(query_size,conditions)
		else:
			resultor(query_size,conditions)
	else:
		singlequery(query_size)

