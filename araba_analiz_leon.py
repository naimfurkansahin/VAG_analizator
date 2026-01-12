import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# ayar
sns.set_theme(style="whitegrid", context="talk", font_scale=0.9)

# veri read
try:
    # veri_bot un csv sini okuyoruz
    df = pd.read_csv('sahibinden_verisi_leon.csv')
    print(f"Harika! {len(df)} adet araç analiz ediliyor...")
except FileNotFoundError:
    print("HATA: 'sahibinden_verisi_leon.csv' bulunamadı! Önce botu çalıştırıp veri çekmelisin.")
    exit()

# görselleştirme
fig, ax = plt.subplots(figsize=(12, 8), dpi=120)

# fırsat matrisi
sns.scatterplot(
    data=df, 
    x='KM', 
    y='Fiyat', 
    hue='Yil', # renk yıla göre değişsin
    palette='viridis', 
    s=200, 
    alpha=0.8, 
    ax=ax
)

ax.set_title('SEAT Leon Piyasa Analizi (Gerçek Veri)', fontweight='bold', color='darkred', pad=20)
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f} TL'.format(x)))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f} km'.format(x)))

# etikete paket ya da ilan isimleri
for i in range(len(df)):
    try:
        # ama kısaltalım paket isimlerini
        etiket = df.Paket[i][:20] 
        ax.text(
            df.KM[i], 
            df.Fiyat[i], 
            etiket, 
            horizontalalignment='left', 
            size=8, 
            color='black', 
            weight='light'
        )
    except:
        pass

sns.despine()
plt.tight_layout()
plt.show()