n, m, svar = int(input("n ? ")), int(input("m ? ")), ""
for i in range(n):
    svar += input(f"Rad {i+1} ? ").replace(".", "")
print(f"Svar: {svar}")