from algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    aanbieding = prijs-prijs*korting
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {aanbieding} euro"
    return uitvoer
print (aanbieding_1("aarbei", 4, 0.1))

inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw_1 = 0.09

def inkomsten_totaal(inkomsten, btw_1):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    btw_totaal = totaal * btw_1
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_totaal} euro btw betaald dient te worden."
    return uitvoer
print (inkomsten_totaal(inkomsten, btw_1))

def laag_en_hoog(inkomsten):
    uitvoer = min(inkomsten),max(inkomsten)
    return uitvoer
print (laag_en_hoog(inkomsten))

import statistics
def gemiddelde(inkomsten):
    uitvoer = f"De gemiddelde inkomsten deze week zijn {statistics.mean(inkomsten)} euro"
    return uitvoer
print (gemiddelde(inkomsten))

invoer_lijst_2 = [10, 5, 3, 2, 1, 2, 9]

def meervoudig(invoer_lijst_2):
    uitvoer = laag_en_hoog(invoer_lijst_2)
    return uitvoer
print (meervoudig(invoer_lijst_2))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
print (combinatie(invoer_lijst_2))