import random

def findCycle(d):
  cycle=list()
  newStart=random.choice(list(d.keys()))
  cycle.append(newStart)
  
  while(d!={}):
    #print(newStart)
    if newStart in d.keys():
      if len(d[newStart])==1:
        x=d[newStart][0]
        cycle.append(x)
        d.pop(newStart)
        newStart=x
      else: 
        x=random.choice(list(d[newStart]))
        cycle.append(x)
        d[newStart].remove(x)
        if len(d[newStart])==0: d.pop(newStart)
        newStart=x
        
    if len(cycle)>1 and cycle[0]==cycle[-1]:
      break
  
  return d, cycle

def merge(lista1,lista2):
  for i in lista1:
    if i in lista2:
      index_of_i=lista2.index(i)
      reorder1=lista1[lista1.index(i):]+lista1[1:lista1.index(i)+1]
      newCycle=lista2[:lista2.index(i)]+reorder1+lista2[lista2.index(i)+1:]
      break
  return newCycle

def combine(d,sp):
  while(len(sp)>1):
    for key in d.keys():
      sp_index=[]
      for i in range (len(sp)):
        if int(key) in sp[i]:
          sp_index.append(i)
          if len(sp_index)==2:
            newCycle=merge(sp[sp_index[0]],sp[sp_index[1]])
            sp.pop(sp_index[1])
            sp.pop(sp_index[0])
            sp.append(newCycle)
            break
  return sp

def eulerianCycle(lista):
  d=dict()
  cvalues=0
  
  smallerCycles=list()
  for l in lista:
    d[l.split(' -> ')[0]]=list(l.split(' -> ')[1].split(','))
    cvalues+=len(d[l.split(' -> ')[0]])
  dcopy=d.copy()
  while (d!={}):
    dp=findCycle(d)
    d=dp[0]
    smallerCycles.append(dp[1])
  
  if len(smallerCycles)==1:
    return smallerCycles[0]
  else:
    merged=combine(dcopy, smallerCycles)
  return merged


if __name__=="__main__":
  edges=[]
  with open("C:/Users/Y530/Downloads/rosalind_ba3f.txt", "r") as f:
    for line in f.readlines():
        edges.append(line.strip())
  res=eulerianCycle(edges)
  print(*res, sep=' -> ', file=open("output.txt","w"))
  print('done')