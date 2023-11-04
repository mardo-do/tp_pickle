print("partie dictionnaire")
print("1.	Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.")
diks={"jour":"jeudi", "mois":"septembre", "annee":2001,"heure":11}
lis=[]
for kle in diks :
    lis.append(diks[kle])
print("lis vale yo : ", lis)

print("2.	Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè")
vale=input("antre yon vale :  ")
if vale.startswith("{") and vale.endswith("}"):
    print("sa'w rantre a antoure ak {}")
else:
    print("sa'w rantre a pa antoure ak {}")

print("3.	Pakouri yon diksyonè, epi afiche tout kle yo.")
dic={"mango":5, "seriz":3, "lam":"jeremi"}
for kle in dic.keys() :
    print(kle)


print("4.	Pakouri yon diksyonè, epi afiche tout valè yo.")
dic={"mango":5, "seriz":3, "lam":"jeremi"}
for vale in dic.values() :
    print(vale)


print("5.	Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.")
dic={"mango":5, "seriz":3, "lam":"jeremi"}
dic1={}
for kle,vale in dic.items():
    dic1[kle]=vale
print("diksyone kopi :  ", dic1)

print("6.	Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo")
diks={"name": "Lub", "age": 14, "assets": "laptop", "phone":"samsung"}
for kle, vale in diks.items():
    if isinstance(vale, str):
        diks[kle]="_{}_".format(vale)
print(diks)

print("7	Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman.")
dik={"a": "12", "b": "abc", "c": "12r", "d":"90"}
dik2={}
for kle,vale in dik.items():
    if vale.isdigit():
        dik2[kle]=vale
print(dik2)

print("8.	Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la")
diks={"a":1, "b": 2, "c":3, "d":4}
lis=[]
tipl=()
for kle, vale in diks.items():
    tipl=(kle,vale)
    lis.append(tipl)
print(lis)

print("9.	Pakouri yon lis tipl, pou w mete l sou fòm diksyonè")
lis=[('a', 1), ('b', 2), ('c', 3), ('d', 4)]
diks={}
for tipl in lis:
    kle , vale = tipl
    diks[kle]=vale
print(diks)





