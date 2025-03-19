nama = input("Masukan Nama: ")
nik = int(input("Masukan NIK: "))
status = input("Masukan Status Pegawai (Tetap/Honor): ").lower()
gol = input("Masukan golongan (A/B/C): ").lower()

liststatus = {"honor":750000, "tetap":1000000}
listbonus = {"a":150000, "b":275000, "c":480000}

for a in liststatus:
    if status == a:
        for b in listbonus:
            if gol == b:
                break
        break
    listbonus["a"] = 200000
    listbonus["b"] = 400000
    listbonus["c"] = 550000

gajinya = liststatus[status]
bonus = listbonus[gol]
gajitotal = int(gajinya + bonus)

print("Nama:", nama)
print("NIK:", nik)
print("Gaji:", gajinya)
print("Bonus:", bonus)
print("Gaji Total:", gajitotal)
