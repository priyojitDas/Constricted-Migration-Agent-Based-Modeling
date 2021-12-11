import os, sys
import pandas as pd
import numpy as np

pp1, pp2 = float(sys.argv[1]), float(sys.argv[2])
probamid = float(sys.argv[3])
probamidb = float(sys.argv[3])

np.random.seed(8)

vboost = [0,np.random.uniform(0,1,1)[0],np.random.uniform(1,2,1)[0],np.random.uniform(2,3,1)[0],np.random.uniform(3,4,1)[0],np.random.uniform(2,3,1)[0],np.random.uniform(1,2,1)[0],np.random.uniform(0,1,1)[0],0]

os.system("python Main.py round1 "+str(pp1)+" "+str(pp2)+" "+str(probamid))

for i in xrange(2,11):
	if i == 2:
		df = pd.read_csv('round'+str(i-1)+".csv")
	else:
		df = pd.read_csv('round'+str(i-1)+"b.csv")
	p1, p2, p3 = df.iloc[df.shape[0]-1,8], df.iloc[df.shape[0]-1,9], df.iloc[df.shape[0]-1,10]
	pp1, pp2 = p1/float(p1+p2+p3), p2/float(p1+p2+p3)
	probamidb += 0.005 * vboost[i-2] * 0.1 * 9 #(4 - np.abs(11 - i - 5)) * 0.1 * 9
	print "Bottom",i,pp1,pp2
	os.system("python Main.py round"+str(i)+"b "+str(pp1)+" "+str(pp2)+" "+str(probamidb))

for i in xrange(2,11):
	if i == 2:
		df = pd.read_csv('round'+str(i-1)+".csv")
	else:
		df = pd.read_csv('round'+str(i-1)+"t.csv")
	p1, p2, p3 = df.iloc[df.shape[0]-1,5], df.iloc[df.shape[0]-1,6], df.iloc[df.shape[0]-1,7]
	pp1, pp2 = p1/float(p1+p2+p3), p2/float(p1+p2+p3)
	print "Top",i,pp1,pp2
	os.system("python Main.py round"+str(i)+"t "+str(pp1)+" "+str(pp2)+" "+str(probamid))
