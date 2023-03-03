"""
Merk at alt er skrevet i egne funksjoner for å holde ting mer adskilt.
Koden er veilendende og ikke sjekket opp mot faktiske sensurveiledninger (utilgjengelige atm)
"""


# O1 IBE151 10/12/19
"""Merk at oppgaven ikke ber om en funksjon! Bare kodeblokken som følger:"""
dividend = float(input('Dividend. Erstatt komma med . (punktum)'))
divisor = float(input('Divisor. Erstatt komma med . (punktum)'))

kvotient = dividend / divisor

print(kvotient)

# O2 10/12/19
# Aight. Hadde en tasteleif i øvingssettet da jeg transkriberte;
# Test for 556 skal være 0:9:16

sekunder_etter_hendelse = int(input('Sekunder etter hendelse: '))

timer = sekunder_etter_hendelse // 3600
minutter = sekunder_etter_hendelse % 3600 // 60 
#sekunder = 
sekunder = sekunder_etter_hendelse \
            - (timer * 3600) \
            - (minutter * 60)

print(f'{timer}:{minutter}:{sekunder}')

# O3 10/12/19
""" Merk at denne oppgaven ber deg skrive en funksjon!"""
def func3(A: int, B: int, C: int) -> bool:
    """Ikke glem docstrings!
    Sjekker om summen av A og B er under (ekslusivt) C, eller om C er partall
    
    args:
        A (int): første heltall (summeres)
        B (int): andre heltall (summeres)
        C (int): Heltallet det sammenlignes mot
    return:
        bool: True hvis A+B > C eller hvis C er partall
    """
    
    # Maybe this?
    if A+B < C:
        return True
    elif C % 2 == 0:
        return True
    else:
        return False

    # or this
    if A+B < C or C % 2 == 0:
        return True
    return False

#print(func3(1, 2, 3) == False)  # Input sample 1 == Output sample 2
#print(func3(-124, -18, 10) == True)  # Input sample 2 == Output sample 2

# O7 10/12/19
def oppgave7(liste_med_tall: list, target: int) -> int:
    """Docstrings!
    Tar en liste heltall liste_med_tall og et søker etter et tall target.
    Gir indeksen hvor tallet finnes.
    
    args:
        liste_med_tall (list): Liste med kandidattall.
        target (int): heltall som søkes etter i liste_med_tall
    returns:
        (int) indeksen for target i liste_med_tall
    """

    if target in liste_med_tall:
        return liste_med_tall.index(target)
    return -1


# O2 3/2/20
def kg_til_pounds(kilo: float) -> float:
    """Konverterer gitte kg til pounds? pund? lbs. Imperial vektenhet.
    Antar 1 kg = 2.2 lbs
    args:
        kilo (float): Vekt i kg
    returns:
        (float) Vekt i lbs
    """
    POUNDS_IN_KG = 2.2  # Fra oppgaveteksten, la 1kg være 2.2 lbs
    return POUNDS_IN_KG * kilo

# O5 3/2/20
# TODO !!
def trekant_tull(A: int, B: int, C: int) -> None:
    """Tar lengden av hver side i en trekant og printer ut en beskrivende melding.
    La a, b, c være punkt på trekanti, då e
    args:
        A (int): Avstand a->b
        B (int): Avstand b->c
        C (int): Avstand c->a
    returns
        None"""
    if A == B == C:
        print('Equilateral triagnle')
    elif A == B or B == C or C == A:
        print('')

"""
O1 8/12/20
"a program" kan være uklart, men det har aldri feilet å anta en funksjon.
Heller ikke nøl med å sende fagledelse et spørsmål om presisering. De bare sitter
der med mobilen og venter uansett."""

def european_in_the_usa() -> None:
    METER_I_MILES = 1609.344
    miles = float(input('Enter the distance in miles: '))

    print('The distance in meters is: ', METER_I_MILES*miles)


"""
O2 8/12/20
Merk at funksjonsnavnet er oppgitt i oppgaveteksten!"""
def isPosDiv(et_heltall: int) -> bool:
    """Tar et heltall og returnerer True hvis tallet er delelig med 10 og positivt"""
    return True if (et_heltall % 10) and (et_heltall > 0) else False

    # eh
    if et_hetall % 10 and et_heltall > 0:
        return True
    return False

"""
O1 02/03/22

"""