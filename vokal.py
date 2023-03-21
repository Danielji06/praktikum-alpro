def hitung_vokal(kalimat):
    vokal = "aiueoAIUEO"
    jumlah = 0
    for karakter in kalimat:
        if karakter in vokal:
            jumlah = jumlah + 1
    return jumlah

def hitung_whitespaces(kalimat):
    jumlah = 0
    for karakter in kalimat:
        if karakter.isspace() == True:
            jumlah = jumlah + 1
    return jumlah

def hitung_konsonan(kalimat):
        vokal = "aiueoAIUEO"
        jumlah = 0
        for karakter in kalimat:
             if karakter not in vokal and karakter.isalpha():
                  jumlah = jumlah + 1
        return jumlah

kalimat = input("Masukkan sebuah kalimat: ")

jumlah_vokal = hitung_vokal(kalimat)
jumlah_whitespaces = hitung_whitespaces(kalimat)
jumlah_konsonan = hitung_vokal(kalimat)

print(f"Jumlah huruf vokal: {jumlah_vokal}")
print(f"Jumlah huruf whitespaces: {jumlah_whitespaces}")
print(f"Jumlah huruf konsonan: {jumlah_konsonan}")