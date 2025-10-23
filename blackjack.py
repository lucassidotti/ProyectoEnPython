import random
mazo = [
  {2: 'corazones'}, {3: 'corazones'}, {4: 'corazones'}, {5: 'corazones'}, {6: 'corazones'},
  {7: 'corazones'}, {8: 'corazones'}, {9: 'corazones'}, {10: 'corazones'}, {'J': 'corazones'},
  {'Q': 'corazones'}, {'K': 'corazones'}, {'A': 'corazones'},

  {2: 'picas'}, {3: 'picas'}, {4: 'picas'}, {5: 'picas'}, {6: 'picas'},
  {7: 'picas'}, {8: 'picas'}, {9: 'picas'}, {10: 'picas'}, {'J': 'picas'},
  {'Q': 'picas'}, {'K': 'picas'}, {'A': 'picas'},

  {2: 'trebol'}, {3: 'trebol'}, {4: 'trebol'}, {5: 'trebol'}, {6: 'trebol'},
  {7: 'trebol'}, {8: 'trebol'}, {9: 'trebol'}, {10: 'trebol'}, {'J': 'trebol'},
  {'Q': 'trebol'}, {'K': 'trebol'}, {'A': 'trebol'},

  {2: 'diamantes'}, {3: 'diamantes'}, {4: 'diamantes'}, {5: 'diamantes'}, {6: 'diamantes'},
  {7: 'diamantes'}, {8: 'diamantes'}, {9: 'diamantes'}, {10: 'diamantes'}, {'J': 'diamantes'},
  {'Q': 'diamantes'}, {'K': 'diamantes'}, {'A': 'diamantes'}
]

figuras=['J','Q','K']
valores_numericos = [2,3,4,5,6,7,8,9,10]
mano=[]
mano_d=[]
descarte=[]
def barajar():

    random.shuffle(mazo)
    
    for _ in range(2):
        carta=mazo[0]
        mano.append(carta)
        descarte.append(mazo.pop(0))
        carta_d=mazo[0]
        mano_d.append(carta_d)
        descarte.append(mazo.pop(0))
    return
barajar()

def calcular_mano(mano):
    parcial=0
    for carta in mano:
        valor = list(carta.keys())[0]
        if valor in figuras:
            puntaje=10
            parcial+=puntaje
        elif valor in valores_numericos:
            puntaje=valor
            parcial+=puntaje
        if valor == 'A':
            if parcial <= 10:
                puntaje = 11
                parcial += puntaje
            else:
                puntaje = 1       
    return parcial

puntaje_jugador=calcular_mano(mano)
puntaje_dealer=calcular_mano(mano_d)     

        

    




print(mano)
print(puntaje_jugador)
print(mano_d)
print(puntaje_dealer)
print(descarte)
