"""
Aplikasi Sebaran COVID-19 di Jawa Barat
"""


def ekstraksi_data():
    """
    Update Terakhir: Kamis, 9 Des 2021 07.00
    Terkonfirmasi:
    Penambahan/Pengurangan Terkonfirmasi: 27
    Isolasi: 923
    Penambahan/Pengurangan Isolasi:  -37
    Sembuh: 692.383
    Penambahan/Pengurangan Sembuh: 64
    Meninggal: 14.737
    Penambahan/Pengurangan Meninggal: 0
    Kontak Erat: 572.979
    Masih Dikarantina: 25.744
    Discarded: 547.235
    Suspek: 216.886
    Isolasi Suspek: 8.568
    Discarded: 208.318
    Total Probable: 6.410
    Isolasi Probable: 276
    Sembuh Probable: 3.999
    Meninggal Probable: 2.135
    """
    hasil = dict()
    hasil['update'] = 'Kamis, 9 Des 2021 07.00'
    hasil['terkonfirmasi'] =
    return hasil


def tampilkan_data(result):
    print("Sebaran COVID-19 di Jawa Barat Berdasarkan Pikobar")
    print(f"Update Terakhir {result['update']}")
    pass


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
