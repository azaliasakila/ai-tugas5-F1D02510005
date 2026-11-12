
import json

# Membaca knowledge base
with open("kb_wifi.json", "r", encoding="utf-8") as file:
    knowledge = json.load(file)

print("=" * 45)
print(knowledge["judul"])
print("=" * 45)
 
# Menampilkan batas sistem
print("\nBatas Sistem:")
print(knowledge["batas"])

# Mengumpulkan fakta dari pengguna
fakta_user = set()

print("\n=== PERTANYAAN DIAGNOSIS ===")
print("Jawab dengan y (Ya) atau n (Tidak)")

pertanyaan = [
    "WiFi tidak aktif",
    "WiFi aktif",
    "nama jaringan tidak terlihat",
    "perangkat terhubung",
    "internet tidak dapat diakses",
    "perangkat lain juga mengalami gangguan",
    "perangkat lain tidak mengalami gangguan",
    "sinyal WiFi lemah",
    "koneksi membaik ketika perangkat didekatkan ke router"
]

for fakta in pertanyaan:
    jawaban = input(f"\nApakah {fakta}? (y/n): ").lower()

    if jawaban == "y":
        fakta_user.add(fakta)

# Proses Forward Chaining
print("\n=== HASIL DIAGNOSIS ===")

ditemukan = False

for aturan in knowledge["aturan"]:

    kondisi = aturan["jika"]
    mode = aturan["mode"]

    # Memeriksa kondisi aturan
    if mode == "dan":
        cocok = all(fakta in fakta_user for fakta in kondisi)
    elif mode == "atau":
        cocok = any(fakta in fakta_user for fakta in kondisi)
    else:
        cocok = False

    # Jika aturan terpenuhi
    if cocok:
        ditemukan = True

        print("\nAturan aktif:", aturan["id"])
        print("Diagnosis:", aturan["maka"])

        kode_sumber = aturan["sumber"]
        print("Referensi:", knowledge["sumber"][kode_sumber])

# Jika tidak ada aturan yang cocok
if not ditemukan:
    print("Belum ditemukan diagnosis yang sesuai.")

print("\n=== DIAGNOSIS SELESAI ===")
