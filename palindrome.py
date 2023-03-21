def cek_palindrome(kalimat):
    kalimat = kalimat.lower()

    kalimat_bersih =""
    for karakter in kalimat:
        if karakter.isalpha():
            kalimat_bersih = kalimat_bersih + karakter

    kalimat_bersih_balik = kalimat_bersih[::-1]

kalimat = input("Masukkan kalimat: ")
hasil = cek_palindrome(kalimat)
if hasil == True:
    print("Palindrome!")
else:
    print("Bukan Palindrome!")
