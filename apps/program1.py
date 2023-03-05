from utils.app import App

def main():
    x = int(input("Masukkan bilangan pertama: "))
    y = int(input("Masukkan bilangan kedua: "))
    print(f"hasil dari {x} + {y} adalah {x+y}")


title = "========== Program 1: Program Menjumlahkan Dua Bilangan ==========\n" # untuk di tampilkan sebagai judul
name = "Program Penjumlahan" # untuk di tampilkan di list menu
description = ("Deskripsi untuk aplikasi\n", False) # deskripsi program
program1 = App(name=name, title=title, description=description, program=main)

if __name__ == "__main__":
    program1.start()
