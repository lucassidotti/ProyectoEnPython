from flask import Flask, render_template, session, redirect, url_for, request
from blackjack_logic import crear_mazo, barajar, calcular_mano, apuestas_jugador, black_jack_n, pedir, doblar, plantarse, turno_dealer, jugadas, imagen_carta

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

    mano_imagen=imagen_carta(mano)

    mano_imagen_d=imagen_carta(mano_d,tapada=True)

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
    mano_d=session.get("mano_d",[])
    descarte=session.get("descarte",[])
    pedir(mano,mazo,descarte)
    session["mazo"]=mazo
    session["mano"]=mano
    session["descarte"]=descarte
    
    mano_imagen=imagen_carta(mano)
    mano_imagen_d=imagen_carta(mano_d,tapada=True)

    return render_template("index.html",
                            mano_imagen=mano_imagen,
                            mano_imagen_d=mano_imagen_d,
                            saldo=session["saldo"],
                            apuesta=session["apuesta_actual"],
                            puntaje_jugador=calcular_mano(mano)
    )

@app.route("/doblar")
def doblar_a():
    mazo=session.get("mazo",[])
    saldo=session.get("saldo")
    descarte=session.get("descarte",[])
    apuesta_actual=session.get("apuesta_actual")
    mano=session.get("mano",[])
    mano_d=session.get("mano_d",[])

    saldo, apuesta_actual, mano, mazo, descarte, puntaje_jugador = doblar(saldo, apuesta_actual, mano, mazo, descarte)
    
    saldo, puntaje_jugador, puntaje_dealer, resultado = jugadas(saldo, mano_d, mazo, apuesta_actual, mano, descarte)

    session["mazo"]=mazo
    session["saldo"]=saldo
    session["apuesta_actual"]=apuesta_actual
    session["mano"]=mano
    session["mano_d"]=mano_d
    session["descarte"]=descarte

    mano_imagen=imagen_carta(mano)
    mano_imagen_d=imagen_carta(mano_d,tapada=False)

    return render_template("index.html",
                            mano_imagen=mano_imagen,
                            mano_imagen_d=mano_imagen_d,
                            saldo=saldo,
                            apuesta=apuesta_actual,
                            puntaje_jugador=puntaje_jugador,
                            puntaje_dealer=puntaje_dealer,
                            resultado=resultado
    )

















if __name__ == "__main__":
    app.run(debug=True)
