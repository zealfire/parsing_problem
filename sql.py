#writting sql queries
#http://www.geeksforgeeks.org/browserstack-interview-set-7-online-coding-questions/
import re
import shlex
array=(raw_input().split(' '))
n=int(array[0])
m=int(array[1])

def remove_bad_substrings(s):
    badSubstrings = ["\""]
    for badSubstring in badSubstrings:
        s = s.replace(badSubstring, "")
    return s
column=raw_input()
columns=re.split(',',column)
columns=[remove_bad_substrings(s) for s in columns]
map={}
result_row=[]
def singlequery(query_size,result_row):
	new_result_row=[]
	left=query_size[0]
	operator=query_size[1]
	right=query_size[2]
	left_i=columns.index(left)
	for i,val in enumerate(result_row):
		if(operator=='>'):
			#print map[val][left_i]
			#print right
			if(map[val][left_i]>right):
				#print "hello"
				new_result_row.append(val)
		elif(operator=='<'):
			if(map[val][left_i]<right):
				new_result_row.append(val)
		else:
			if(map[val][left_i]==right):
				new_result_row.append(val)
	result_row=new_result_row
	return result_row

def resultand(query_size,conditions,result_row):
	i=0
	j=1
	#print conditions
	while 1:
		if j>conditions:
			return result_row
		query_size1=[]
		query_size1.append(query_size[i])
		query_size1.append(query_size[i+1])
		query_size1.append(query_size[i+2])
		result_row=singlequery(query_size1,result_row)
		i+=4
		j+=1
def resultor(query_size,conditions,result_row):
	''''''

for i in range(n):
	row=raw_input()
	map[i]=row.split(',')
	map[i]=[remove_bad_substrings(s) for s in map[i]]
for j in range(m):
	query=raw_input()
	query_size=shlex.split(query)
	#print query_size
	query_size=[remove_bad_substrings(s) for s in query_size]
	length=len(query_size)
	conditions=length/3
	if(conditions>1):
		result_row=range(n)
		joining=query_size[3]
		if joining=='and':
			print len(resultand(query_size,conditions,result_row))
		else:
			resultor(query_size,conditions,result_row)
	else:
		result_row=range(n)
		print len(singlequery(query_size,result_row))

