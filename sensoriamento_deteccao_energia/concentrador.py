
arq = open('/home/daniel/Gnuradio_Workspace/sensoriamento_deteccao_energia/dados.txt', 'r')
texto = arq.readlines()
cont = 0
for i in range(len(texto)):
    if ( 'canal ocupado' in texto[i]):
        cont += 1
print("Probabilidade de deteccao = ",cont/len(texto))
arq.close()