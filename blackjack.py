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
    ases=0
    for carta in mano:
        valor = list(carta.keys())[0]
        if valor in figuras:
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


apuestas={1:5, 2:10, 3:25, 4:50, 5:100}
saldo=int(input("Ingrese la cantidad de fichas que quiere comprar: "))
fichas=int(input(" 1. 5 \n 2. 10 \n 3. 25 \n 4. 50 \n 5. 100 \n"))
if fichas in apuestas:
    apuesta_actual=apuestas[fichas]
    saldo=saldo-apuesta_actual
    print(f"Su saldo es: {saldo}")
    print(f"Usted aposto {apuesta_actual} fichas")

puntaje_jugador=calcular_mano(mano)
puntaje_dealer=calcular_mano(mano_d)     

print(f"Tu mano: {mano}")
print(f"Puntaje: {puntaje_jugador}")
print(f"El dealer muestra {mano_d[0]}")

def turno_jugador(saldo,apuesta_actual):
    puntaje_jugador = calcular_mano(mano)

    if puntaje_jugador==21:
        print(f"¡BlackJack! {puntaje_jugador}")
        saldo+=int(apuesta_actual*1.5)
        print(f"Su saldo es: {saldo}")
        return saldo,puntaje_jugador, apuesta_actual
    else:
        acciones=(int(input("Que quiere hacer? \n 1.Pedir \n 2.Plantarse \n 3.Doblar \n")))
        while True:
            if acciones == 3:
                if saldo>=apuesta_actual:
                    saldo-=apuesta_actual
                    apuesta_actual*=2
                    print(f"¡Dobló la apuesta a: {apuesta_actual}!")
                    n_carta=mazo.pop(0)
                    mano.append(n_carta)
                    descarte.append(n_carta)
                    puntaje_jugador=calcular_mano(mano)
                    print(f"Su mano: {mano} | Puntaje: {puntaje_jugador}")
                    if puntaje_jugador>21:
                        print(f"¡Bust! Usted pierde, su puntaje: {puntaje_jugador}")
                        print(f"Su saldo es: {saldo}")
                    break
            if acciones==1:
                n_carta=mazo.pop(0)
                mano.append(n_carta)
                descarte.append(n_carta)
                puntaje_jugador=calcular_mano(mano)
                print(f"Su mano: {mano} | Puntaje: {puntaje_jugador}")
                if puntaje_jugador>21:
                    print(f"¡Bust! Usted pierde, su puntaje: {puntaje_jugador}")
                    print(saldo)
                    break
                else:
                    acciones=(int(input("Que quiere hacer? \n 1.Pedir \n 2.Plantarse \n")))
            elif acciones==2:
                print(f"El jugador se planta con: {puntaje_jugador}")
                print("Esperar al turno del dealer...")
                break
            else:
                acciones=(int(input("Que quiere hacer? \n 1.Pedir \n 2.Plantarse \n")))
        return saldo,puntaje_jugador,apuesta_actual

def turno_dealer(mano_d,mazo,puntaje_dealer):
    puntaje_dealer=calcular_mano(mano_d)
    print(f"Mano del dealer: {mano_d} | Puntaje: {puntaje_dealer}")
    while puntaje_dealer <17:
        n_carta=mazo.pop(0)
        mano_d.append(n_carta)
        descarte.append(n_carta)
        puntaje_dealer=calcular_mano(mano_d)
        print(f"El dealer pide una carta... {mano_d} || {puntaje_dealer}")
        if puntaje_dealer >21:
            print(f"¡El dealer se pasa! {mano_d} | {puntaje_dealer}")
            return puntaje_dealer
    print(f"El dealer se planta con: {mano_d} | {puntaje_dealer}")    
    return puntaje_dealer


saldo, puntaje_jugador, apuesta_actual = turno_jugador(saldo,apuesta_actual)

if puntaje_jugador <21:
    puntaje_dealer = turno_dealer(mano_d,mazo,puntaje_dealer)
    if puntaje_dealer > 21:
        print(f"Usted gana con: {puntaje_jugador} ¡El dealer se pasa!")
        saldo+=apuesta_actual
        print(f"Su saldo actual es: {saldo}!")
    elif puntaje_dealer > puntaje_jugador:
        print(f"El dealer gana con: {puntaje_dealer}")
        print(f"Su nuevo saldo es: {saldo}")
    elif puntaje_jugador > puntaje_dealer:
        print(f"Usted gana con: {puntaje_jugador} ¡Felicidades!")
        saldo+=apuesta_actual
        print(f"Su saldo es: {saldo}")
    else: 
        print("Empate... se devuelve la apuesta")
        saldo+=apuesta_actual
else:
    print(f"Termina el juego porque el jugador tiene: {puntaje_jugador}")


    
    
    



