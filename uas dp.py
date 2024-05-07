print("===== Bryan Oktoviano R =====")
print("Konverter Satuan Suhu")

print("===== Konversi Celcius =====")

Celcius = float(input("Masukan Nilai Celius : "))
Fahrenheit = (9 / 5) * Celcius + 32
Reamur = (4 / 5) * Celcius
Kelvin = Celcius + 273

print("Nilai Celcius : ", Celcius, "C")
print("Nilai Dalam Fahrenheit : ", Fahrenheit, "F")
print("Dalam Nilai Reamur : ", Reamur, "R")
print("Dalam Nilai Kelvin : ", Kelvin, "K")

###########################################################

print("===== Konversi Fahrenheit =====")

Fahrenheit = float(input("Masukan Nilai Fahrenheit : "))
Celcius = (5 / 9) * (Fahrenheit - 32)
Reamur = (4 / 9) * (Fahrenheit - 32)
Kelvin = (5 / 9) * (Fahrenheit - 32) + 273

print("Nilai Fahrenheit : ", Fahrenheit, "F")
print("Nilai Dalam Celcius : ", Celcius, "c")
print("Dalam Nilai Reamur : ", Reamur, "R")
print("Dalam Nilai Kelvin : ", Kelvin, "K")

###########################################################

print("===== Konversi Reamur =====")

Reamur = float(input("Masukan Nilai Reamur : "))
Celcius = (5 / 4) * Reamur
Fahrenheit = (9 / 4) * Fahrenheit + 32
Kelvin = (5 / 4) * Reamur + 273

print("Nilai Reamur : ", Reamur, "R")
print("Nilai Dalam Celcius : ", Celcius, "C")
print("Dalam Nilai Fahrenheit : ", Fahrenheit, "F")
print("Dalam Nilai Kelvin : ", Kelvin, "K")

###########################################################

print("===== Konversi Kelvin =====")

Kelvin = float(input("Masukan Nilai Kelvin : "))
Celcius = Kelvin - 273
Fahrenheit = (9 / 5) * (Kelvin - 273) + 32
Reamur = (4 / 5) * (Kelvin - 273)

print("Nilai Kelvin : ", Kelvin, "K")
print("Nilai Dalam Celcius : ", Celcius, "c")
print("Dalam Nilai Fahrenheit : ", Fahrenheit, "F")
print("Dalam Nilai Reamur : ", Reamur, "R")