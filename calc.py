
'''import pickle
a='ram'
r=pickle.dumps(a)
print(r)#pickled representation

f=pickle.loads(r)
print(f) #unpickled representation'''

import pickle

f1=open('a2.txt','wb')
r=pickle.dump('ram',f1)
f1.close()

f1=open('a2.txt','rb')
s=pickle.load(f1)
print(s)
f1.close()


