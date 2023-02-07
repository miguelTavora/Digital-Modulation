import numpy as np
from PIL import Image
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


#np.set_printoptions(threshold=np.inf)

# emissor
im_inicial = Image.open("lena_color.tif")
largura, altura = im_inicial.size

#converter num np.array
a = np.array(im_inicial)
b = a.flatten()
print("tamanho de b",len(b))
print("primeiros 20 valores",b[0:20])


#quantificação
index ,valores = quantifica_sinal(b,12)
#criação dicionário para desquantificação
dicionario = cria_dicionario(index,valores)


#codificação
cod = codificador(index,8)
print("tamanho de cod",len(cod))


#hamming 15x11
ham = hamming(cod)
hed = cod_image(largura,altura,ham[0:4])



#modulação QPSK
mod = modulation_QPSK(ham[4:],8,1)

#canal AWGN 
noise_mod = AWGN_channel(mod,1e-1)


#desmodelador QPSK
demod = demodulation_QPSK(noise_mod,8,1)


#correção erros
padding = descod_number(hed[len(hed)-4:len(hed)])
error_correction = error_dectetion_correction(demod,padding)

#descodificador
decod = descodifier(error_correction,8)

#desquantificação
desq = desquantifica(decod,dicionario)

#criação imagem
image_shape = descod_numbers(hed[0:20],10)
image_final = Image.fromarray(np.reshape(desq,(image_shape[0],image_shape[1],3)))
image_final.save("noisy_lena.bmp")



print("--- %s seconds ---" % (time.time() - start_time))


















