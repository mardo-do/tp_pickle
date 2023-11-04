print("1.	Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif")
lis=["aba","ariel","viv","biden"]*2
print(lis)


print("2	Ou gen yon lis antye, konvèti l an yon lis chenn.")
lis1=[1 , 3, 4, 5, 6, 8,]
lis2=[]
for nb in lis1:
    lis2.append(str(nb))
print(lis2)





print("3.	Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil")
lis_min=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
konveti=" ".join(lis_min)
konveti=konveti.upper()
lis_maj=konveti.split(" ")
print(lis_maj)

print("4.	Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman")
lis1=["lundi","mardi","mercredi","lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche","mercredi","samedi","jeudi","vendredi","lundi"]
lis2=[]
i=1
while i < len(lis1):
    if i % 3 ==0:
        lis2.append(lis1[i])
    i +=1
print(lis2)

print("5.	Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl.") 
lis1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
tipl=()
lis2=[]
i=1
for nb in range(len(lis1)):
    if i%3 == 0:
        tipl=(lis1[i-3],lis1[i-2],lis1[i-1])
        lis2.append(tipl)
    i +=1
print(lis2)


print("6.	Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.")
lis1=["lundi","mardi","mercredi","lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche","mercredi","samedi","jeudi","vendredi","lundi"]
lis2=[]
for el in lis1:
    if el in lis2:
        continue
    else:
        lis2.append(el)
print(lis2)





print("7.	Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.")
lis1=["lundi","mardi","jeudi","dimanche"]
lis2=["mercredi","samedi","jeudi","vendredi","lundi"]
lis3=[]
for l1 in lis1 :
    for l2 in lis2:
        if l1==l2:
            lis3.append(l1)
print(lis3)


print("8.	Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.")
lis1=["mango","zaboka","seriz","patat",1,4,3,5,5]
lis2=["patat","lam","zoranj","seriz","kawot",3,5,3]
lis3=list(set(lis1)&set(lis2))
print(lis3)

print("9.	Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman")
diks={"jour":"jeudi", "mois":"septembre", "annee":2001,"heure":11}
lis=[]
lis1=[]
for kle in diks.keys():
    lis.append(kle)
print("lis kle : ", lis)

for kle in diks.values():
    lis1.append(kle)
print("lis vale : ", lis1)

print("10.	Reyini 3 lis ansanm, san okenn doublon.")
lis1=["mango","zaboka","seriz","patat"]
lis2=["patat","lam","zoranj","seriz","kawot"]
lis3=["kawot","zaboka","kenep","sitron"]
lis1_2=lis1 + list(set(lis2)-set(lis1))
lis2_3=lis2 + list(set(lis3)-set(lis2))
lis4=lis1_2 + list(set(lis2_3)-set(lis1_2))
print(lis4)
        

