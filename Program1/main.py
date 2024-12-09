class InputForm:
    def __init__(self):
        self.mahasiswa = []

    def tambah_data(self, nama, nim):
        self.mahasiswa.append({'nama': nama, 'nim': nim})
        print(f"Data mahasiswa {nama} dengan NIM {nim} berhasil ditambahkan.")

    def hapus_data(self, nim):
        for mhs in self.mahasiswa:
            if mhs['nim'] == nim:
                self.mahasiswa.remove(mhs)
                print(f"Data mahasiswa dengan NIM {nim} berhasil dihapus.")
                return
        print(f"Data mahasiswa dengan NIM {nim} tidak ditemukan.")

    def ubah_data(self, nim, nama_baru):
        for mhs in self.mahasiswa:
            if mhs['nim'] == nim:
                mhs['nama'] = nama_baru
                print(f"Data mahasiswa dengan NIM {nim} berhasil diubah menjadi {nama_baru}.")
                return
        print(f"Data mahasiswa dengan NIM {nim} tidak ditemukan.")

    def tampilkan_data(self):
        if not self.mahasiswa:
            print("Tidak ada data mahasiswa.")
            return
        print("Data Mahasiswa:")
        for mhs in self.mahasiswa:
            print(f"NIM: {mhs['nim']}, Nama: {mhs['nama']}")

def main():
    form = InputForm()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Ubah Data")
        print("4. Tampilkan Data")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            form.tambah_data(nama, nim)
        elif pilihan == '2':
            nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
            form.hapus_data(nim)
        elif pilihan == '3':
            nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
            nama_baru = input("Masukkan nama baru mahasiswa: ")
            form.ubah_data(nim, nama_baru)
        elif pilihan == '4':
            form.tampilkan_data()
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()