fizikusok=[]
with open("fizikusoik.txt","r",encoding="utf-8")as f:
    for sor in f:
        kislista=sor[:-1].split(";")
        fizikusok.append(kislista)
    f.close() 

evszamok = [int(fizikus[2]) for fizikus in fizikusok]
atlagos_evszam = sum(evszamok) / len(evszamok)
legkorabbi = min(evszamok)
legkesobb = max(evszamok)

print("Legkorábbi felfedezési évszám:", legkorabbi)
print("Legkésőbbi felfedezési évszám:", legkesobb)
print("Átlagos felfedezési évszám:", atlagos_evszam)

