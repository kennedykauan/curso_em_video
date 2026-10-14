import moeda
import dado


valor = dado.leiadinheiro('Digite um valor R$ ').replace(',', '.')
print(valor)
moeda.resumo(valor)