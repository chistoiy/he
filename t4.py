import datetime,time,random

def hex36(num:int):
	print(type(num))
	num = int(num)
	key='qwertyuiopasdfghjklzxcvbnm1234567890'
	a = []
	while num != 0:
		C = int(num%36)
		a.append(key[C])
		num = num/36
	a.reverse()
	out = ''.join(a)
	return out
	
	
print(hex36(1233))
	