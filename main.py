"""
Aplikasi Sebaran COVID-19 di Jawa Barat
"""
import covidwestjava

if __name__ == '__main__':
    print('Aplikasi utama')
    result = covidwestjava.ekstraksi_data()
    covidwestjava.tampilkan_data(result)
