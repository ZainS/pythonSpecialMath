import sys

def specialMath(n):
	ls= [0,1]
	for i in range(2,n+1):
		ls.append(ls[i-1]+ls[i-2])
	return ls[-1]
print(specialMath(int(sys.argv[1])))