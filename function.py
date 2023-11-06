import random
import string
print("1.	kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.")

def enves(mo):
    long=len(mo)
    inv=""
    j=1
    for i in range(long):
        inv +=mo[long-j]
        j += 1

    return inv
print(enves("mardochee"))

print("2.	kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik")
def kod_aleyatwa(nonb=int(input("konbyen let ou vle kod la genyen?  :  "))):
    karakte=string.ascii_letters
    kod=""
    for l in range(nonb):
        kod+="".join(random.choice(karakte))
    return kod
print("kod aleyatwa :  ",kod_aleyatwa())

print("3.	kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.")
def aleyatwaSanRepetisyon(nonb=int(input("konbyen let ou vle kod la genyen?  :  "))):
    karakte=string.ascii_letters
    kod=""
    for l in range(nonb):
        if random.choice(karakte) not in kod :
            kod+="".join(random.choice(karakte))
        else:
            continue
    return kod
print("kod aleyatwa san repetisyon  :  ",aleyatwaSanRepetisyon())

print("4.	kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon")
def alafanimerik(nonb=int(input("konbyen let ou vle kod la genyen?  :  "))):
    karakte=string.ascii_letters + string.digits
    kod=""
    for l in range(nonb):
        if random.choice(karakte) not in kod :
            kod+="".join(random.choice(karakte))
        else:
            continue
    return kod
print("kod aleyatwa san repetisyon  :  ",alafanimerik())


print("5.	Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. ")
lisMw=["pa1tat","la1m","zoran2j","seriz","ka-wot"]

     




print("6.	Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil")
def separe_let(fraz=""):
    i=0
    fraz2=""
    for mo in fraz:
        if   mo ==" ":
            continue
        else:
            fraz2+=mo+","
    return fraz2
print(separe_let("ayibobo"))

print("7.	Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè")
def kripte(mo=""):
    alfa="abcdefghijklmnopqrstuvwxyz"
    mo_kripte=""
    for let in mo:
        if let in alfa:
            mo_kripte+="{}-".format(alfa.index(let))
    return mo_kripte
print(kripte("alo"))




print("8.	Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè")
def dekripte(mo=""):
    lis=mo.split("-")
    alfa="abcdefghijklmnopqrstuvwxyz"
    mo_dekripte=""
    for el in lis:
        if el.isdigit():
            mo_dekripte+=alfa[int(el)]
        elif el=="-":
            continue
        else:
            continue
    return mo_dekripte
print(dekripte("0-11-14"))

print("9.	Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li retounen tou 2 valè yo sou fòm Tuple.")
def pemite(val1,val2):
    tipl=(val2,val1)
    return tipl
print(pemite("marie","rose"))


print("10.	Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. Atansyon ak non konpoze ak tirè yo")
def inisyal(non=""):
    nonn=non.replace("-"," ")
    non1=nonn.split(" ")
    let1=""
    for lis in non1:
        let1+=lis[0]
    return let1
print(inisyal("Jean-Baptiste Jean"))