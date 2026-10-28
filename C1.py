# ----------------------------------------------------------------------
# C1. Atzīmju kopsavilkums
# ----------------------------------------------------------------------

# Kodā izveido sarakstu ar septiņām atzīmēm. Izvadi to skaitu, summu, vidējo, augstāko un zemāko. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Sarakstu, kurā glabā atzīmes, nosauc ar vārdu atzimju_saraksts.

atzimju_skaits = [5,3,7,4,1,9,10]

print ("Skaits:",len(atzimju_skaits))
print ("Summa:", sum(atzimju_skaits))
print ("Vidējaus:"), sum(atzimju_skaits) / len(atzimju_skaits)
print ("Augstākais:", max(atzimju_skaits))
print ("Zemākais:", min(atzimju_skaits))
