tal, antal = int(input("N ? ")), 0
for x in range(tal):
    if ((x+1)*(x+2)*(x+3)) >= tal:
        break
    antal += 1
print(f"Svar: {antal}")