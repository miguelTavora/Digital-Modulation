import numpy as np


def cria_dicionario(indices, valores):

	Dict = {}

	for a in range(len(indices)):
		if indices[a] in Dict.keys():
			continue
		else:
			Dict[indices[a]] = valores[a]

	return Dict


def desquantifica(indices, dicionario):

	result = np.zeros(len(indices))

	for a in range(len(indices)):
		result[a] = dicionario.get(indices[a])

	return result.astype(np.uint8)











