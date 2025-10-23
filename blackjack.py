import random
valores=[2,3,4,5,6,7,8,9,10,'j','q','k','a']
random.shuffle(valores)
valor=valores[0]
palos=['corazones','picas','trebol','diamantes']
palo=palos[0]
random.shuffle(palos)
print({valor:palo})
