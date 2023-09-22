meme_dict = {
    'CRINGE': 'Pena agena',
    'LOL': 'Una respuesta común a algo gracioso',
    'ROFL': 'Ligera desaprobación',
    'SHEESH': 'Ligera desaprobación',
    'CREEPY': 'aterrador, siniestro',
    'AGGRO': 'ponerse agresivo/enojado'
}

word = input("escribe una palabra que no entiendas(¡con mayusculas!)")

if word in meme_dict.keys():
    #¿que hacer si no se encuentra la palabra?
    print(meme_dict[word])
else:
    # ¿que hacer si no se encuentra la palabra?
    print("Tu palabra no esta, lo siento")
