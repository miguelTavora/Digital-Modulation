import numpy as np
from matplotlib import pyplot as plt
from ex1 import modulation_QPSK
from ex1 import demodulation_QPSK
from ex1 import AWGN_channel
import time

start_time = time.time()

def show_graph(signal):

	value = modulation_QPSK(signal,200,100)

	plt.plot(value)

	plt.show()


def compare_with(sign,sign_noise):
	count = 0

	for a in range(len(sign)):
		if(sign[a] ==  sign_noise[a]):
			count+= 1

	return count


np.set_printoptions(threshold=np.inf)



#show_graph([0,0,0,1,1,0,1,1])

##################### ############################### ##################



################## #############  EX4   ##############  ################

bin_sequence = [0,1,1,0,1,1,0,0]

ex_mod = modulation_QPSK(bin_sequence,8,1)

ex_mod_channel= AWGN_channel(ex_mod,1e-1)

ex_demod = demodulation_QPSK(ex_mod_channel,8,1)

compare_1 = compare_with(bin_sequence,ex_demod)

print("Número de valores iguais em 8 para Ruído de 1e-1:",compare_1)


#################################################

ex_mod_channel_1= AWGN_channel(ex_mod,0.5)

ex_demod_1 = demodulation_QPSK(ex_mod_channel_1,8,1)

compare_2 = compare_with(bin_sequence,ex_demod_1)

print("Número de valores iguais em 8 para Ruído de 0.5:",compare_2)


#################################################

ex_mod_channel_2= AWGN_channel(ex_mod,1)

ex_demod_2 = demodulation_QPSK(ex_mod_channel_2,8,1)

compare_3 = compare_with(bin_sequence,ex_demod_2)

print("Número de valores iguais em 8 para Ruído de 1:",compare_3)

#################################################

ex_mod_channel_3= AWGN_channel(ex_mod,2)

ex_demod_3 = demodulation_QPSK(ex_mod_channel_3,8,1)

compare_4 = compare_with(bin_sequence,ex_demod_3)

print("Número de valores iguais em 8 para Ruído de 1:",compare_4)



print("--- %s seconds ---" % (time.time() - start_time))


















