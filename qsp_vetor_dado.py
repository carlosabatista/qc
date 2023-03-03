from qsp_v1 import *
import numpy as np
from random import *

#V = [1/np.sqrt(2),0,0,0,0,0,0,1/np.sqrt(2)]
n=8
A=[]
B=[]
for i in range(n):
	A.append(random())
	B.append(random())

SA = np.sum(A)
SB = np.sum(B)

VA = A/SA
VB = B/SB

A = np.sqrt(VA)
B = np.sqrt(VB)




print("A = ",A)

print("B = ",B)

V = tensorproduct(A,B)

print("V = ",V)

Angulos = gen_angles(V)

print("Árvore de Ângulos")
angles_tree(Angulos)