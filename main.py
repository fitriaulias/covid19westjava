"""
Aplikasi Sebaran COVID-19 di Jawa Barat
"""


def ekstraksi_data():
    """
    Update Terakhir: Kamis, 9 Des 2021 07.00
    Terkonfirmasi: 708.189
    Penambahan/Pengurangan Terkonfirmasi: 27
    Isolasi: 923
    Penambahan/Pengurangan Isolasi:  -37
    Sembuh: 692.383
    Penambahan/Pengurangan Sembuh: 64
    Meninggal: 14.737
    Penambahan/Pengurangan Meninggal: 0
    Kontak Erat: 572.979
    Dikarantina: 25.744
    Discarded Kontak Erat: 547.235
    Suspek: 216.886
    Isolasi Suspek: 8.568
    Discarded Suspek: 208.318
    Total Probable: 6.410
    Isolasi Probable: 276
    Sembuh Probable: 3.999
    Meninggal Probable: 2.135
    """
    hasil = dict()
    hasil['update'] = 'Kamis, 9 Des 2021 07.00'
    hasil['terkonfirmasi'] = 708.189
    hasil['perubahan_terkonfirmasi'] = 27
    hasil['isolasi'] = 923
    hasil['perubahan_isolasi'] = -37
    hasil['sembuh'] = 692.383
    hasil['perubahan_sembuh'] = 64
    hasil['meninggal'] = 14.737
    hasil['perubahan_meninggal'] = 0
    hasil['kontak_erat'] = 572.979
    hasil['dikarantina'] = 25.744
    hasil['discarded_kontak'] = 547.235
    hasil['suspek'] = 216.886
    hasil['isolasi_suspek'] = 8.568
    hasil['discarded_suspek'] = 208.318
    hasil['total_probable'] = 6.410
    hasil['isolasi_probable'] = 276
    hasil['sembuh_probable'] = 3.999
    hasil['meninggal_probable'] = 2135
    return hasil


def tampilkan_data(result):
    print("Sebaran COVID-19 di Jawa Barat Berdasarkan Pikobar")
    print(f"\nUpdate Terakhir {result['update']}")
    print(f"\nTotal Terkonfirmasi: {result['terkonfirmasi']}")
    print(f"Penambahan/Pengurangan Terkonfirmasi: {result['perubahan_terkonfirmasi']}")
    print(f"Isolasi: {result['isolasi']}")
    print(f"Penambahan/Pengurangan Isolasi: {result['perubahan_isolasi']}")
    print(f"Sembuh: {result['sembuh']}")
    print(f"Penambahan/Pengurangan Sembuh: {result['perubahan_sembuh']}")
    print(f"Meninggal: {result['meninggal']}")
    print(f"Penambahan/Pengurangan Meninggal: {result['perubahan_meninggal']}")
    print("\nKontak Erat")
    print(f"Total Kontak Erat: {result['kontak_erat']}")
    print(f"Masih Dikarantina: {result['dikarantina']}")
    print(f"Discarded: {result['discarded_kontak']}")
    print("\nSuspek")
    print(f"Total Suspek: {result['suspek']}")
    print(f"Isolasi/Dalam Perawatan: {result['isolasi_suspek']}")
    print(f"Discarded: {result['discarded_suspek']}")
    print("\nProbable")
    print(f"Total Probable: {result['total_probable']}")
    print(f"Isolasi/Dalam Perawatan: {result['isolasi_probable']}")
    print(f"Selesai Isolasi/Sembuh: {result['sembuh_probable']}")
    print(f"Meninggal: {result['meninggal_probable']}")
    pass


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
