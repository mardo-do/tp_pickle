#je suis mardo etudiant en L4 ESH

print("LA PARTIE STR ")

#MASTER STR (index, split, replace, lower, upper, title)

print("1.	Nan yon chenn karaktè, mete tout karaktè yo an miniskil")
ma_Chaine="Ayibobo Ayiti"
ma_Chaine=ma_Chaine.lower()
print(ma_Chaine)

print("#2.	Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas. Epi afiche yon lis ki gen chak eleman yo")
ma_Chaine="Ayibobo Ayiti"
print(ma_Chaine.split(" "))


print("3.	Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil.")
ma_Chaine="je deteste le language python"
ma_Chaine=ma_Chaine.title()
print(ma_Chaine)

print("4.	Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.")
chaine1="bonjour tout le monde"
chaine2=chaine1.split(" ")
ch2=""
for ch in chaine2 :
    ch2 += ch[0]
print(ch2)

print("5.	Ranplase tout karaktè a ki nan yon chenn pa '@'")
ma_Chaine="viv lang kreyol la "
ma_Chaine=ma_Chaine.replace("a", "@")
print(ma_Chaine)

print("6.	Mete yon chenn karaktè devan dèyè, answit mete l an majiskil") 
chaine="salut"
long=len(chaine)
inv=""
j=1
for i in range(long):
    inv +=chaine[long-j]
    j += 1

print(inv.upper())




print("7.	Afiche endeks premye karaktè 'a' ki nan yon chenn.")
ma_Chaine="Ayiti kapab avanse"
print(ma_Chaine.index("a"))

print("8.	Afiche total tout endeks karaktè 'a' ki nan yon chenn (Kit se a majiskil oubyen miniskil).")
chaine="Ayiti kapab avanse"
long=len(chaine)
ind=0
j=0
for ch in range(long):
    if chaine[j]=="A"or chaine[j]=="a":
        ind += j
    j +=1
print(ind)

print("9.	Kreye yon lis ki gen endeks tout karaktè 'a' ki nan yon chenn (Sèlman a miniskil")
chaine="Ayiti kapab avanse"
lis=[]
long=len(chaine)
j=0
for ch in range(long):
    if chaine[j]=="a":
        lis.append(j)
    j +=1
print(lis)

print("10.Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo)")
chen="ariel henry vole"
ch=""
for let in chen :
    if let.isspace()==True :
        continue
    else :
        ch += let
print(ch)