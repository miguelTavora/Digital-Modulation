import numpy as np

#so resulta para 4
def modulation_QPSK(signal,npoints,eb):

	continous = np.arange(len(signal)*int(npoints/2),dtype = np.float64)

	time = np.arange(npoints)
	amplitude = np.sqrt(eb*2)

	#criar cossenos para cada fase possível
	coss = amplitude*np.cos(((2*np.pi)/npoints)*time+(np.pi/4))
	coss1 = amplitude*np.cos(((2*np.pi)/npoints)*time+(np.pi-np.pi/4))
	coss2 = amplitude*np.cos(((2*np.pi)/npoints)*time+(np.pi+np.pi/4))
	coss3 = amplitude*np.cos(((2*np.pi)/npoints)*time+(-np.pi/4))
	
	#atribuição dos npoints dos cossenos para cada conjunto 2 bits
	for a in range(int(len(signal)/2)):
		if(signal[a*2] == 0 and signal[a*2+1] == 0):
			continous[a*npoints:a*npoints+npoints] = coss[:]

		elif(signal[a*2] == 0 and signal[a*2+1] == 1):
			continous[a*npoints:a*npoints+npoints] = coss1[:]

		elif(signal[a*2] == 1 and signal[a*2+1] == 0):
			continous[a*npoints:a*npoints+npoints] = coss2[:]

		else:
			continous[a*npoints:a*npoints+npoints] = coss3[:]

	return continous



def demodulation_QPSK(signal,npoints,eb):

	iteration = int(len(signal)/npoints)

	discrete = np.zeros(int(len(signal)/int((npoints/2))),dtype=np.uint8)

	phase = np.array([[0,0],[0,1],[1,0],[1,1]],dtype=np.uint8)

	n = np.arange(0,npoints)

	#sen e con generico para multiplicar
	cs = np.cos(((2*np.pi)*n/npoints))
	cs2 = np.sin(((2*np.pi)*n/npoints))

	for c in range(iteration):
		#buscar o npoints do sinal multiplicar pelo sen e cos generico
		#final sumar tudo e verificar a fase
		y = signal[c*npoints:c*npoints+npoints]
		ci = np.dot(cs,y)
		si = np.dot(cs2,y)

		s1 = np.sum(si*np.sqrt(2*eb))
		c1 = np.sum(ci*np.sqrt(2*eb))

		if(s1 > 0 and  c1 > 0):
			discrete[c*2:c*2+2] = phase[3]

		elif(s1 > 0 and c1 < 0 ):
			discrete[c*2:c*2+2] = phase[2]

		elif(s1 < 0 and c1 < 0 ):
			discrete[c*2:c*2+2] = phase[1]

		elif(s1< 0 and c1 > 0 ):
			discrete[c*2:c*2+2] = phase[0]

		else:
			print("erro")

	return discrete


def AWGN_channel(signal,noise):
	#o np.random.randn retorna um array e para cada valor do QPSK é adicionado o valor do ruido
	return signal + np.sqrt(noise) * np.random.randn(len(signal))



