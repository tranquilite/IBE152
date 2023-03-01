"""
En streng DNA representeres ofte som en serie med A'er, C'er, 'G' er og 'T'er for hver av nukleotidene.
Så, gitt en streng DNA av en vilkårlig lengde (feks 'ATGCTTCAGAAAGGTCTTACG'), kunne man laget en funksjon som teller antall ganger hver nukleotide dukker opp, og presenterer det på formen 
6, 4, 5, 6
 ?
/me tar på seg quiz-hatten
"""

def dna_nukleo(dna: str) -> None:
    return (dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T'))

print(*dna_nukleo('ATGCTTCAGAAAGGTCTTACG'))
print(str(dna_nukleo('ATGCTTCAGAAAGGTCTTACG'))[1:-1])


# ====================================================================
"""På vei for å gjenskape Jurassic Park på røkkeløkka må vi desverre også gjennom 
transkripsjon til RNA. Heldigvis er det ikke så mye forskjell! Vi må bare flippe T'en 
over til en U, og så begynner vi!
(hint er å sjekke ut metodene på strings)
( Så feks en DNA streng "GATGGAACTTGACTACGTAAATT" ender opp som "GAUGGAACUUGACUACGUAAAUU" )"""

def gattaca(dna: str) -> str:
    return dna.replace('T', 'U')

print(gattaca('GATGGAACTTGACTACGTAAATT'))

# Ble dette rett? Vi tester!
print( gattaca('GATGGAACTTGACTACGTAAATT') == 'GAUGGAACUUGACUACGUAAAUU')
# Tanken her er at vi sammenligner resultatet fra gattaca() med en kjent størrelse
# Vi bruker == for å redusere det til et True/False uttrykk, så vi slipper å huske
# hva den kjente verdien er, eller hva som er rett at funksjonen returnerer, og bare tar det som at
# "Hvis denne printer True, så stemmer det jeg tester for" og avlaster hjernen.


# ====================================================================
"""For mens jeg prøver å gjenskape jurassic park her, så mista jeg litt chemical x i blandebøtta, 
og det blir jo farlig om vi slipper ut masse mutanter, så jeg må finne ut hvor mange mutasjoner 
det er mellom to strenger med DNA ; 😮 
Før: GAGCCTACTAACGGGAT
Etter: CATCGTAATGACGGCCT 

Jeg er helt rådvill! Hvis det er for mange mutasjoner, så får jeg ikke en søt dinosaur, 
men en dodofugl. Ohright, hvis en bokstav er endra mellom før og etter, så er det en mutasjon."""

def dino_or_dodo(dna1: str, dna2: str) -> int:
    avvik = 0

    for idx, nuc in enumerate(dna1):
        if nuc != dna2[idx]:
            avvik += 1

    return avvik

print(
    dino_or_dodo('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT')
)


# ====================================================================
"""Team TA er slu. Vi har begynt å snike oss rundt hver gang det er bedpres og knabbe litt pizza.
Tidligere har første som har funnet rett rom sendt epost til resten av gjengen, men fakultetet
aner ugler i mosen og har begynt å følge med ekstra. For å fortsette å nyte det gode pizzalivet
har vi begynt å kryptere epostene, denne gang med et tradisjonelt Cæsarschiffer.
Grunnideen er at man shifter et alfabet bortover med 13 tegn til høyre (åja, og den wrapper rundt
når det går for langt), så en "A" i klartekst blir en "N" i schiffrert tekst, X blir K, M blir Z, osv..
Alle er velkomne til å bli med på pizzajakten, men dekrypteringsprogrammet vårt er proprietært (tm),
så andre må finne sin egen løsning :V
 "Jeg er så kreativ" 
Oj! Der tikka neste bedpres inn!

GREZVANYEBZ XY GBYI, BAFQNT  """

def TAs_pizzaparty (hemmelighet: str) -> str:
    alfabet = [*'abcdefghijklmnopqrstuvwxyz'.upper()]
    
    # Enkel cheesy håndtering av "dette burde ikke være i strengen"
    if hemmelighet not in alfabet:
        return hemmelighet
    
    # Men dette er essensen i cæsarschifferet:
    return alfabet[(alfabet.index(hemmelighet.upper()) + 13) % 26]

# Løkker er ikke dekket ennå, men virker som om de fleste kan? og nå
# har vi begynt å snakke om map, så why the not
print( ''.join(map(TAs_pizzaparty, 'GREZVANYEBZ XY GBYI BAFQNT')) )



# ====================================================================
""""Ordboka definerer palindrom som et ord eller uttrykk som kan leses 
likt begge veier; for eksempel 'madam', 'rotor', 'ella redder alle'"
Kan vi lage en funksjon som tar en streng, og returnerer True/False avhengig av 
hvorvidt strengen er et palindrom eller ei?"""


def er_palindrom(tekst: str) -> bool:
    return tekst == tekst[::-1]

print(
    er_palindrom('madam'),
    er_palindrom('ella redder alle'),
    er_palindrom('molde')
)