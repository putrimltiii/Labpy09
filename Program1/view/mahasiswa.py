from data.mahasiswa import Mahasiswa
from view.input_form import InputForm

class MahasiswaView:
    def _init_(self):
        self.data_mahasiswa = []

    def tambah_data(self):
        nim, nama, jurusan = InputForm.input_data()
        mahasiswa = Mahasiswa(nim, nama, jurusan)
        self.data_mahasiswa.append(mahasiswa)
        print("Data berhasil ditambahkan.")

    def tampilkan_data(self):
        if not self.data_mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            for idx, mahasiswa in enumerate(self.data_mahasiswa, start=1):
                print(f"{idx}. {mahasiswa}")

    def hapus_data(self):
        self.tampilkan_data()
        try:
            idx = int(input("Pilih nomor data yang akan dihapus: ")) - 1
            if 0 <= idx < len(self.data_mahasiswa):
                del self.data_mahasiswa[idx]
                print("Data berhasil dihapus.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")

    def ubah_data(self):
        self.tampilkan_data()
        try:
            idx = int(input("Pilih nomor data yang akan diubah: ")) - 1
            if 0 <= idx < len(self.data_mahasiswa):
                nim, nama, jurusan = InputForm.input_data()
                self.data_mahasiswa[idx].nim = nim
                self.data_mahasiswa[idx].nama = nama
                self.data_mahasiswa[idx].jurusan = jurusan
                print("Data berhasil diubah.")
            else:
                print("Nomor tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")