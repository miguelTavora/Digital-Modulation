import numpy as np
from cod_decod import codificador
from cod_decod import descodifica_sindroma

Tabela={
0:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
12:[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
10:[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
9:[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
6:[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
5:[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
3:[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
14:[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],
13:[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
11:[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
7:[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
15:[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
8:[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
4:[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
2:[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
1:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
}


def hamming(mensagem):
        l=[11-len(mensagem)%11]
        P= np.array([[1,1,0,0],[1,0,1,0],[1,0,0,1],[0,1,1,0],[0,1,0,1],[0,0,1,1],[1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1],[1,1,1,1]])
        l=codificador(l,4)
      
        G= np.hstack((np.eye(11),P))
        
        if(len(mensagem)%11!=0):mensagem= np.pad(mensagem,(0,(11-len(mensagem)%11)),'constant')
        
        mensagem = np.reshape(mensagem,(-1,11))
        hamming = list(np.arange(len(mensagem)))
      
        for m in range(len(mensagem)):
                hamming[slice(m*15,m*15+15,1)] = (np.dot(mensagem[m],G)%2)

        hamming=np.insert(hamming,0,l).astype('uint8')
        return hamming


        
	
def error_dectetion_correction(signal,bitsremove):
        

        signal=np.reshape(np.array(signal),(-1,15))

        sindroma = np.arange(len(signal)*4,dtype="uint8")

        P= np.array([[1,1,0,0],[1,0,1,0],[1,0,0,1],[0,1,1,0],[0,1,0,1],[0,0,1,1],[1,1,1,0],[1,1,0,1],[1,0,1,1],[0,1,1,1],[1,1,1,1]])
        G= np.hstack((np.matrix.transpose(P),np.eye(4,dtype=np.uint8)))
        G=np.matrix.transpose(G)
        
        for s in range(len(signal)):
                
                sindroma[slice(s*4,s*4+4,1)] = (np.dot(signal[s],G)%2)

        sindroma = np.reshape(sindroma,(-1,4))
        
        valores=descodifica_sindroma(sindroma,len(sindroma))

        padroes=(list(map(lambda x:Tabela[x],valores)))
        
        sinal_final=(list(map(lambda x,y:np.bitwise_xor(x,y),signal,padroes)))

        sem_sindroma =  np.arange(len(sinal_final)*11)

        for n in range(len(sinal_final)):
                sem_sindroma[slice(n*11,n*11+11,1)] = sinal_final[n][:11]

        
        remove_bits = sem_sindroma[:len(sem_sindroma)-bitsremove]
        
        return remove_bits
        

