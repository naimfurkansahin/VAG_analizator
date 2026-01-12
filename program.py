'''
naimfurkansahin@gmail.com

VAG grubu araçların piyasa analizini yapan ve alım satımda yarar sağlaması adına
grafik çizdiren bir python programı.
'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ayarlar
sns.set_theme(style="whitegrid", context="talk")

# geçici veri seti oluşturdum.
data = {
    'Marka': ['Seat', 'Seat', 'Seat', 'Volkswagen', 'Volkswagen', 'Volkswagen', 'Cupra', 'Cupra',
              'Audi', 'Audi'],
    'Model': ['Leon', 'Leon', 'Leon', 'Golf', 'Golf', 'Golf', 'Formentor', 'Formentor', 'A3', 'A3'],
    'Paket': ['FR', 'Style', 'FR', 'Life', 'R-Line', 'Life', 'VZ', 'VXL', 'Advanced', 'S-Line'],
    'Yil': [2020, 2019, 2021, 2020, 2021, 2019, 2022, 2023, 2021, 2022],
    'KM': [45000, 60000, 30000, 50000, 25000, 70000, 15000, 5000, 60000, 45000],
    'Fiyat': [1270000, 900000, 1300000, 1300000, 900000, 910000, 210000, 2400000, 1900000, 2100000],
    'Hasar_Kaydi': [0, 5000, 0, 0, 0, 12000, 0, 0, 1000, 0]
}

# 1 - veriyi tabloya dönüştürmek için pandas
df = pd.DataFrame(data)

print("-"*25 + " TÜM ARAÇ LİSTESİ " + "-"*25)
print(df)
print("\n" + "-"*68 + "\n")

# 2 - ANALİZ (hangi aracın ortalaması ne kadardır?)
marka_ortalamasi = df.groupby('Marka')['Fiyat'].mean().reset_index()

print("--- MARKA BAZLI ORTALAMA FİYATLAR ---")
print(marka_ortalamasi)

# 3 - Görselleştirme

# çözünürlük ayarı
plt.figure(figsize=(12, 7), dpi=120)

# renk paleti
ax = sns.barplot(x='Marka', y='Fiyat', data=df, palette='viridis', hue='Marka', legend=False, errorbar=None)

# başlık ve eksenler
plt.title('VAG Grubu: Marka Bazlı Fiyat Ortalamaları', fontsize=20, fontweight='bold', pad=20)
plt.xlabel('Marka', fontsize=14, labelpad=15)
plt.ylabel('Ortalama Fiyat (TL)', fontsize=14, labelpad=15)

# despine
sns.despine(left=True, bottom=True)

# y ekseni ayarı
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.1f} M₺'.format(x/1000000)))

# sütunlarda fiyat
for i in ax.containers:
    ax.bar_label(i, fmt='%.0f TL', padding=5, fontsize=12)

# grafiği göster veya kaydet
plt.tight_layout() # Öğelerin birbirine girmesini engeller
plt.show()