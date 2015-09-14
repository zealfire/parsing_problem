import re
fp=open("program.c","r")
content=fp.read()
sentences=re.split("\n",content)
final_content=[]
for sent in sentences:
	pattern1="^//.*"
	pattern3=".//.*"
	pattern2=".*//.*"
	if(re.findall(r"//.*",sent)):
		sent=re.sub("//.*","",sent,re.S|re.M)
	elif(re.findall(r'/[*]{1}.*[*]{1}/',sent)):
		sent=re.sub("/[*]{1}.*[*]{1}/","",sent)
	final_content.append(sent)

new_content="\n".join(final_content)
print new_content	
