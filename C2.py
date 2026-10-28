# ----------------------------------------------------------------------
# C2. Degviela un braucieni
# ----------------------------------------------------------------------

# Tvertnē ir 50 litri degvielas. Viens brauciens patērē 7 litrus. Izvadi, cik braucienu var veikt un cik degvielas paliek pāri. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------     

degviela = 50
paterins = 7

braucieni = (degviela / paterins)
paliek = degviela - (braucieni * paterins)

print(braucieni, "braucieni")
print(paliek, "litri")
