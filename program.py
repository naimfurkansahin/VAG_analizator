import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# --- AYARLAR ---
sns.set_theme(style="whitegrid", context="talk", font_scale=0.9)

# --- VERİ OKUMA ---
try:
    df = pd.read_csv('arabalar.csv')
except FileNotFoundError:
    print("CSV bulunamadı!")
    exit()

# --- GÖRSELLEŞTİRME ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16), dpi=150) # Boyutu biraz uzattım

# 1. GRAFİK
sns.barplot(x='Marka', y='Fiyat', data=df, palette='viridis', hue='Marka', legend=False, errorbar=None, ax=ax1)
ax1.set_title('Marka Bazlı Ortalama Fiyatlar', fontweight='bold', pad=20)
ax1.set_xlabel('') # Üstteki grafikte 'Marka' yazmasına gerek yok, zaten belli. Sildik, yer açıldı.
ax1.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.1f} M₺'.format(x/1000000)))
for i in ax1.containers:
    ax1.bar_label(i, fmt='%.0f TL', padding=3, fontsize=10)

# 2. GRAFİK
sns.scatterplot(data=df, x='KM', y='Fiyat', hue='Marka', s=250, palette='deep', alpha=0.8, ax=ax2)
ax2.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0) # Lejant dışarıda

ax2.set_title('Fırsat Matrisi (Sol Alt = Kelepir)', fontweight='bold', color='darkred', pad=20)
ax2.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.1f} M₺'.format(x/1000000)))
ax2.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f} bin'.format(x/1000)))

# Etiketler
for i in range(df.shape[0]):
    ax2.text(
        df.KM[i] + 2000, # Biraz daha sağa
        df.Fiyat[i] + 10000, 
        df.Model[i], 
        horizontalalignment='left', 
        size=9, 
        color='black', 
        weight='semibold'
    )

sns.despine(left=True, bottom=True)

# DÜZENLEME: Boşlukları mükemmel ayarla
plt.tight_layout(rect=[0, 0, 1, 0.96]) # Tepeden boşluk
plt.subplots_adjust(hspace=0.3) # İki grafik arasını aç

# --- KAYDETME (Bu klasöre resim olarak indirir) ---
plt.savefig('vag_analiz_raporu.png', bbox_inches='tight', dpi=300)
print("Rapor 'vag_analiz_raporu.png' olarak kaydedildi!")

plt.show()