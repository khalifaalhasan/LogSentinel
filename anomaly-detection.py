import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# 1. Load Data (Hanya ambil 100.000 baris pertama agar cepat)
print("Sedang membaca file log...")
# Menggunakan separator TAB (\t) karena file kamu TSV
# Header=0 artinya baris pertama adalah nama kolom
df = pd.read_csv('data/access.log', sep='\t',  nrows=100000, on_bad_lines='skip')

# Bersihkan nama kolom (kadang ada spasi)
df.columns = df.columns.str.strip()

print(f"Data berhasil di-load: {len(df)} baris")

# 2. Feature Engineering (Menyiapkan Data untuk ML)
# Kita akan mencari anomali berdasarkan perilaku IP Address
# Fitur: 
# A. Jumlah Request per IP (Traffic Spikes)
# B. Rata-rata Bytes yang diunduh (Data Exfiltration?)

# Group by Host (IP)
ip_features = df.groupby('host').agg({
    'url': 'count',       # Jumlah request
    'bytes': 'mean'       # Rata-rata ukuran file
}).reset_index()

ip_features.columns = ['host', 'request_count', 'avg_bytes']
ip_features = ip_features.fillna(0) # Isi data kosong dengan 0

# 3. Jalankan Isolation Forest
print("Sedang mendeteksi anomali...")
model = IsolationForest(contamination=0.01, random_state=42) # Anggap 1% data adalah anomali
ip_features['anomaly'] = model.fit_predict(ip_features[['request_count', 'avg_bytes']])

# Hasil: -1 adalah Anomali, 1 adalah Normal
anomalies = ip_features[ip_features['anomaly'] == -1]
normal = ip_features[ip_features['anomaly'] == 1]

print(f"Ditemukan {len(anomalies)} IP Address mencurigakan (Anomali).")
print("Contoh IP Anomali:")
print(anomalies.head())

# 4. Visualisasi Scatter Plot
plt.figure(figsize=(10, 6))

# Plot Normal (Biru)
plt.scatter(normal['request_count'], normal['avg_bytes'], 
            c='blue', alpha=0.5, label='Normal Traffic', s=10)

# Plot Anomali (Merah)
plt.scatter(anomalies['request_count'], anomalies['avg_bytes'], 
            c='red', label='Anomaly', marker='x', s=50)

plt.title('Deteksi Anomali Trafik Web (Isolation Forest)')
plt.xlabel('Jumlah Request per IP')
plt.ylabel('Rata-rata Ukuran Paket (Bytes)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Simpan gambar
output_img = 'anomaly_result.png'
plt.savefig(output_img)
print(f"Grafik tersimpan sebagai {output_img}")
plt.show()