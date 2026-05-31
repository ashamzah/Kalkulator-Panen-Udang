###################################################
## APLIKASI KALKULATOR PANEN UDANG V1
## Created by AS HAMZAH
## Blog : arissandohamzah.hantulaut.web.id
###################################################

dataPanen = [
    ["Panen1", 60, 93, 200, 72500], # Tipe Panen, DOC (day), Size (pcs/kg), Biomass (kg), Harga (Rp)
    ["Panen2", 70, 77, 200, 90000],
    ["Panen3", 80, 68, 200, 100000],
    ["Panen4", 90, 61, 200, 110000]
]

############################
## FUNGSI-FUNGSI
############################
def menu_utama(): #Fungsi memanggil menu utama
    pilihanMenu = input('''
    ============== APLIKASI PANEN UDANG ==============

    1. Report Data Panen
    2. Menambah Data Panen
    3. Mengubah Data Panen
    4. Menghapus Data Panen
    5. Menghitung Keuntungan Panen
    6. Exit Program

    Masukkan angka Menu yang ingin dijalankan (1-6): ''')
    return pilihanMenu

def submenu_1(): #Fungsi memanggil submenu 1. Report Data Panen
    pilihanMenu1=input('''
    ============== REPORT DATA PANEN ==============

    1. Report Seluruh Data Panen
    2. Report Data Panen Tertentu
    3. Kembali ke Menu Utama

    Masukkan angka Menu yang ingin dijalankan (1-3): ''')
    return pilihanMenu1

def submenu_2(): #Fungsi memanggil submenu 2. Menambah Data Panen
    pilihanMenu2=input('''
    ============== MENAMBAH DATA PANEN ==============

    1. Menambah Data Panen
    2. Kembali ke Menu Utama

    Masukkan angka Menu yang ingin dijalankan (1-2): ''')
    return pilihanMenu2

def submenu_3(): #Fungsi memanggil submenu 3. Mengubah Data Panen
    pilihanMenu3=input('''
    ============== MENGUBAH DATA PANEN ==============
    1. Mengubah Keseluruhan
    2. Mengubah Sebagian (Per Parameter)
    3. Kembali ke Menu Utama

    Masukkan angka Menu yang ingin dijalankan (1-3): ''')
    return pilihanMenu3

def submenu_4(): #Fungsi memanggil submenu 4. Menghapus Data Panen
    pilihanMenu4=input('''
    ============== MENGHAPUS DATA PANEN ==============

    1. Menghapus Data Panen
    2. Kembali ke Menu Utama

    Masukkan angka Menu yang ingin dijalankan (1-2): ''')
    return pilihanMenu4

def submenu_5(): #Fungsi memanggil submenu 5. Menghitung Keuntungan Panen
    pilihanMenu5=input('''
    ============== MENGHITUNG KEUNTUNGAN PANEN ==============

    1. Menghitung Keuntungan Panen
    2. Kembali ke Menu Utama

    Masukkan angka Menu yang ingin dijalankan (1-2): ''')
    return pilihanMenu5

def tampilkan_tabel_panen(): #Fungsi untuk menampilkan data panen
    if len(dataPanen) == 0: #Kondisi jika data panen kosong
        print("Data panen masih kosong.")
        return
    
    avg_doc = 0
    avg_size = 0
    sum_biomass = 0
    avg_harga = 0
    sum_total = 0

    print("=" * 70)
    print(f"{'No':<5}{'Panen':<10}{'DOC':<8}{'Size':<8}{'Biomass':<10}{'Harga':<10}{'Total':<12}")
    print("=" * 70)

    for i in range(len(dataPanen)):
        total = dataPanen[i][3] * dataPanen[i][4] # Menghitung Total Harga per Panen >> Biomass x Harga
        avg_doc += dataPanen[i][1] / len(dataPanen) # Menghitung Rata-Rata DOC Panen
        avg_size += dataPanen[i][2] / len(dataPanen) # Menghitung Rata-Rata Size Panen
        sum_biomass += dataPanen[i][3] # Menghitung Total Biomass Panen
        avg_harga += dataPanen[i][4] / len(dataPanen) # Menghitung Rata-Rata Harga per Kg Udang
        sum_total += dataPanen[i][3] * dataPanen[i][4] # Menghitung Total Income

        print(f"{i+1:<5}{dataPanen[i][0]:<10}{dataPanen[i][1]:<8}{dataPanen[i][2]:<8}{dataPanen[i][3]:<10}{dataPanen[i][4]:<10}{total:<12}")
    print("=" * 70)
    print(f"{' ':<5}{'Total':<10}{int(round(avg_doc,0)):<8}{int(round(avg_size,0)):<8}{int(round(sum_biomass)):<10}{int(round(avg_harga)):<10}{int(round(sum_total)):<12}")
    print("=" * 70)

def tampilkan_sebagian_data_panen(): #Fungsi untuk menampilkan sebagian data panen
    global namaPanen, indexPanen

    generate_no_panen()
    panenAda = cari_no_panen(namaPanen)

    if panenAda == True:
        indexPanen = daftarPanen.index(namaPanen)

        print("=" * 60)
        print(f"REPORT {dataPanen[indexPanen][0].upper()}".center(60))
        print("=" * 60)

        print(f"{'1. DOC':<35}: {dataPanen[indexPanen][1]:.0f} hari")
        print(f"{'2. Size':<35}: {dataPanen[indexPanen][2]:.0f} pcs/kg")
        print(f"{'3. Biomass':<35}: {dataPanen[indexPanen][3]:.0f} kg")
        print(f"{'4. Harga':<35}: Rp. {dataPanen[indexPanen][4]:.0f}/kg")
        print(f"{'5. Total Harga':<35}: Rp. {dataPanen[indexPanen][4] * dataPanen[indexPanen][3]:.0f}")
        print("=" * 60)

    else:
        print("Panen yang anda masukkan tidak tersedia !!!")

def input_data_panen(): #Fungsi untuk input baru maupun mengubah data panen
    global docPanen, sizePanen, biomassPanen, hargaPanen
    docPanen=int(input("Masukkan DOC Panen: "))
    sizePanen=int(input("Masukkan Size Panen: "))
    biomassPanen=int(input("Masukkan Biomass Panen: "))
    hargaPanen=int(input("Masukkan Harga/kg Udang Panen: "))

def generate_no_panen(): #Fungsi untuk menggenerate nomor panen
    global namaPanen, daftarPanen, daftarNoPanen, maxNoPanen
    namaPanen = f"Panen{noPanen}"
    daftarPanen = []
    daftarNoPanen = []

    for panen in dataPanen: #Proses urutan panen (no Panen)
        daftarPanen.append(panen[0])
        daftarNoPanen.append(int(panen[0].replace("Panen", "")))
    
    if len(daftarNoPanen) > 0:
        maxNoPanen = max(daftarNoPanen) #Kondisi menghitung maksimal nomor panen
    else:
        maxNoPanen = 0

def cari_no_panen(namaPanen): #Fungsi untuk mencari data panen 
    for panen in dataPanen:
        if panen[0] == namaPanen:
            return True
    return False

def hitung_panen(): #Fungsi untuk menghitung total panen dan keuntungan
    global totalBiomass, totalPakan, totalBiayaPakan, totalIncome, totalCost, profitLoss, profitLossKg, feedCostKg, grossMargin, roi, keterangan
    
    if len(dataPanen) == 0: #Kondisi jika data panen kosong
        print("Data panen masih kosong. Tidak bisa menghitung keuntungan.")
        return
    totalBiomass=0  #Menghitung Total Biomass
    for biomass in dataPanen: 
        totalBiomass+=biomass[3]
    
    totalPakan = fcr * totalBiomass #Menghitung Total Pakan dan Biaya Pakan
    totalBiayaPakan = hargaPakan * totalPakan

    totalIncome=0 #Menghitung Total Income
    for panen in dataPanen: 
        totalIncome+=panen[4]*panen[3]

    totalCost = totalBiayaPakan + listrik + gaji + kimia + lain #Menghitung Total Cost
    profitLoss = totalIncome - totalCost #Menghitung Profit atau Loss
    profitLossKg = profitLoss/totalBiomass #Menghitung Profit atau Loss /kg
    feedCostKg = totalBiayaPakan/totalBiomass #Menghitung Feed Cost/kg
    grossMargin = (profitLoss/totalIncome) * 100 #Menghitung Gross Margin
    roi = (profitLoss/totalCost) * 100 #Menghitung ROI

    #Keterangan Hasil Perhitungan
    if roi >= 30:
        keterangan = "Sangat Menguntungkan"
    elif roi >= 15:
        keterangan = "Menguntungkan"
    elif roi >= 0:
        keterangan = "Tipis / Perlu Efisiensi"
    else:
        keterangan = "Rugi"

def tampilkan_hasil_kalkulasi(): #Fungsi untuk menampilkan tabel kalkulasi
    if len(dataPanen) == 0: #Kondisi jika data panen kosong
        print("Data panen masih kosong. Tidak bisa menampilkan tabel kalkulasi.")
        return
    print("=" * 60)
    print("HASIL KALKULASI FINANSIAL".center(60))
    print("=" * 60)

    print(f"{'1. Total Income':<35}: Rp {totalIncome:.0f}")
    print(f"{'2. Total Cost':<35}: Rp {totalCost:.0f}")
    print(f"{'3. Feed Cost per kg Udang':<35}: Rp {feedCostKg:.0f}")
    print(f"{'4. Profit/Loss':<35}: Rp {profitLoss:.0f}")
    print(f"{'5. Profit/Loss per kg Udang':<35}: Rp {profitLossKg:.0f}")
    print(f"{'6. Gross Margin':<35}: {grossMargin:.2f}%")
    print(f"{'7. ROI':<35}: {roi:.2f}%")

    print("=" * 60)
    print(f"Berdasarkan hasil kalkulasi, panen udang anda: {keterangan}")
    print("=" * 60)
    
############################
## MENU APLIKASI
############################
while True:
    #MENU UTAMA
    pilihanMenu=menu_utama()

    #MENU READ : 1. REPORT DATA PANEN
    if pilihanMenu=='1': #Case saat user memilih report data panen
        while True:
            pilihanMenu1=submenu_1()
            if pilihanMenu1=='1': #Case saat user memilih sub menu Report Seluruh Data Panen
                tampilkan_tabel_panen()
            elif pilihanMenu1=='2': #Case saat user memilih sub menu Report Data Panen Tertentu
                noPanen = int(input("Masukkan No. Panen yang Ingin Dilihat: "))
                tampilkan_sebagian_data_panen()
            elif pilihanMenu1=='3': #Case saat user memilih sub menu Kembali ke Menu Utama
                break
            else:
                print("Pilihan yang anda masukkan tidak valid !!!") 

    #MENU CREATE : 2. MENAMBAH DATA PANEN
    elif pilihanMenu=='2': #Case saat user memilih menambah data panen
        while True:
            pilihanMenu2=submenu_2()
            if pilihanMenu2=='1': #Case saat user memilih sub menu Menambah Data Panen
                print(f"Silahkan Masukkan Data Panen")
                noPanen=int(input("Masukkan no. Panen: "))
                generate_no_panen()

                if namaPanen in daftarPanen: #Kondisi jika user memasukkan data panen yang sudah ada
                    print(f"Data {namaPanen} Sudah Ada")
                
                elif namaPanen not in daftarPanen and 1 <= noPanen <= maxNoPanen + 1: #Kondisi jika user memasukkan data panen baru
                    input_data_panen()
                    cek_simpan_data=input("Simpan Data Panen? y/n ")
                    if cek_simpan_data.lower() == 'y':
                        dataPanen.append([namaPanen,docPanen,sizePanen,biomassPanen,hargaPanen]) #Proses menambah data panen baru
                        print(f"Data {namaPanen} telah berhasil disimpan")
                    elif cek_simpan_data.lower() == 'n':
                        print(f"Data {namaPanen} tidak disimpan")
                    else:
                        print("Pilihan yang anda masukkan tidak valid !!!")
                else:
                    print("No. panen yang anda masukkan tidak sesuai dengan urutan !!!")

            elif pilihanMenu2=='2': #Case saat user memilih sub menu Kembali ke Menu Utama
                break
            else:
                print("Pilihan yang anda masukkan tidak valid !!!") 
    
    #MENU UPDATE : 3. MENGUBAH DATA PANEN
    elif pilihanMenu=='3': #Case saat user memilih mengubah data panen
        while True:
            pilihanMenu3=submenu_3()
            if pilihanMenu3=='1': #Case saat user memilih submenu 1. mengubah keseluruhan
                noPanen = int(input("Masukkan No. Panen yang Ingin Dilihat: "))
                tampilkan_sebagian_data_panen()
                generate_no_panen()
                panenAda = cari_no_panen(namaPanen)
                if panenAda == True:
                    indexPanen = daftarPanen.index(namaPanen)
                    cek_ubah_data=input("Ingin mengubah data panen? y/n ")
                    if cek_ubah_data.lower() == 'y':
                        input_data_panen()
                        dataPanen[indexPanen]=([namaPanen,docPanen,sizePanen,biomassPanen,hargaPanen]) #Proses menambah data panen baru
                        print(f"Data {namaPanen} Telah Berhasil Diubah")
                    elif cek_ubah_data.lower() == 'n':
                        print(f"Data {namaPanen} Tidak Diubah")
                    else:
                        print("Pilihan yang anda masukkan tidak valid !!!")
                
                else:
                    print("Panen yang anda masukkan tidak tersedia !!!")
            elif pilihanMenu3=='2': #Case saat user memilih submenu mengubah sebagian (per parameter)
                noPanen = int(input("Masukkan No. Panen yang Ingin Dilihat: "))
                tampilkan_sebagian_data_panen()
                generate_no_panen()
                panenAda = cari_no_panen(namaPanen)
                if panenAda == True:
                    indexPanen = daftarPanen.index(namaPanen)
                    indexKolom=int(input('''
                    List Kolom yang Dapat Diubah: 
                    1. DOC
                    2. Size
                    3. Berat
                    4. Harga
                    Masukkan No. Kolom yang Ingin Diubah (1-4): 
                    '''))
                    if 1 <= indexKolom <= 4: #Case ketika index kolom yang dipilih tersedia
                        valuePanen=int(input("Masukkan Data yang Ingin Diubah: "))
                        dataPanen[indexPanen][indexKolom]=valuePanen
                        print(f"Data {namaPanen} Telah Berhasil Diubah")
                    else:
                        print("Kolom yang anda masukkan tidak valid !!!")
                else:
                    print("Panen yang anda masukkan tidak tersedia !!!")
            elif pilihanMenu3=='3': #Case saat user memilih sub menu Kembali ke Menu Utama
                break
            else:
                print("Pilihan yang anda masukkan tidak valid !!!") 
            
    #MENU DELETE : 4. MENGHAPUS DATA PANEN
    elif pilihanMenu=='4': #Case saat user memilih menghapus data panen
        while True:
            pilihanMenu4=submenu_4()
            if pilihanMenu4=='1': #Case saat user memilih submenu 1. menghapus data panen
                print(f"Silahkan Masukkan Data Panen yang Ingin Anda Hapus")
                noPanen=int(input("Masukkan no. Panen: "))
                generate_no_panen()
                panenAda = cari_no_panen(namaPanen)

                if panenAda == True: #Kondisi jika nama panen ada di daftar panen
                    tampilkan_sebagian_data_panen()
                    cek_hapus_data=input("Ingin menghapus data panen? y/n ")
                    if cek_hapus_data.lower() == 'y':
                        del dataPanen[indexPanen] #Proses menghapus panen yang dipilih
                        print(f"Data {namaPanen} Sudah Berhasil Dihapus")
                    elif cek_hapus_data.lower() == 'n':
                        print(f"Data {namaPanen} Tidak Dihapus")
                    else:
                        print("Pilihan yang anda masukkan tidak valid !!!")
                else: #Kondisi jika nama panen tidak ada di daftar panen
                    print(f"Data {namaPanen} tidak ada")

            elif pilihanMenu4=='2': #Case saat user memilih submenu 2. Kembali ke Menu Utama
                break
            else:
                print("Pilihan yang anda masukkan tidak valid !!!") 

    #MENU HITUNG : 5. MENGHITUNG KEUNTUNGAN PANEN
    elif pilihanMenu=='5': #Case saat user memilih menghitung keuntungan panen
        while True:
            pilihanMenu5=submenu_5()
            if pilihanMenu5=='1': #Case saat user memilih submenu 1. menghitung keuntungan panen
                if pilihanMenu5=='1':
                    if len(dataPanen) == 0:
                        print("Data panen masih kosong. Tidak bisa menghitung keuntungan.")
                        continue
                    fcr = float(input("Silahkan input nilai FCR: "))
                    hargaPakan = int(input("Silahkan masukkan harga pakan per kg: "))
                    listrik = int(input("Silahkan masukkan total harga listrik: "))
                    gaji = int(input("Silahkan masukkan total harga gaji karyawan: "))
                    kimia = int(input("Silahkan masukkan total harga bahan kimia: "))
                    lain = int(input("Silahkan masukkan total harga lainnya: "))
                    
                    hitung_panen()
                    tampilkan_hasil_kalkulasi()
            elif pilihanMenu5=='2': #Case saat user memilih submenu 2. Kembali ke Menu Utama
                break
            else:
                print("Pilihan yang anda masukkan tidak valid !!!") 

    #MENU CLOSE : 6. KELUAR DARI APLIKASI
    elif pilihanMenu=='6': #Case saat user memilih untuk keluar dari Aplikasi
        cek_keluar_aplikasi=input("Anda yakin ingin keluar? y/n ")
        if cek_keluar_aplikasi.lower() == 'y':
            print("Terimakasih sudah menggunakan aplikasi ini !!!")
            break
        elif cek_keluar_aplikasi.lower() == 'n':
            continue
        else:
            print("Pilihan yang anda masukkan tidak valid !!!")
    else:
        print("Pilihan yang anda masukkan tidak valid !!!")
            