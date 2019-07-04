from collections import defaultdict

print ("enter the number of alphabets in the lexographical order")
print ("enter those alphabets")
print ("enter the no. of strings you wush to give")
print ("enter the strings4")
n = int(input())
l=[]
d=defaultdict(list)
for i in range(0,n):
	k=input()
	l.append(k)
ans=[]
m = int(input())
for i in range(0,m):
	k=input()
	d[k[0]].append(k)
for ele in l:
	d[ele].sort()
	if(len(d[ele])>0):
		ans.append(d[ele])
print(ans)
