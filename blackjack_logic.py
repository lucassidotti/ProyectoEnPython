import random
def crear_mazo():
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
    return mazo

FIGURAS=['J','Q','K']

def barajar(mazo):
    random.shuffle(mazo)
    
    mano=[]
    mano_d=[]
    descarte=[]

    for _ in range(2):
        carta=mazo[0]
        mano.append(carta)
        descarte.append(mazo.pop(0))
        carta_d=mazo[0]
        mano_d.append(carta_d)
        descarte.append(mazo.pop(0))
    return mazo, mano, mano_d, descarte

def calcular_mano(mano):
    parcial=0
    ases=0
    for carta in mano:
        valor = list(carta.keys())[0]
        if valor in FIGURAS:
            parcial+=10
        elif valor=='A':
            parcial+=11
            ases+=1
        else:
            parcial+=valor
    while parcial >21 and ases >0:
        parcial-=10
        ases-=1
    return parcial

def apuestas_jugador(saldo,fichas):
    apuestas = {1:5, 2:10, 3:25, 4:50, 5:100}
    if fichas in apuestas:
        apuesta_actual=apuestas[fichas]
        saldo=saldo-apuesta_actual
        return saldo, apuesta_actual 
    
def black_jack_n(saldo, apuesta_actual,mano,mano_d):
    puntaje_jugador = calcular_mano(mano)
    puntaje_dealer = calcular_mano(mano_d)
    resultado = ""
    if puntaje_jugador==21 and len(mano)==2:
        if puntaje_dealer==21 and len(mano_d)==2:
            saldo += apuesta_actual
            resultado="empate"
        else:
            saldo+=int(apuesta_actual*2.5)
            resultado="blackjack"
    return saldo,puntaje_jugador,apuesta_actual, resultado

def pedir(mano,mazo,descarte):
    n_carta=mazo.pop(0)
    mano.append(n_carta)
    descarte.append(n_carta)
    puntaje_jugador=calcular_mano(mano)
    return mano,mazo,descarte,puntaje_jugador
    
def doblar(saldo,apuesta_actual,mano,mazo,descarte):
    saldo-=apuesta_actual
    apuesta_actual*=2
    n_carta=mazo.pop(0)
    mano.append(n_carta)
    descarte.append(n_carta)
    puntaje_jugador=calcular_mano(mano)
    return saldo,apuesta_actual,mano,mazo,descarte,puntaje_jugador           

def plantarse():
    return True

def turno_dealer(mano_d,mazo,descarte):
    puntaje_dealer=calcular_mano(mano_d)
    while puntaje_dealer <17:
        n_carta=mazo.pop(0)
        mano_d.append(n_carta)
        descarte.append(n_carta)
        puntaje_dealer=calcular_mano(mano_d)
        if puntaje_dealer >21:
            break
    return puntaje_dealer

def jugadas(saldo,mano_d,mazo,apuesta_actual,mano,descarte):
    puntaje_dealer=calcular_mano(mano_d)
    puntaje_jugador=calcular_mano(mano)
    resultado = ""

    if puntaje_jugador > 21:
        resultado = "pierde"
        return saldo, puntaje_jugador,puntaje_dealer, resultado
    
    puntaje_dealer = turno_dealer(mano_d,mazo,descarte)

    if puntaje_dealer > 21:
        saldo += apuesta_actual *2
        resultado="gana"
    elif puntaje_jugador> puntaje_dealer:
        saldo += apuesta_actual *2
        resultado="gana"
    elif puntaje_dealer > puntaje_jugador:
        resultado="pierde"
    else: 
        saldo += apuesta_actual
        resultado="empate"
    return saldo, puntaje_jugador, puntaje_dealer, resultado








