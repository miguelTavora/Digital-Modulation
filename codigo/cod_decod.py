import numpy as np


def criarTabelas (bits, vMax, typeQ):
    quantificacao = []
    decisao = []

    delta = (2.0*vMax)/2**bits

    if(typeQ == "midrise"):
        # 1o termo = vMax - delta/2
        decisao = np.arange (-vMax + delta, vMax + delta, delta) # Decisao
        quantificacao = np.arange (-vMax + (delta/2), vMax, delta) # Quantificao

    elif (typeQ == "midtread"):
        # 1o termo = vMax
        decisao = np.arange (-vMax + delta/2, vMax, delta)
        quantificacao = np.arange (-vMax + delta, vMax + delta, delta)
    else:
        print ("Erro")

    return quantificacao, decisao
    
def quantifica_sinal(sinal,nbits):
    
    vMax = np.max(sinal)
    niveis_quantizacao,niveis_decisao = criarTabelas(nbits, vMax, 'midrise')
    
    indices_quantizacao = lambda l : np.searchsorted(niveis_decisao,sinal)
    lista_indices_quantizacao = indices_quantizacao(sinal)
    
    valores_quantizados = lambda i : niveis_quantizacao[lista_indices_quantizacao]
    
    return (indices_quantizacao(sinal).astype(np.uint8),valores_quantizados(lista_indices_quantizacao))


def codificador(signal,R):

	#vai buscar os ultimos bits dependendo de R, adiciona 0 a esquerda aos que n chega ao valor R de bits
    bin_values= list(map(lambda x: np.binary_repr(x).zfill(R)[-R:],signal))


	#separa os bits de string para char tipo: '0101' -> '0','1','0','1'
    every_bit = np.array(list(map(lambda x: list(x),bin_values)))

	#transformar ndarray 2d em 1d
    d1_copy = every_bit.ravel()#pode ser ravel ou flatten(flatten cria uma copia, ravel aponta pra mesma memoria)

	#converter char pra int
    d1_copy = d1_copy.astype(np.uint8)

    return d1_copy

def cod_image(width,height,padding):

    st_width = np.array(list(np.binary_repr(width)))

    st_height = np.array(list(np.binary_repr(height)))

    pre_value = np.insert(padding,0,st_height)

    result = np.insert(pre_value,0,st_width).astype(np.uint8)

    return result


def descodifier(signal,nbits):
    number = 0

    #array para guardar os valores
    values = np.arange(len(signal)/nbits)

    #convete num array bidimensional
    signal_2d = np.reshape(signal,(-1,nbits))

    #dois ciclos para ir a cada posição e multiplicar por 2 o indice
    for n in range(len(signal_2d)):
        for i in range(len(signal_2d[0])):
             number=2*number+signal_2d[n][i]

        values[n] = number
        number = 0

    return values.astype(np.uint8)



def descodifica_sindroma(s,size):
    n=0
    
    int_value = np.arange(size)
    for i in range(len(s)):
        for j in range(4):
            n=2*n+s[i][j]
        int_value[i] = n
        n=0
    return int_value


def descod_numbers(number,division):
    num = 0
    num2 = 0
    values = [] 

    for i in range(len(number)-division):
        num=2*num+number[i]

    for l in range(len(number)-division,len(number)):
        num2=2*num2+number[l]

    values.append(num)
    values.append(num2)
    return values




def descod_number(number):
    num = 0

    for i in range(len(number)):
        num=2*num+number[i]

    return num










