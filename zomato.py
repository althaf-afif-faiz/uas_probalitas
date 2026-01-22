import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Langkah 2: Membuat bingkai data (Load Data)
# Pastikan file csv berada di lokasi yang sama atau sesuaikan path-nya
dataframe = pd.read_csv("Zomato-data-.csv")

# Langkah 3: Pembersihan dan Persiapan Data
def handleRate(value):
    try:
        value = str(value).split('/')
        value = value[0]
        return float(value)
    except:
        return np.nan

dataframe['rate'] = dataframe['rate'].apply(handleRate)

print("--- Informasi Dataframe ---")
dataframe.info()
print("\n--- Jumlah Nilai Null ---")
print(dataframe.isnull().sum())

# Langkah 4: Menjelajahi Jenis Restoran
plt.figure(figsize=(10, 6))
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
plt.title("Jumlah Restoran berdasarkan Tipe")
plt.show()

# Total vote berdasarkan tipe restoran
grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.figure(figsize=(10, 6))
plt.plot(result, c='green', marker='o')
plt.xlabel('Type of restaurant')
plt.ylabel('Votes')
plt.title("Total Votes berdasarkan Tipe Restoran")
plt.show()

# Langkah 5: Identifikasi Restoran yang Paling Banyak Dipilih
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']
print('\n--- Restoran dengan Votes Tertinggi ---')
print(restaurant_with_max_votes)

# Langkah 6: Ketersediaan Pesanan Online
plt.figure(figsize=(6, 6))
sns.countplot(x=dataframe['online_order'])
plt.title("Ketersediaan Pesanan Online")
plt.show()

# Langkah 7: Analisis Peringkat (Rate)
plt.figure(figsize=(8, 6))
plt.hist(dataframe['rate'].dropna(), bins=5, edgecolor='black')
plt.title('Distribusi Rating')
plt.show()

# Langkah 8: Perkiraan Biaya untuk Pasangan
plt.figure(figsize=(12, 6))
sns.countplot(x=dataframe['approx_cost(for two people)'])
plt.title("Perkiraan Biaya untuk Dua Orang")
plt.xticks(rotation=45)
plt.show()

# Langkah 9: Perbandingan Peringkat - Pesanan Online vs Offline
plt.figure(figsize=(6, 6))
sns.boxplot(x='online_order', y='rate', data=dataframe)
plt.title("Hubungan Rating dengan Pesanan Online")
plt.show()

# Langkah 10: Preferensi Mode Pesanan berdasarkan Jenis Restoran (Heatmap)
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap: Tipe Restoran vs Pesanan Online')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()