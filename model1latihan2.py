random_list = [105, 3.1, "Hello", 2.7, "World", 412, 5.5, "Al"]

int_dict = {}  # Dictionary untuk menyimpan nilai integer
float_tuple = ()  # Tuple untuk menyimpan nilai float
string_list = []  # List untuk menyimpan nilai string

for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item % 100) // 10
        ratusan = item // 100
        
        int_dict[item] = {"satuan": satuan, "puluhan": puluhan, "ratusan": ratusan}
    elif isinstance(item, float):
        float_tuple += (item,)
    elif isinstance(item, str):
        string_list.append(item)

# Menampilkan hasil
print("Data Integer (dalam Dictionary):")
for key, value in int_dict.items():
    print(f"{key}: {value}")

print("\nData Float (dalam Tuple):")
print(float_tuple)

print("\nData String (dalam List):")
print(string_list)