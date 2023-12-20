import math
protein, k = input("Björns protein ? "), int(input("k ? "))
alla_typer_proteiner = set(protein)
minsta_klippnings_antal = 100
for protein_typ_av_set in alla_typer_proteiner:
    antal_glapp = 0
    klippnings_antal = 0
    for index, protein_typ in enumerate(protein):
        if protein_typ != protein_typ_av_set:
            antal_glapp += 1
        if protein_typ == protein_typ_av_set or index == len(protein)-1:
            if (antal_glapp/k) >= 1:
                klippnings_antal += math.ceil(antal_glapp/k)
            elif antal_glapp > 0:
                klippnings_antal += 1
            antal_glapp = 0
    if klippnings_antal < minsta_klippnings_antal:
        minsta_klippnings_antal = klippnings_antal
print(f"Svar: {minsta_klippnings_antal}")