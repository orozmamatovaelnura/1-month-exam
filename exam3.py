def add_elements(li):
  li.insert(0,'Element')
  li.insert(1,'start')
  li.append('finish')
  return li

def new_dict(*args):
  e=1
  chisla={}
  for i in args:
    chisla[i]=e
    e+=1
  return chisla



def lamb(cort):
  cort=list(cort)
  b=[]
  a=filter(lambda x: x%2==0, cort)
  for i in cort:
    d=lambda u: u**2
    b.append(d(i))
  return list(a),b
a,b=lamb((1,2,3,4,5))