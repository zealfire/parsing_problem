import re
#removes all comment in a program
fp=open("program.c","r")
content=fp.read()
content=re.sub(re.compile("/\*.*\*/",re.DOTALL ) ,"" ,content)
content=re.sub(re.compile(r"//.*") ,"" ,content)
content=re.sub(re.compile(r"[\n](\s){1,}[\n]",re.DOTALL|re.MULTILINE) ,"\n" ,content)
print content

