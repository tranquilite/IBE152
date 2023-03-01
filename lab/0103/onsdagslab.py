
# Alt er egentlig bare navn
a = 12
# Du lager et alias 'a'

a = lambda x: x # her kommer funksjonsisntruksene dine inn.

a = 12  # lage alias 'a' på objektet 12
b = 24  # lage alias 'b' på objektet 24
a = b  # sette alias 'a' LIK 'b'
del b

def alias_paa_funksjonen(parameterliste):
    pass

alias2 = alias_paa_funksjonen
alias2('yah')

#list.index()

#LISTA_MI.index(12)
#__getitem_(LISTA_MI, 12)  # Way for komplisert atm

# Dette er python;:
def FUNKSJONEN_MIN(arg1: int, arg2: list) -> bool:
    pass

# FUNKSJONEN_MIN

    #annotert: int, int, return int
def func(arg1: int, arg2: int) -> int:
    return arg1 * arg2

pfft = func(1.5, 1.25) #  Magic! 1.875! FLOAT! Ikke int, selv om det er det vi har
# annotert som returntype

# Dette er C++
# bool myFunc (int arg1, int arg2) {}

# 'yolo'.index()

# []
# " Finn dette i arrayet/rekka/serien "

#(__getitem__, _-setitem__ og __delitem__ FUNFACT! Ignorer dette inntil neste ukes fredag)

# ()
# *KJØR KODEN* knytta til dette navnet.



# ==========================================================

navn = 'Navn Navnesen'

print( 'Hei, ' + navn )  # Går fint
# print( 'Hei, ' + 12 )  # Går ikke

print( 'Hei, ' + str(12) )  # Caste til str, og det funker igjen!

# STRENGFORMATERING!
# print('Hei, {}'.format(navn))
a, b, c, d = 12, 24, 36, 58
print(f'Hei, {navn=} {a=} {b=} {c=} {d=}')

def demo():
    a = input('Enter val: ')
    b = input('Enter another val: ')

    print(f' {a} + {b} = {int(a)+int(b)}')

demo()

    
