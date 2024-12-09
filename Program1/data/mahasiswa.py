class Mahasiswa:
    def _init_(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def _str_(self):
        return f"{self.nim} - {self.nama} ({self.jurusan})"