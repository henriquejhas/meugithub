'''try:

    f = open('lotofacil.txt', 'r')

except:
    print('Deu erro')
else:
    jogos = f.readlines()
    print(jogos[0].replace('\n','').split('\t'))
    contar = 0
    for i, jogo in enumerate(jogos):
        contar += 1
        jogos[i] = jogos[i].replace('\n','').split('\t')
        #print(i,jogos[i])
        #if contar >= 10:
        #    break
    print(jogos[1000])
    
finally:
    f.close()

'''

try:

    f = open('dadosTrades1.txt', 'r')

except:
    print('Deu erro')
else:
    trades = f.readlines()
    
    for i, trade in enumerate(trades): 
        lista = trade.split(' ')
        trades[i] = str(lista[4])
        
    
    
finally:
    f.close()


try:
    f = open('dadosTradesFormatados.txt', 'a')
    
except:
    print('Deu erro')
else:
    f.write('tipo,hora,mediaM1,mediaM5,mediaM15,volumeM1,volumeM5,volumeM15,rsiM1,rsiM5,rsiM15,resultado\n')
    f.writelines(trades)

finally:
    f.close()


