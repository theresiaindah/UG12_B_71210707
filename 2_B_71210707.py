a =str(input("Masukkan nama: "))

p = []
q = []

while a != "STOP":
    b = "Masukkan nomor kursi "+a+" :"
    x = input(b)
    if x not in p:
        p.append(x)
        q.append(a)
    else:
        print("Mohon maaf kursi tersebut telah terisi !")
    a= str(input("Masukkan nama: "))
print("List kursi yang telah terisi: ")
for i in range (len(p)):
    print("kursi nomor %s telah diisi oleh %s"%(p[i],q[i]))