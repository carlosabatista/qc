import numpy as np
import math

#gen_angles(vetor de amplitudes): Dado um vetor com amplitudes de um estado desejável, retorna os ângulos de rotação Ry dos multiplexadores 
#angles_tree(vetor de angulos gerado por gen_angles): Dado um vetor de ângulos, imprime-o em camadas, dando ideia de árvore
#rnd_state_1quibt(): retorna um estado aleatório para um qubit 
#rnd_entangled_2qubits(): retorna um estado emaranhado de 2 qubits
#tensorproduct(qubitA, qubitB): realiza o produto tensorial de dois estados quaisquer
#simcircuit(quantum circuit): realiza a simulação de um circuito quântico, dvolvendo o histograma 


#Gera angulos baseado no vetor de estados
def gen_angles(x):
  N = len(x)
  n = math.log2(N)
  twopi = 2*np.pi
   
  angles=[]

  if (N>1):
    new_x=np.zeros(int(N/2), dtype=np.float64)
    for k in range(len(new_x)):
      new_x[k]=np.sqrt(x[2*k]**2+x[2*k+1]**2)
    auxia = gen_angles(new_x)
    if(auxia!=None):
      inner_angles=auxia
    for k in range(len(new_x)):
      if(new_x[k]!=0):
        if(x[2*k]>0):
          angles.append(2*math.asin(x[2*k+1]/new_x[k]))
        else:
          angles.append(2*math.pi-2*math.asin(x[2*k+1]/new_x[k]))
      else:
        angles.append(0)
    if(auxia!=None):
      #print(angles)
      angles=inner_angles+angles
      
    for i in range(len(angles)):
        while(angles[i]>=twopi):
            angles[i]=angles[i]-twopi
        while(angles[i]<0):
            angles[i]=angles[i]+twopi
      
    return angles


#Arvore de Angulos
def angles_tree(angles):

	N = len(angles)+1
	n = math.log2(N)
	indexalpha=0
	
	for i in range(int(n)):
		for j in range(2**(int(i))):
			print("alpha",indexalpha,angles[2**i+j-1])
			indexalpha+=1
		print()
		
	return 0
	

#Gera um qubit aleatório de valores reais
from random import *
def rnd_state_1qubit():
	a = random()
	b = np.sqrt(1-a)
	a = np.sqrt(a)
	
	rnd = random()
	sinal_a = 1
	if(rnd>=0.5):
		sinal_a = -1
	
	rnd = random()
	sinal_b = 1
	if(rnd>=0.5):
		sinal_b = -1

	a=sinal_a*a
	b=sinal_b*b
	
	return a,b

#Gera um estado de dois qubits emaranhados, tipo a|00>+b|11>

def rnd_entangled_2qubits():
	a = random()
	b = np.sqrt(1-a)
	a = np.sqrt(a)
	
	rnd = random()
	sinal_a = 1
	if(rnd>=0.5):
		sinal_a = -1
	
	rnd = random()
	sinal_b = 1
	if(rnd>=0.5):
		sinal_b = -1

	a=sinal_a*a
	b=sinal_b*b
	
	entang1 = [a,0,0,b]
	entang2 = [0,a,b,0]
	
	rnd_orig = random()
	rnd_entang = entang1
	if(rnd_orig>0.5):
		rnd_entang = entang2

	return rnd_entang

def tensorproduct(A,B):
  nt=[]
  for i in range(len(A)):
    for j in range(len(B)):
      aux = A[i]*B[j]
      nt.append(aux)
  return nt

from qiskit.visualization import plot_histogram
from qiskit import Aer, transpile

def simcircuit(qc):
	qc.measure_all()
	simular = Aer.get_backend('aer_simulator')
	circ=transpile(qc,simular)
	resultado = simular.run(circ).result()
	counts = resultado.get_counts(circ)
	titulo = "Probabilidades"
	plot_histogram(counts,title=titulo)
	return 0
