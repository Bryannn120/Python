#KALKULATOR
print("="*20)
print("PROGRAM KALKULATOR")
print("="*20)
print("1. Penjuhalan")
print("2. pengurangan")
print("3. perkalian")
print("4. pembagian")
print("5. KELUAR")
j = int(input("Masukan pilihan 1/2/3/4/5 :"))

if j==1:
    a = int(input("Masukan bil 1 : "))
    b = int(input("Masukan bil 2 : "))
    c = a + b
    print(a, "+" ,b, "=", c)
    print()
elif j==2:
    a = int(input("Masukan bil 1 : "))
    b = int(input("Masukan bil 2 : "))
    c = a - b
    print(a, "-" ,b, "=", c)
    print()
elif j==3:
    a = int(input("Masukan bil 1 : "))
    b = int(input("Masukan bil 2 : "))
    c = a * b
    print(a, "*" ,b, "=", c)
    print()
elif j==4:
    a = float(input("Masukan bil 1 : "))
    b = float(input("Masukan bil 2 : "))
    c = a / b
    print(a, "/" ,b, "=", c)
    print()
else:
    print("BERHENTI")