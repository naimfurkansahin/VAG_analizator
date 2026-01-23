import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

ctk_bg = '#242424'      # Arka plan (Koyu Gri)
text_color = '#ffffff'  # Tam Beyaz (Yazılar için)

# global font matplotlib
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans', 'Liberation Sans'] # Modern font ailesi
plt.rcParams['axes.edgecolor'] = ctk_bg # Çerçeve rengi (görünmez olsun)
plt.rcParams['text.color'] = text_color 

# veriread
try:
    df = pd.read_csv('sahibinden_verisi_leon.csv')
    print(f"Harika! {len(df)} adet araç analiz ediliyor...")
except FileNotFoundError:
    print("Veri yok, örnek veri ile devam ediliyor...")
    data = {'KM': [15000, 45000, 120000, 80000, 20000], 
            'Fiyat': [1200000, 1050000, 850000, 950000, 1150000], 
            'Yil': [2022, 2020, 2017, 2019, 2021], 
            'Paket': ['FR 1.5 eTSI', 'Style', 'FR 1.4 TSI', 'Xcellence', 'FR Plus']}
    df = pd.DataFrame(data)

# görselleştirme
fig, ax = plt.subplots(figsize=(12, 8), dpi=120)
fig.patch.set_facecolor(ctk_bg)
ax.set_facecolor(ctk_bg)

#grid ayqrı
ax.grid(color='white', linestyle=':', linewidth=0.3, alpha=0.2, zorder=0)

# scatter plot
sns.scatterplot(
    data=df, 
    x='KM', 
    y='Fiyat', 
    hue='Yil', 
    palette='cool', # parlak palet
    s=250, 
    alpha=0.9, 
    edgecolor=ctk_bg,
    linewidth=1.5,
    ax=ax,
    zorder=2
)

ax.set_title('SEAT Leon Piyasa Analizi', fontweight='bold', color='white', pad=25, fontsize=18)

# eksen isimleri
ax.set_xlabel('KM', color='white', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('Fiyat', color='white', fontsize=12, fontweight='bold', labelpad=10)

# eksen sayıları
ax.tick_params(axis='both', colors='white', labelsize=10, length=0) # length=0 çentikleri siler

# format ayarları
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f} TL'.format(x)))
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f} km'.format(x)))

# etiketller
for i in range(len(df)):
    try:
        etiket = df.Paket[i][:20] 
        ax.text(
            df.KM[i], 
            df.Fiyat[i], 
            etiket, 
            horizontalalignment='left', 
            size=8, 
            color='#cccccc', # hafif gri
            verticalalignment='bottom'
        )
    except:
        pass

sns.despine(left=True, bottom=True) #çerçeveleri temizliyoruz

plt.tight_layout()
plt.show()