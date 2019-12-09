def generate_identite(l):
    m=[]
    li=[]
    for i in range(0,l):
      for j in range(0,l):
         if(i==j):
	    li.append(1)
	 else:
	    li.append(0)
      m.append(li)
      li=[]
    return m

def inverse(e):
  def rowscaler(row,scaler):
     for m in range(0,len(row)):
        row[m]*=scaler
     return row
  if(len(e)==len(e[0])):
     mi=generate_identite(len(e))
     for j in range(0,len(e)):
	 for i in range(0,len(e)):
	     if(i==j):
	 	mi[j]=rowscaler(mi[j],1/float(e[j][j]))
		e[j]=rowscaler(e[j],1/float(e[j][j]))
	     else:
		p=e[j][j]
	        x=e[i][j]/float(p)	
		for k in range(0,len(e)):
		  e[i][k]-=x*e[j][k]
		  mi[i][k]-=x*mi[j][k]     
     return mi

def multipy(x,y):
    mat=[]
    if(len(x[0])==len(y)):
       for i in range(0,len(x)):
	  row=[]
       	  for j in range(0,len(y[0])):
	      sum=0
	      for k in range(0,len(y)):
	         sum+=x[i][k]*y[k][j]
	      row.append(sum)
	  mat.append(row)
       return(mat)
    else:
	print("can't multipy")

def transpose(e):
   for i in range(0,len(e)):
	for j in range(i,len(e[i])):
	   e[i][j],e[j][i]=e[j][i],e[i][j]
   return e;


def calculmoy(mat):
    moy=[]
    for i in range(len(mat[0])):
	sum=0
	for j in range(len(mat)):
	    sum+=mat[j][i][0]
	moy.append(sum/float(len(mat)))
    return moy


train=[[150,50],[160,60],[155,55],[167,65],[170,70],[180,70]]
target=[[2],[3],[2],[3],[3],[2.5]]

def fit(train,target):
   cpt=0
   results=[]
   dim=len(train[0])
   while cpt+dim-1<len(train):
      totrain=[train[cpt],train[cpt+1]]
      totarget=[target[cpt],target[cpt+1]]
      sol=multipy(inverse(totrain),totarget)
      results.append(sol)
      cpt=cpt+dim
   return calculmoy(results)

sol=fit(train,target)
sol=[sol]
print sol
def predict(sol,vect):
   result=multipy(sol,vect)
   return result
test=[[150],[50]]
print predict(sol,test)
