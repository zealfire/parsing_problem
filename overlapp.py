import re
sample_text="aaaaaannndnnnnnnfffhfhhgjjjwkkkllclc"
#still need to generalize this
list1=[w for w in re.finditer(r'(?=(a{2,2}))',sample_text)]
print len(list1)#.size()#(list)
list1=[w for w in re.finditer(r'(?=(n{4}))',sample_text)]
print len(list1)
list1=[w for w in re.finditer(r'(?=(a{5,}))',sample_text)]
print len(list1)
list1=[w for w in re.finditer(r'(?=(an{2,2}))',sample_text)]
print len(list1)
list1=[w for w in re.finditer(r'(?=(a{2}d{2}))',sample_text)]
print len(list1)
#list=re.findall(r'(?=aa)',sample_text)
#for i in list1:
#	print i.group(1)
