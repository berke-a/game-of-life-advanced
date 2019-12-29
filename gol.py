import sys
import copy

mapp=sys.argv[1]
f = open(mapp, "r")
m = []
for line in f:
	elems = line.split()
	m.append(elems)
	mapp=m


u=[]
for i in mapp:
	a=''.join(i)
	c=[char for char in a] 
	u=u+[c]
mapp=u

gen=int(sys.argv[3])

rule=sys.argv[2]
f = open(rule, "r")
m = []
for line in f:
	elems = line.split()
	m.append(elems)
	rule=m

u=[]
for i in rule:
	a=''.join(i)
	c=[char for char in a] 
	u=u+[c]
rule=u


def rules(x,mapp,cop,row,col):
	if x[0]==mapp[row][col]:
		if x[1]=='=':
			if nei(row,col)==int(x[2]):
				cop[row][col]=x[3]
			else:
				pass
		elif x[1]=='<':
			if nei(row,col)<int(x[2]):
				cop[row][col]=x[3]
			else:
				pass
		elif x[1]=='>':
			if nei(row,col)>int(x[2]):
				cop[row][col]=x[3]
			else:
				pass
def nei(row,col):
	stack=''
	if len(mapp)==1 and len(mapp[0])==1:
		return 0
	elif row!=0 and col!=0 and row!=(len(mapp)-1) and col!=(len(mapp[0])-1):
		stack=mapp[row][col-1]+mapp[row][col+1]+mapp[row-1][col]+mapp[row-1][col-1]+mapp[row-1][col+1]+mapp[row+1][col]+mapp[row+1][col-1]+mapp[row+1][col+1]
		return stack.count('*')
	elif row==0 and col==0:
		stack=mapp[row][col+1]+mapp[row+1][col]+mapp[row+1][col+1]
		return stack.count('*')
	elif row==(len(mapp)-1) and col==(len(mapp[0])-1):
		stack=mapp[row][col-1]+mapp[row-1][col]+mapp[row-1][col-1]
		return stack.count('*')
	elif row==0 and col==(len(mapp[0])-1) :
		stack=mapp[row][col-1]+mapp[row+1][col]+mapp[row+1][col-1]
		return stack.count('*')
	elif row==(len(mapp)-1) and col==0:
		stack=mapp[row][col+1]+mapp[row-1][col]+mapp[row-1][col+1]
		return stack.count('*')
	elif row==0 and col!=0 and col!=(len(mapp[0])-1) :
		stack=mapp[row][col-1]+mapp[row][col+1]+mapp[row+1][col]+mapp[row+1][col-1]+mapp[row+1][col+1]
		return stack.count('*')
	elif row!=(len(mapp)-1) and row!=0 and col==0:
		stack=mapp[row][col+1]+mapp[row-1][col]+mapp[row-1][col+1]+mapp[row+1][col]+mapp[row+1][col+1]
		return stack.count('*')
	elif row==(len(mapp)-1) and col!=0 and col!=(len(mapp[0])-1) :
		stack=mapp[row][col-1]+mapp[row][col+1]+mapp[row-1][col]+mapp[row-1][col-1]+mapp[row-1][col+1]
		return stack.count('*')
	elif col==(len(mapp[0])-1) and row!=0 and row!=(len(mapp)-1):
		stack=mapp[row][col-1]+mapp[row-1][col]+mapp[row-1][col-1]+mapp[row+1][col]+mapp[row+1][col-1]
		return stack.count('*')

c=1
row=0
Rrow=0
col=0
ng=copy.deepcopy(mapp)
if gen!=0:
	while c<=gen:
		ng=copy.deepcopy(mapp)
		row=0
		while row<len(mapp):
			col=0
			while col<len(mapp[0]):
				Rrow=0
				while Rrow<len(rule):
					rules(rule[Rrow],mapp,ng,row,col)
					Rrow+=1
				col+=1
			row+=1
		c+=1
		mapp=copy.copy(ng)
else:
	mapp
e=[]
for i in mapp:
	e=e+i+['\n']
e.pop()
result=''
for q in e:
	result=result+''.join(q)
print result