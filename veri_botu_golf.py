import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time

# fiyatı temizleme fonksiyonu ( noktalardan )
def fiyati_duzelt(fiyat_metni):
    try:
        if not fiyat_metni: return 0
        temiz = fiyat_metni.replace("TL", "").replace(".", "").replace(",", "").strip()
        return int(temiz)
    except:
        return 0

# KM temizleme fonksiyonu ( noktalardan )
def km_duzelt(km_metni):
    try:
        if not km_metni: return 0
        temiz = km_metni.replace("Km", "").replace(".", "").strip()
        return int(temiz)
    except:
        return 0

if __name__ == '__main__':
    print("Bot başlatılıyor...")
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)

    try:
        # VW GOLF ilanına gidiyoruz
        url = "https://www.sahibinden.com/volkswagen-golf"
        print(f"Siteye gidiliyor: {url}")
        driver.get(url)

        # captcha ya karşı manuel müdahale için
        print("\n" + "!"*50)
        print("LÜTFEN TARAYICIYI KONTROL ET!")
        print("1. Captcha çıktıysa çöz.")
        print("2. İlanlar ekrana gelince buraya gel ve ENTER'a bas.")
        input("Hazır olduğunda ENTER'a bas >> ")
        print("!"*50 + "\n")
        # ------------------------------

        print("Veriler çekiliyor...")
        ilanlar = driver.find_elements(By.CLASS_NAME, "searchResultsItem")
        
        toplanan_veri = []

        for ilan in ilanlar:
            try:
                # başlık
                basliklar = ilan.find_elements(By.CLASS_NAME, "searchResultsTitleValue")
                if not basliklar: continue # Reklam satırıysa geç
                baslik = basliklar[0].text.replace(",", "-") # CSV bozulmasın diye virgülü tire yap

                # fiyat
                fiyatlar = ilan.find_elements(By.CLASS_NAME, "searchResultsPriceValue")
                ham_fiyat = fiyatlar[0].text if fiyatlar else "0"
                fiyat = fiyati_duzelt(ham_fiyat)

                # özellikler (Yıl ve KM)
                ozellikler = ilan.find_elements(By.CLASS_NAME, "searchResultsAttributeValue")
                yil = ozellikler[0].text if len(ozellikler) > 0 else "0"
                ham_km = ozellikler[1].text if len(ozellikler) > 1 else "0"
                km = km_duzelt(ham_km)

                print(f"Çekildi: {yil} Model - {km} KM - {fiyat} TL")
                # veriyi listeye ekle (Marka 'VW', Model 'Golf' olarak sabitliyoruz şimdilik)
                toplanan_veri.append(f"VW,Golf,{baslik},{yil},{km},{fiyat}")

            except Exception as e:
                continue

        # dosyaya Kaydet
        with open("sahibinden_verisi_golf.csv", "w", encoding="utf-8") as f:
            f.write("Marka,Model,Paket,Yil,KM,Fiyat\n") # Başlıklar
            for satir in toplanan_veri:
                f.write(satir + "\n")
                
        print(f"\nBaşarılı! Toplam {len(toplanan_veri)} ilan 'sahibinden_verisi_golf.csv'ye kaydedildi.")

    except Exception as e:
        print("Hata oluştu:", e)

    finally:
        driver.quit()