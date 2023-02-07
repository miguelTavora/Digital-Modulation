import numpy as np
from PIL import Image
from scipy import special
from cod_decod import quantifica_sinal
from cod_decod import codificador
from cod_decod import descodifier
from cod_decod import descod_number
from cod_decod import cod_image
from cod_decod import descod_numbers
from ham import hamming
from ham import error_dectetion_correction
from ex1 import modulation_QPSK
from ex1 import demodulation_QPSK
from ex1 import AWGN_channel
from desquantify import cria_dicionario
from desquantify import desquantifica
import time

start_time = time.time()

##################### ############################### ##################



################## #############  EX5   ##############  ################

def calculate_error(signal, original):

    error = np.arange(len(signal),dtype =np.float64)

    for a in range(len(signal)):
        error[a] = signal[a]-original[a]

    return error


def SNR_calculater(signal, original):

    error_index =  calculate_error(signal, original)

    Px = np.sum(np.power(signal,2))/len(signal)

    Peq = np.sum(np.power(error_index,2))/len(signal)

    SNR = 10*np.log10(Px/Peq)

    return SNR



def SNR_teorical(signal, nbits):

    Px = np.sum(np.power(signal,2))/len(signal)

    SNR = 6.02*nbits + 10*np.log10((3*Px)/(max(signal)**2))

    return SNR


def calculate_BER(signal,original):
    
    count = 0

    signal = signal.astype(np.int8)
    original = original.astype(np.int8)

    for a in range(len(signal)):
        if(signal[a] - original[a] != 0):
            count += 1

    result = count/len(signal)

    return result

def QPSK_BER(signal, eb, n0):

	ber = 0.5*special.erfc(np.sqrt((eb/n0)))

	return ber



#np.set_printoptions(threshold=np.inf)

# emissor
im_inicial = Image.open("lena_color.tif")
largura, altura = im_inicial.size

#converter num np.array
a = np.array(im_inicial)
b = a.flatten()


#quantificação
index ,valores = quantifica_sinal(b,10)
#criação dicionário para desquantificação
dicionario = cria_dicionario(index,valores)


#codificação
cod = codificador(index,8)


#modulação QPSK
mod = modulation_QPSK(cod,8,1)


#Canal AWGN
noise_mod = AWGN_channel(mod,2)


#desmodelador QPSK
demod = demodulation_QPSK(noise_mod,8,1)


ber_depois = calculate_BER(demod,cod)
print("BER sem correção erros: ",ber_depois)

#descodificador
decod = descodifier(demod,8)

#desquantificação
desq = desquantifica(decod,dicionario)


print("--- %s seconds ---" % (time.time() - start_time))


















