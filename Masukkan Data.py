import mysql.connector

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="spek_laptop"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan data laptops yang ingin dimasukkan

laptops = [

    {
        "brand": "Asus",
        "model": "ZenBook 14",
        "processor": "Intel Core i7-1165G7",
        "ram": "16GB DDR4",
        "storage": "512GB SSD",
        "graphics_card": "Intel Iris Xe Graphics",
        "display": "14-inch FHD IPS",
        "operating_system": "Windows 10 Home",
        "weight": "1.13 kg"
    },
    {
        "brand": "Dell",
        "model": "XPS 13",
        "processor": "Intel Core i7-1185G7",
        "ram": "16GB LPDDR4x",
        "storage": "1TB SSD",
        "graphics_card": "Intel Iris Xe Graphics",
        "display": "13.4-inch UHD+ Touchscreen",
        "operating_system": "Windows 11 Home",
        "weight": "1.2 kg"
    },
    {
        "brand": "Apple",
        "model": "MacBook Pro 13",
        "processor": "Apple M1",
        "ram": "8GB unified memory",
        "storage": "256GB SSD",
        "graphics_card": "Integrated 8-core GPU",
        "display": "13.3-inch Retina",
        "operating_system": "macOS Monterey",
        "weight": "1.4 kg"
    }

]

# Perulangan untuk memasukkan data ke dalam tabel

# Inisialisasi list kosong untuk menyimpan data laptop
laptops = []

# Menentukan jumlah data yang ingin dimasukkan
jumlah_laptop = 3  # Misalnya, ingin memasukkan 3 laptop

for i in range(jumlah_laptop):
    brand = input(f"Masukkan brand laptop ke-{i + 1}: ")
    model = input(f"Masukkan model laptop ke-{i + 1}: ")
    processor = input(f"Masukkan processor laptop ke-{i + 1}: ")
    ram = input(f"Masukkan RAM laptop ke-{i + 1}: ")
    storage = input(f"Masukkan storage laptop ke-{i + 1}: ")
    graphics_card = input(f"Masukkan graphics card laptop ke-{i + 1}: ")
    display = input(f"Masukkan display laptop ke-{i + 1}: ")
    operating_system = input(f"Masukkan operating system laptop ke-{i + 1}: ")
    weight = input(f"Masukkan weight laptop ke-{i + 1}: ")

    # Membuat dictionary untuk setiap laptop dan menambahkannya ke list laptops
    laptop = {
        "brand": brand,
        "model": model,
        "processor": processor,
        "ram": ram,
        "storage": storage,
        "graphics_card": graphics_card,
        "display": display,
        "operating_system": operating_system,
        "weight": weight
    }
    laptops.append(laptop)

print("Data laptop yang dimasukkan:")
print(laptops)