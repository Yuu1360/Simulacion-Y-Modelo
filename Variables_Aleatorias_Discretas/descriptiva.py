import math

def bernoulliExtito(pExito):
    return pExito

def bernoulliFracaso(pExito):
    return 1 - pExito

def binomial(nEnsayos, nExitos, pExito):
    return math.factorial(nEnsayos)/(math.factorial(nExitos)*math.factorial(nEnsayos-nExitos))*pExito**nExitos*(1-pExito)**(nEnsayos-nExitos)

def geometrica(pExito, primerExito):
    return (1-pExito)**(primerExito-1)*pExito

def poisson(nConcurrenciasUnidadTiempo, nTiempo):
    return ((nConcurrenciasUnidadTiempo**nTiempo)*(math.e**-nConcurrenciasUnidadTiempo))/math.factorial(nTiempo)

if __name__ == "__main__":
    print(binomial(4, 3, 0.8))
    print(geometrica(0.80, 2))
    print(poisson(5, 3))