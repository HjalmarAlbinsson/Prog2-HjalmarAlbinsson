antal_byggnader, kostnad_mp, byggnads_lista = int(input("Antal byggnader ? ")), int(input("Kostnad av Megapickeln ? ")), []
for f in range(antal_byggnader):
    inmat = input(f"Produktionshastighet och pris för byggnad {f+1} ? ").split(" ")
    byggnads_lista.append([int(inmat[0]), int(inmat[1]), int(inmat[0])/int(inmat[1])])

prod_hast = byggnads_lista[0][0]
KALKYERAR = True
pickles = 0
tid = 0

while KALKYERAR:
    if pickles >= kostnad_mp:
        print(f"Svar: {tid}")
        KALKYERAR = False

    tid += 1
    pickles += prod_hast
    best_byggnad_der = [0, 0, 0]
    for i in (byggnads_lista):
        if i[1] <= pickles and i[2] > best_byggnad_der[2] and ((kostnad_mp-pickles) / prod_hast) > i[2]/i[1]:
            best_byggnad_der = i

    prod_hast += best_byggnad_der[0]
    pickles -= best_byggnad_der[1]

    if pickles >= 1000:
        print(pickles)