# Data nilai siswa
dataNilai=[
    {
        "absen":1,
        "nama":"Amel Putri",
        "nilaiMath":67,
        "nilaiIPA":89,
        "nilaiIPS":80
    },
    {
        "absen":2,
        "nama":"Budi Wahyu",
        "nilaiMath":80,
        "nilaiIPA":85,
        "nilaiIPS":70
    },
    {
        "absen":3,
        "nama":"Cahyo Rizal",
        "nilaiMath":97,
        "nilaiIPA":90,
        "nilaiIPS":92
    }
]

# Function to print all data
def printAllData():
    jmlData=int(len(dataNilai))
    print("Absen\t|Nama\t\t\t|NilaiMath\t|Nilai IPA\t|Nilai IPS")
    for i in range(jmlData):
        print(f"{dataNilai[i]["absen"]}\t|{dataNilai[i]["nama"]}\t\t|{dataNilai[i]["nilaiMath"]}\t\t|{dataNilai[i]["nilaiIPA"]}\t\t|{dataNilai[i]["nilaiIPS"]}")

# Function for data nilai siswa
def menu1():
    jmlData=int(len(dataNilai))
    after=""
    lihatDetail=""
    avgNilai=""

    while True:
        print('''
        1. Tampilkan seluruh data.
        2. Tampilkan detail data siswa
        3. Tampilkan rata-rata nilai siswa.
        4. Kembali ke menu utama.
        ''')
        print("-"*100)

        submenu=int(input("Masukkan angka menu yang ingin anda jalankan: "))

        if submenu==1:
            printAllData()

            after=input("Apakah anda mau masih mau menampilkan data? (yes/no): ")
            if after.lower()=="yes":
                # menuBack=="yes"
                print("-"*100)
                continue
            else:
                break
        
        elif submenu==2:
            absenExisting=[dataNilai[i]["absen"] for i in range(int(len(dataNilai)))]
            printAllData()
            print("-"*100)

            while True:
                try:
                    lihatDetail=int(input("Masukkan angka absen yang anda mau lihat datanya: "))
                    while lihatDetail not in absenExisting:
                        print("Angka absen anda tidak valid. Masukkan angka yang ada pada data")
                        lihatDetail=int(input("Masukkan angka absen yang anda mau lihat datanya: "))
                    
                    avgNilai=round((dataNilai[lihatDetail-1]["nilaiMath"]+dataNilai[lihatDetail-1]["nilaiIPA"]+dataNilai[lihatDetail-1]["nilaiIPS"])/3,2)
                    print("Absen\t|Nama\t\t\t|NilaiMath\t|Nilai IPA\t|Nilai IPS\t|Rata-rata Nilai")
                    print(f"{dataNilai[lihatDetail-1]["absen"]}\t|{dataNilai[lihatDetail-1]["nama"]}\t\t|{dataNilai[lihatDetail-1]["nilaiMath"]}\t\t|{dataNilai[lihatDetail-1]["nilaiIPA"]}\t\t|{dataNilai[lihatDetail-1]["nilaiIPS"]}\t\t|{avgNilai}")

                    break
                except:
                    print("Masukkan kembali data yang valid!")
                    continue

            after=input("Apakah anda mau masih mau menampilkan data? (yes/no): ")
            if after.lower()=="yes":
                print("-"*100)
                continue
            else:
                break

        
        elif submenu==3:
            sumMath,avgNilaiMath,sumIPA,avgNilaiIPA,sumIPS,avgNilaiIPS = [0,0,0,0,0,0]
        
            for i in range(jmlData):
                sumMath+=dataNilai[i]["nilaiMath"]
                sumIPA+=dataNilai[i]["nilaiIPA"]
                sumIPS+=dataNilai[i]["nilaiIPS"]

            avgNilaiMath=round(sumMath/jmlData,2)
            avgNilaiIPA=round(sumIPA/jmlData,2)
            avgNilaiIPS=round(sumIPS/jmlData,2)

            print("NilaiMat\t|Nilai IPA\t|Nilai IPS")
            print(f"{avgNilaiMath}\t\t|{avgNilaiIPA}\t\t|{avgNilaiIPS}")
            print(f"Rata-rata seluruh pelajaran adalah {round((avgNilaiMath+avgNilaiIPA+avgNilaiIPS)/3,2)}\n")

            after=input("Apakah anda mau masih mau menampilkan data? (yes/no): ")
            if after.lower()=="yes":
                print("-"*100)
                continue
            else:
                break
        
        elif submenu==4:
            break
        
        else:
            print("Masukkan angka menu yang valid!")
            print("-"*100)
            continue
    print("-"*100)

# Function for input nilai siswa
def menu2():
    after=""
    
    print("Berikut adalah data yang tersimpan saat ini")
    printAllData()
    print("-"*100)

    while True:
        absenExisting=[dataNilai[i]["absen"] for i in range(int(len(dataNilai)))]
        inputAbsen=absenExisting[0]

        while True:
            try:
                inputAbsen=int(input("Masukkan nomor absen: "))
                while inputAbsen in absenExisting:
                    print("Angka absen tidak boleh sama. Pastikan angka absen unik.")
                    inputAbsen=int(input("Masukkan nomor absen: "))

                inputNama=input("Masukkan nama siswa: ")
                inputNilaiMath=int(input("Input nilai Math: "))
                inputNilaiIPA=int(input("Input nilai IPA: "))
                inputNilaiIPS=int(input("Input nilai IPS: "))
                break
            except:
                print("Masukkan kembali data yang valid!")
                continue
            
        dataNilai.append({
            "absen":inputAbsen,
            "nama":inputNama,
            "nilaiMath":inputNilaiMath,
            "nilaiIPA":inputNilaiIPA,
            "nilaiIPS":inputNilaiIPS
            })
        
        after=input("Apakah anda mau menambah data lagi? (yes/no): ")   
        
        if after.lower()=="yes":
            continue
        else:
            print("Data anda telah tersimpan. Berikut adalah list data baru.")
            printAllData()
            break
    print("-"*100) 

# Function for edit nilai siswa
def menu3():
    print("Berikut adalah data yang tersimpan saat ini")
    printAllData()
    print("-"*100)  

    while True:
        absenExisting=[dataNilai[i]["absen"] for i in range(int(len(dataNilai)))]
        editAbsen=""
        while True:
            try:
                while editAbsen not in absenExisting:
                    editAbsen=int(input("Input absen siswa yang datanya akan diedit: "))
                break
            except:
                print("Absen harus berupa angka!")
                continue
        
        while True:
            inputMatpel=input("Masukkan nama mata pelajaran (Math, IPA, IPS): ")

            try:
                if inputMatpel.lower() == "math":
                    inputNilaiMath=int(input("Input nilai Math baru: "))
                    dataNilai[editAbsen-1].update({"nilaiMath":inputNilaiMath})
                elif inputMatpel.lower() == "ipa":
                    inputNilaiIPA=int(input("Input nilai IPA baru: "))
                    dataNilai[editAbsen-1].update({"nilaiIPA":inputNilaiIPA})
                elif inputMatpel.lower() == "ips":
                    inputNilaiIPS=int(input("Input nilai IPS baru: "))
                    dataNilai[editAbsen-1].update({"nilaiIPS":inputNilaiIPS})
                else:
                    print("Masukkan nama pelajaran yang valid!")
                    continue
            
                print("-"*100)
                print("Data anda telah tersimpan. Berikut adalah list data baru.")
                printAllData()
                break

            except:
                print("Masukkan nilai yang valid!")
        
        break    
    # print("-"*100)
        
def menu4():
    print("Berikut adalah data yang tersimpan saat ini.")
    printAllData()
    print("-"*100)  

    while True:
        absenExisting=[dataNilai[i]["absen"] for i in range(int(len(dataNilai)))]
        cek=""
        delAbsen=""
        while True:
            try:
                while delAbsen not in absenExisting:
                    delAbsen=int(input("Input absen siswa yang datanya akan dihapus: "))
                break
            except:
                print("Absen harus berupa angka!")
                continue 

        while True:
            try:
                cek=input(f"Apakah anda yakin untuk menghapus absen {delAbsen} (yes/no)? ")
                if cek.lower()=="yes":
                   del dataNilai[delAbsen-1]
                   print("-"*100)
                   print("Data anda telah tersimpan. Berikut adalah list data baru.")
                   printAllData() 
                   break
                elif cek.lower()=="no":
                    print("Anda akan kembali ke menu utama.")
                    break
            except:
                print("Masukkan input yang benar! (yes/no)")
                continue
        
        break         


while True:
    menu=["1. Menampilan data nilai siswa", 
          "2. Input nilai siswa",
          "3. Edit nilai siswa",
          "4. Menghapus nilai siswa",
          "5. Exit program"]
    
    print("Halo Pak/Bu Guru! Selamat datang di Data Siswa SD Musim Semi :)")
    for item in menu:
        print(item)
    inputMenu=int(input("Masukkan angka menu yang ingin dijalankan: "))
    print("\n")

    if inputMenu==1:
        print("-"*100)  
        menu1()
        print("-"*100)  
    elif inputMenu==2:
        print("-"*100)  
        menu2()
        print("-"*100)  
    elif inputMenu==3:
        print("-"*100)  
        menu3()
        print("-"*100)  
    elif inputMenu==4:
        print("-"*100)  
        menu4()
        print("-"*100)  
    elif inputMenu==5:
        print("-"*100)  
        print("Terima kasih sudah menggunakan Data Siswa SD Musim Semi!")
        break
    else:
        print("Masukkan menu yang valid!")

