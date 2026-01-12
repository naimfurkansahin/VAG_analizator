'''
naimfurkansahin@gmail.com

VAG grubu araçların piyasa analizini yapan ve alım satımda yarar sağlaması adına
grafik çizdiren bir python programı.
'''


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#geçici veri seti oluşturdum.
data = {
    'Marka': ['Seat', 'Seat', 'Seat', 'Volkswagen', 'Volkswagen', 'Volkswagen', 'Cupra', 'Cupra'],
    'Model': ['Leon', 'Leon', 'Leon', 'Golf', 'Golf', 'Golf', 'Formentor', 'Formentor'],
    'Paket': ['FR', 'Style', 'FR', 'Life', 'R-Line', 'Life', 'VZ', 'VXL'],
    'Yil': [2020, 2019, 2021, 2020, 2021, 2019, 2022, 2023],
    'KM': [45000, 60000, 30000, 50000, 25000, 70000, 15000, 5000],
    'Fiyat': [1150000, 950000, 1300000, 1250000, 1600000, 1050000, 2100000, 2400000],
    'Hasar_Kaydi': [0, 5000, 0, 0, 0, 12000, 0, 0]
}