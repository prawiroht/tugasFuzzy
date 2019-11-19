# membership function TB
def tbRendah(x):
    if x >= 160 :
        return 0
    elif 150 <= x and x <= 160 :
        return (160-x)/10
    else :
        return 1

def tbSedang(x):
    if x <= 150 or x >= 180 :
        return 0
    elif 150 <= x and x <=160 :
        return (x-150)/10
    elif 170 <= x and x <= 180 :
        return (180-x)/10
    else :
        return 1
def tbTinggi(x):
    if x <= 170 :
        return 0
    elif 170 <= x and x <= 180 :
        return (x-170)/10
    else :
        return 1

# membership function BB
def bbRingan(y):
    if y >= 70 :
        return 0
    elif 60 <= y and y <= 70 :
        return (70-y)/10
    else :
        return 1
def bbSedang(y):
    if y <= 60 or y >= 90 :
        return 0
    elif 60 <= y and y <= 70 :
        return (y-60)/10
    elif 80 <= y and y <= 90 :
        return (90-y)/10
    else :
        return 1
def bbBerat(y):
    if y <= 80 :
        return 0
    elif 80 <= y and y <= 90 :
        return (y-80)/10
    else :
        return 1

# membership function IMB
def imbKurus(z):
    if z >= 19 :
        return 0
    elif 18 <= z and z <= 19 :
        return (19-z)
    else :
        return 1
def imbIdeal(z):
    if z <= 18 or z >= 25 :
        return 0
    elif 18 <= z and z <= 19 :
        return z-18
    elif 24 <= z and z <= 25 :
        return 25-z
    else :
        return 1
def imbGemuk(z):
    if z <= 24 :
        return 0
    elif 24 <= z and z <= 25 :
        return z-24
    else :
        return 1

#Rule
def R1(x,y,z): # If x is rendah and y is ringan then z is ideal
    return min(tbRendah(x),bbRingan(y),imbIdeal(z))

def R2(x,y,z): # If x is rendah and y is sedang then z is gemuk
    return min(tbRendah(x),bbSedang(y),imbGemuk(z))

def R3(x,y,z): # If x is rendah and y is berat then z is gemuk
    return min(tbRendah(x),bbBerat(y),imbGemuk(z))

def R4(x,y,z): # If x is sedang and y is ringan then z is kurus
    return min(tbSedang(x),bbRingan(y),imbKurus(z))

def R5(x,y,z): # If x is sedang and y is sedang then z is ideal
    return min(tbSedang(x),bbSedang(y),imbIdeal(z))

def R6(x,y,z): # If x is sedang and y is berat then z is gemuk
    return min(tbSedang(x),bbBerat(y),imbGemuk(z))

def R7(x,y,z): # If x is tinggi and y is ringan then z is kurus
    return min(tbTinggi(x),bbRingan(y),imbKurus(z))

def R8(x,y,z): # If x is tinggi and y is sedang then z is ideal
    return min(tbTinggi(x),bbSedang(y),imbIdeal(z))

def R9(x,y,z): # If x is tinggi and y is berat then z is gemuk
    return min(tbTinggi(x),bbBerat(y),imbGemuk(z))
    
tb = float(input("Masukkan tinggi badan(cm) : "))
bb = float(input("Masukkan berat badan(kg)  : "))

penyebut = 0
pembilang = 0

i = 15
while(i <= 30):
    a = max(R1(tb,bb,i),R2(tb,bb,i),R3(tb,bb,i),R4(tb,bb,i),R5(tb,bb,i),R6(tb,bb,i),R7(tb,bb,i),R8(tb,bb,i),R9(tb,bb,i))
    penyebut += a*0.01
    pembilang += i*a*0.01
    i += 0.01
    
bmi = pembilang/penyebut    
print(bmi)

if bmi < 18 :
    print("Kurus, Naikkan berat badan anda")
elif bmi < 19:
    print("Kurang ideal, Naikkan berat badan anda sedikit lagi")
elif bmi < 24:
    print("Berat badan ideal, pertahankan")
elif bmi < 25:
    print("Sedikit kegemukan, turunkan berat badan anda sedikit lagi")
else:
    print("Kegemukkan, turunkan berat badan anda")