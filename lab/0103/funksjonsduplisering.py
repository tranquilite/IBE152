def hours(sekunder, is_24):
    return 1


test_timer_inn = [60]
test_timer_ut = [1]

for x, y in zip(test_timer_inn, test_timer_ut):
    if hours(x, True) == y:
        print("Hurra!")


def minuter(sekunder, is_24):
    return 1


test_min_inn = [60]
test_min_ut = [1]

for x, y in zip(test_min_inn, test_min_ut):
    if hours(x, True) == y:
        print("Hurra!")


test_sc_in = [60]
test_sc_out = [1]

for x, y in zip(test_sc_in, test_sc_out):
    if hours(x, True) == y:
        print("Hurra!")


#=================================================
# BRUKER FUNKSJONER FOR Å REDUSERE DUPLISERING.
# Alt over er plutselig kokt ned til:


def litt_mer_kompakt(test_inn, test_ut, testf):
    for x, y in zip(test_inn, test_ut):
        if testf(x, True) == y:
            print("Hurra!")





def funksjon_som_adderer(addend, addend2):
    return addend+addend2
