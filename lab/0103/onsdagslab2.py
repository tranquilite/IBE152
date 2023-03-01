# Gjennomgang av metoder på lister

##########################################################
# append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort

lista_mi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # liste!
print(lista_mi)

# ALT ER OBJEKT! (Forklarer mer neste skikkelige lab...)

lista_mi.append(15)
print(lista_mi)

lista_mi.clear()
print(lista_mi)

lista_mi = [1, 2, 3, 4, 5, 6, 6, 6]
print(lista_mi.count(6))

lista_mi = [1, 2, 3, 4, 5, 6, 6, 6]


# Extend!
# Fallgruve! Kan blandes med append, men har oppfører seg veldig annerledes.

ny_ting = ['bah', 'bah']

lista_mi.append(ny_ting)  # append legger *hele* objektet til på slutten
print(lista_mi)

lista_mi = [1, 2, 3, 4, 5, 6, 6, 6]
lista_mi.extend(ny_ting)  # extend *slår begge listene sammen*
print(lista_mi)

lista_mi = [1, 2, 3, 4, 5, 6, 4, 7, 6, 6]
print(
    lista_mi.index(6),  # burde bli 5, right? :)
    lista_mi.index(6, 6)
)


# Merk at pop *returner* objektet som "poppes" av lista!
lista_mi = [1, 2, 3, 4, 5, 6, 4, 7, 6, 6]
print(
    lista_mi.pop(),
    lista_mi.pop(0)
)