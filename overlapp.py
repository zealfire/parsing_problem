import re
t=int(raw_input())
sample_text1=raw_input()
#sample_text1="aaaaaannndnnnnnnfffhfhhgjjjwkkkllclc"
sample_text=[]
for i in range(t):
	string=raw_input()
	sample_text=[]
	for j in range(len(string)):
		if(ord(string[j])>=97 and ord(string[j])<=122):
			#print ord(string[j])
			sample_text.append(string[j])
		elif(string[j]=='+'):
			ch=sample_text.pop()
			for k in range(4):
				sample_text.append(ch)
		elif(string[j]=='.'):
			ch=sample_text.pop()
			#print ch
			for k in range(2):
				sample_text.append(ch)
		elif(string[j]=='*'):
			sample_text.append('{')
			sample_text.append('5')
			sample_text.append(',')
			sample_text.append('}')
	pattern=''.join(sample_text)
	#print pattern
	k=re.compile(r'(?=(%s))'%pattern)
	list1=[w for w in k.finditer(sample_text1)]
	print len(list1)
