import mysql.connector

import pandas as pd

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="spek_laptop"

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Contoh pernyataan SQL SELECT

select_query = "SELECT * FROM laptops"

 

# Eksekusi pernyataan SELECT

db_cursor.execute(select_query)

 

# Ambil hasil SELECT

results = db_cursor.fetchall()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()

laptops = {
    "brand": ["Asus", "Dell", "Apple"],
    "model": ["ZenBook 14", "XPS 13", "MacBook Pro 13"],
    "processor": ["Intel Core i7-1165G7", "Intel Core i7-1185G7", "Apple M1"],
    "ram": ["16GB DDR4", "16GB LPDDR4x", "8GB unified memory"],
    "storage": ["512GB SSD", "1TB SSD", "256GB SSD"],
    "graphics_card": ["Intel Iris Xe Graphics", "Intel Iris Xe Graphics", "Integrated 8-core GPU"],
    "display": ["14-inch FHD IPS", "13.4-inch UHD+ Touchscreen", "13.3-inch Retina"],
    "operating_system": ["Windows 10 Home", "Windows 11 Home", "macOS Monterey"],
    "weight": ["1.13 kg", "1.2 kg", "1.4 kg"]
}

# Konversi hasil SELECT menjadi dataframe pandas

df = pd.DataFrame(laptops)

# Simpan dataframe sebagai file Excel

df.to_excel("spek_laptop.xlsx", index=False, engine="openpyxl")

print("Data telah disimpan dalam file Excel 'spek_laptop.xlsx'") #csv / xlsx