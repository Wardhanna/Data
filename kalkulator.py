def tambah(a,b):
    tambah = a + b
    return tambah

def kurang(a,b):
    kurang = a - b
    return kurang

def kali(a,b):
    kali = a * b
    return kali

def bagi(a,b):
    bagi = a / b
    return bagi

while True:
    print('\n\t============= KALKULATOR SEDERHANA =============')
    a = int(float(input('Masukan Bilangan Pertama : ')))
    b = int(float(input('Masukan Bilangan Kedua   : ')))
    print("\n1. Penjumlahan (+)\n2. Pengurangan (-)\n3. Perkalian (*)\n4. Pembagian (/)\n5. Batal (X)")
    c = input('\nPilih 1 sampai 5 : ')
    if c == '1':
        print('Penjumlahan: ',a,'+',b,'= ',tambah(a,b))
    elif c == '2':
        print('Pengurangan: ',a,'-',b,'= ',kurang(a,b))
    elif c == '3':
        print('Perkalian: ',a,'*',b,'= ',kali(a,b))
    elif c == '4':
        print('Pembagian: ',a,'//',b, '= ', bagi(a,b))
    elif c == '5':
        print('See You Next Time ^_^')
        break
    else:
        print('ANGKA NYA KAGAK NGOTAK WOE!!!')