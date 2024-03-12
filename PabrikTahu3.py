class Node:
    def __init__(self, idd, bulan, tahun, saldo_tetap, pemasukan, pengeluaran):
        self.idd = idd
        self.bulan = bulan
        self.tahun = tahun
        self.saldo = saldo_tetap
        self.pemasukan = pemasukan
        self.pengeluaran = pengeluaran
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.current_id = 1  # ID pertama dimulai dari 1

    def tambah_data_kas(self, bulan, tahun, saldo_tetap, pemasukan, pengeluaran):
        new_node = Node(self.current_id, bulan, tahun, saldo_tetap, pemasukan, pengeluaran)
        self.current_id += 1  # Meningkatkan ID untuk entri berikutnya
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def dapatkan_data_kas(self, bulan, tahun):
        current = self.head
        while current:
            if current.bulan == bulan and current.tahun == tahun:
                return current
            current = current.next
        return None

    def update_data_kas(self, bulan, tahun, pemasukan=None, pengeluaran=None, saldo=None):
        current = self.head
        while current:
            if current.bulan == bulan and current.tahun == tahun:
                if pemasukan is not None:
                    current.pemasukan = pemasukan
                if pengeluaran is not None:
                    current.pengeluaran = pengeluaran
                if saldo is not None:
                    current.saldo = saldo - current.pengeluaran + current.pemasukan
                return True
            current = current.next
        return False

    def hapus_data_kas(self, bulan, tahun):
        current = self.head
        if current.bulan == bulan and current.tahun == tahun:
            self.head = current.next
            return True
        while current.next:
            if current.next.bulan == bulan and current.next.tahun == tahun:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def quick_sort(self, criteria, ascending=True):
        if criteria == "idd":
            self.quick_sort_by_id(ascending)
        elif criteria == "tahun":
            self.quick_sort_by_year(ascending)

    def quick_sort_by_id(self, ascending=True):
        def partition(start, end):
            pivot = start
            left = start + 1
            right = end

            while True:
                while left <= right and self.get_node_at(left).idd <= self.get_node_at(pivot).idd:
                    left += 1
                while left <= right and self.get_node_at(right).idd >= self.get_node_at(pivot).idd:
                    right -= 1

                if left > right:
                    break
                else:
                    self.swap_nodes(left, right)

            self.swap_nodes(pivot, right)
            return right

        def quick_sort_recursive(start, end):
            if start >= end:
                return
            pivot_index = partition(start, end)
            quick_sort_recursive(start, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, end)

        quick_sort_recursive(0, self.length() - 1)

        if not ascending:
            self.reverse()

    def quick_sort_by_year(self, ascending=True):
        def partition(start, end):
            pivot = start
            left = start + 1
            right = end

            while True:
                while left <= right and self.get_node_at(left).tahun <= self.get_node_at(pivot).tahun:
                    if self.get_node_at(left).tahun == self.get_node_at(pivot).tahun:
                        if self.get_node_at(left).idd < self.get_node_at(pivot).idd:
                            left += 1
                            continue
                    left += 1
                while left <= right and self.get_node_at(right).tahun >= self.get_node_at(pivot).tahun:
                    if self.get_node_at(right).tahun == self.get_node_at(pivot).tahun:
                        if self.get_node_at(right).idd > self.get_node_at(pivot).idd:
                            right -= 1
                            continue
                    right -= 1

                if left > right:
                    break
                else:
                    self.swap_nodes(left, right)

            self.swap_nodes(pivot, right)
            return right

        def quick_sort_recursive(start, end):
            if start >= end:
                return
            pivot_index = partition(start, end)
            quick_sort_recursive(start, pivot_index - 1)
            quick_sort_recursive(pivot_index + 1, end)

        quick_sort_recursive(0, self.length() - 1)

        if not ascending:
            self.reverse()

    def get_node_at(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            count += 1
            current = current.next
        return None

    def swap_nodes(self, left, right):
        temp_left = self.get_node_at(left)
        temp_right = self.get_node_at(right)
        temp_left.bulan, temp_right.bulan = temp_right.bulan, temp_left.bulan
        temp_left.tahun, temp_right.tahun = temp_right.tahun, temp_left.tahun
        temp_left.saldo, temp_right.saldo = temp_right.saldo, temp_left.saldo
        temp_left.pemasukan, temp_right.pemasukan = temp_right.pemasukan, temp_left.pemasukan
        temp_left.pengeluaran, temp_right.pengeluaran = temp_right.pengeluaran, temp_left.pengeluaran

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

bukukas = LinkedList()
bukukas.tambah_data_kas("Desember", 2023, 1000000, 2000000, 1600000)

while True:
    print("Selamat Datang")
    print("Menu")
    print("1. Lihat Buku Kas")
    print("2. Tambahkan Data Baru")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    print("6. Sorting")
    pilih = str(input("Masukkan Pilihan : "))

    if pilih == "1":
        print("Data Kas Bulanan:")
        current = bukukas.head
        while current:
            print(f"ID: {current.idd}, Bulan: {current.bulan}, Tahun: {current.tahun}")
            print("Saldo:", current.saldo)
            print("Pemasukan:", current.pemasukan)
            print("Pengeluaran:", current.pengeluaran)
            print("")
            current = current.next

    elif pilih == "2":
        bulan = str(input("Masukkan Bulan Transaksi : "))
        tahun = int(input("Masukkan Tahun Transaksi : "))
        pemasukan = int(input("Masukkan Pemasukan Transaksi : "))
        pengeluaran = int(input("Masukkan Pengeluaran Transaksi : "))
        
        saldo_terakhir = 0
        if bukukas.head:
            current = bukukas.head
            while current.next:
                current = current.next
            saldo_terakhir = current.saldo        
        saldo_baru = saldo_terakhir + pemasukan - pengeluaran
        bukukas.tambah_data_kas(bulan, tahun, saldo_baru, pemasukan, pengeluaran)
        print("Data Berhasil Ditambahkan.")
        print("")

    elif pilih == "3":
        bulan_hapus = str(input("Masukkan Nama Bulan dari Data yang ingin Dihapus : "))
        tahun_hapus = int(input("Masukkan Tahun dari Data yang ingin dihapus : "))
        if bukukas.hapus_data_kas(bulan_hapus, tahun_hapus):
            print("Data kas berhasil dihapus.")
            print("")
        else:
            print("Data tidak ditemukan.")
            print("")

    elif pilih == "4":
        bulan_update = str(input("Masukkan Nama Bulan yang ingin Diperbarui : "))
        tahun_update = int(input("Masukkan Tahun yang ingin diperbarui : "))
        if bukukas.dapatkan_data_kas(bulan_update, tahun_update):
            pemasukan_baru = int(input("Masukkan Jumlah Pemasukan Baru : "))
            pengeluaran_baru = int(input("Masukkan Jumlah Pengeluaran Baru : "))
            saldo_baru = int(input("Masukkan Saldo Baru : "))
            if bukukas.update_data_kas(bulan_update, tahun_update, pemasukan_baru, pengeluaran_baru, saldo_baru):
                print("Data kas berhasil diperbarui.")
            else:
                print("Gagal memperbarui data.")
        else:
            print("Data tidak ditemukan.")

    elif pilih == "5":
        break

    elif pilih == "6":
        print("Menu Sorting:")
        print("1. Ascending berdasarkan ID")
        print("2. Descending berdasarkan ID")
        print("3. Ascending berdasarkan tahun")
        print("4. Descending berdasarkan tahun")
        sort_pilih = input("Pilih cara sorting: ")

        if sort_pilih == "1":
            bukukas.quick_sort("idd")
        elif sort_pilih == "2":
            bukukas.quick_sort("idd", ascending=False)
        elif sort_pilih == "3":
            bukukas.quick_sort("tahun")
        elif sort_pilih == "4":
            bukukas.quick_sort("tahun", ascending=False)

        print("Data Kas Bulanan setelah Sorting:")
        current = bukukas.head
        while current:
            print(f"ID: {current.idd}, Bulan: {current.bulan}, Tahun: {current.tahun}")
            print("Saldo:", current.saldo)
            print("Pemasukan:", current.pemasukan)
            print("Pengeluaran:", current.pengeluaran)
            print("")
            current = current.next
