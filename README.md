# uas_probalitas

# Nama : Althaf Afif Faiz
# NIM : 312410404
# Kelas : TI.24.A.3

# 📊 Analisis Data Restoran Zomato

Proyek ini adalah implementasi **Exploratory Data Analysis (EDA)** menggunakan Python untuk menganalisis dataset restoran dari Zomato. Tujuan utamanya adalah untuk memahami preferensi pelanggan, faktor yang mempengaruhi rating restoran, dan tren bisnis kuliner.

## 📝 Gambaran Proyek

Dalam proyek ini, kami mengolah data mentah restoran untuk menjawab pertanyaan bisnis seperti:
* Tipe restoran apa yang paling populer?
* Apakah restoran yang menyediakan *online order* memiliki rating lebih tinggi?
* Berapa kisaran harga rata-rata untuk dua orang?
* Bagaimana hubungan antara tipe restoran dengan ketersediaan layanan online?

## 🛠️ Teknologi yang Digunakan

Proyek ini dibangun menggunakan pustaka Python berikut:
* **Pandas**: Untuk manipulasi dan pembersihan data (DataFrame).
* **Numpy**: Untuk operasi numerik dan penanganan nilai kosong.
* **Matplotlib & Seaborn**: Untuk visualisasi data (grafik batang, boxplot, heatmap, dll).

## 📂 Struktur File

* `Zomato-data-.csv`: Dataset mentah yang berisi informasi restoran (Nama, Vote, Rate, Biaya, dll).
* `analisis_zomato.py`: Skrip Python utama yang berisi seluruh kode analisis dan visualisasi.
* `README.md`: Dokumentasi proyek ini.

## 🚀 Langkah-Langkah Analisis

Kode program mencakup langkah-langkah berikut sesuai metodologi analisis data:

1.  **Data Loading**: Memuat dataset CSV ke dalam Pandas DataFrame.
2.  **Data Cleaning**: Membersihkan kolom `rate` (mengubah format '4.1/5' menjadi float) dan menangani *missing values*.
3.  **Univariate Analysis**:
    * Visualisasi jumlah restoran berdasarkan tipe.
    * Analisis distribusi rating.
    * Analisis perkiraan biaya untuk dua orang.
4.  **Bivariate Analysis**:
    * Hubungan antara *Online Order* dan *Rating* (menggunakan Boxplot).
    * Total *Votes* berdasarkan tipe restoran.
5.  **Multivariate Analysis**:
    * Heatmap untuk melihat korelasi antara Tipe Restoran dan Ketersediaan Pesanan Online.

## 💻 Cara Menjalankan

1.  Pastikan Anda telah menginstal Python.
2.  Instal pustaka yang diperlukan dengan perintah:
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
3.  Pastikan file `Zomato-data-.csv` berada dalam satu folder dengan skrip Python.
4.  Jalankan program:
    ```bash
    python analisis_zomato.py
    ```

## 📊 Hasil Temuan (Insights)

Beberapa wawasan menarik dari analisis ini:
* **Restoran Populer**: "Empire Restaurant" adalah restoran dengan jumlah votes terbanyak.
* **Online Order**: Mayoritas restoran tipe "Dining" tidak menyediakan layanan pesan antar online, sedangkan tipe "Cafe" lebih seimbang.
* **Rating**: Terdapat korelasi positif di mana restoran yang menyediakan layanan *online order* cenderung memiliki sebaran rating yang sedikit lebih tinggi.
* **Biaya**: Sebagian besar restoran menawarkan harga yang terjangkau (kisaran rendah-menengah) untuk paket makan dua orang.

---
*Dibuat sebagai bagian dari latihan Analisis Data dengan Python.*
