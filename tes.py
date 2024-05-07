import matplotlib.pyplot as plt

# Data
kelompok1 = {
    'Angka': [1, 2, 3, 4, 5, 6],
    'Frekuensi': [18, 13, 10, 18, 24, 17]
}

kelompok2 = {
    'Angka': [1, 2, 3, 4, 5, 6],
    'Frekuensi': [14, 17, 18, 17, 12, 22]
}

# Plotting Kelompok 1
plt.figure(figsize=(10, 5))
plt.bar(kelompok1['Angka'], kelompok1['Frekuensi'], color='blue', alpha=0.7)
plt.title('Frekuensi Kemunculan Angka - Kelompok 1')
plt.xlabel('Angka')
plt.ylabel('Frekuensi')
plt.xticks(kelompok1['Angka'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Plotting Kelompok 2
plt.figure(figsize=(10, 5))
plt.bar(kelompok2['Angka'], kelompok2['Frekuensi'], color='red', alpha=0.7)
plt.title('Frekuensi Kemunculan Angka - Kelompok 2')
plt.xlabel('Angka')
plt.ylabel('Frekuensi')
plt.xticks(kelompok2['Angka'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
