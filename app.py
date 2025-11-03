from flask import Flask, render_template, session, redirect, url_for, request
from blackjack_logic import crear_mazo, barajar, calcular_mano, apuestas_jugador, black_jack_n, pedir, doblar, plantarse, turno_dealer, jugadas

app =Flask(__name__)
app.secret_key = "una_clave_super_segura"

@app.route("/")
def inicio():
    saldo=session.get("saldo",5000)
    session["saldo"]=saldo
    fichas = {5:5, 10:10, 25:25, 50:50, 100:100}
    session["fichas"]=fichas
    apuesta=0
    mano = [] 
    cartas_dealer = []
    puntaje_jugador = 0
    return render_template("index.html", 
                           saldo=saldo, 
                           apuesta=apuesta, 
                           mano=mano, 
                           cartas_dealer=cartas_dealer,
                           puntaje_jugador=puntaje_jugador)

@app.route("/partida/<int:fichas>")
def partida(fichas):
    saldo=session.get("saldo",5000)
    apuesta_actual=session.get("apuesta_actual")
    mano=session.get("mano",[])
    mano_d=session.get("mano_d",[])
    descarte=session.get("descarte",[])

    if not apuesta_actual:
        saldo, apuesta_actual=apuestas_jugador(saldo,fichas)
        session["saldo"]=saldo
        session["apuesta_actual"]=apuesta_actual
        mazo=crear_mazo()
        mazo, mano, mano_d, descarte=barajar(mazo)
        session["mazo"]=mazo
        session["mano"]=mano
        session["mano_d"]=mano_d
        session["descarte"]=descarte
    else:
        session["mano"]=mano
        session["mano_d"]=mano_d
        session["descarte"]=descarte

    mano_imagen=[]
    for carta in mano:
        valor=list(carta.keys())[0]
        palo=carta[valor]
        ruta=f"imagenes/{palo}_{valor}.png"
        mano_imagen.append(ruta)

    mano_imagen_d=[]
    for i, carta in enumerate(mano_d):
        if i==0:
            mano_imagen_d.append("imagenes/back_light.png")
        else:
            valor=list(carta.keys())[0]
            palo=carta[valor]
            ruta=f"imagenes/{palo}_{valor}.png"
            mano_imagen_d.append(ruta)

    return render_template("index.html", 
                           saldo=saldo, 
                           apuesta=apuesta_actual,
                           mano_imagen_d=mano_imagen_d, 
                           mano_imagen=mano_imagen, 
                           cartas_dealer=mano_d,
                           puntaje_jugador=calcular_mano(mano))

@app.route("/pedir")
def pedir_c():
    mazo=session.get("mazo",[])
    mano=session.get("mano",[])
    descarte=session.get("descarte",[])
    carta=pedir(mano,mazo,descarte)
    session["mazo"]=mazo
    session["mano"]=mano
    session["descarte"]=descarte
    mano_imagen=[]
    for carta in mano:
        valor=list(carta.keys())[0]
        palo=carta[valor]
        ruta=f"imagenes/{palo}_{valor}.png"
        mano_imagen.append(ruta)

    return render_template("index.html",
                            mano_imagen=mano_imagen,
                            saldo=session["saldo"],
                            apuesta=session["apuesta_actual"],
                            puntaje_jugador=calcular_mano(mano)
    )





















if __name__ == "__main__":
    app.run(debug=True)
