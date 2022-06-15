def arredonda(num: float, casas:int=2):
    pot10 = 10 ** casas
    return round(num * pot10) / pot10



def calcula_pu(VF: float, prazo_anual: float, taxa_anual: float) -> float:
    ''' Calcula o PU 
    VF: float
    prazo_anual: float
    taxa_anual: float

    retorno:
    PU: float
    '''
    return VF / ((1 + taxa_anual)**(prazo_anual))


# Teste
VF = 48.81
prazo_anual = 13/252
taxa_anual = 0.1265
resultado_previsto = 48.51

teste = round(calcula_pu(VF,prazo_anual,taxa_anual)*100)/100 == resultado_previsto
print(f'Resultado: {resultado}')
