prijzen = {
    "aardbei" : 4,
    "vanille" : 3,
    "chocolade": 5
}
aanbieding = prijzen ["vanille"]*0.8
reclame_tekst = (f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €{aanbieding}")
reclame_tekst2 = reclame_tekst[:62]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if (len(el))>4:
        print (el.upper())
    else:
        print (el.lower())