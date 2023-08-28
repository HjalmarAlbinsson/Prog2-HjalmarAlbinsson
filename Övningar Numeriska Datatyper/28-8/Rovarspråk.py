konsonanter = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
text = input("Skriv en text: ").lower()
ny_text = ""
for bokstav in text:
    if bokstav in konsonanter:
        ny_text += bokstav + "o" + bokstav
    else:
        ny_text += bokstav
print(ny_text)