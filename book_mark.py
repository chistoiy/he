import re
s = 'asdfghjklsdfhjkl'
import json
import re,copy
#   '<DL><p>','DT><H3','<DT><A',
li = []
dic ={}
l2 = []
l3 = []
def ccc(s):
	#r ='HREF="(.*)"\s.*">(.*)</'
	r = 'HREF="(.*?)".*>(.*)</'
	ret = re.findall(r,s)[0]
	return list(ret)
with open(r'C:\Users\changshi\Desktop\bookmark-2018-11-27.html','r',encoding='utf-8') as f:
	lines = re.findall('<DL><p>.*|<DT><H3.*|<DT><A.*|</DL><p>.*', f.read(),)
	
	for index,i in enumerate(lines):
		if index==len(lines)-1:
			li.pop(0)
			li.pop(-1)
			for jndex,j in enumerate(li):
				if not isinstance(j,dict):
					li[jndex]=ccc(j) #...
			
			break
		li.append(i)
		
		if i.startswith('</DL'):
			#print('aaa')
			li.pop()
			while isinstance(li[-1],dict):
				l2.append(li.pop())
			while li[-1].startswith('<DT><A'):
				l2.append(li.pop())
				#print(li)
			 
			if li[-1].startswith('<DL><p>'):
				li.pop()
			if li[-1].startswith('<DT><H3'):
				#x = re.findall('>(.+)</H3',li.pop())
				x = re.findall('<H3.*>(.+?)</H3',li.pop())
				 
				#print(l2)
				l2.reverse()
				for i in l2:
					#print(ccc(i))
					if isinstance(i,dict):
						l3.append(i)
						continue
					l3.append(ccc(i))
					
				dic[x[0]]=copy.deepcopy(l3)
				li.append(copy.copy(dic))
				l2.clear()
				l3.clear()
				dic.clear()
print(li)
			

with open('book.json','w',encoding='utf-8')as f:
	f.write(json.dumps(li,ensure_ascii=False))
with open('book_title.txt','w',encoding='utf-8')as p:
	for i in li :
		if isinstance(i,dict):
			p.write(str(i.keys()))
	p.write('/n')
	p.write(str(li))