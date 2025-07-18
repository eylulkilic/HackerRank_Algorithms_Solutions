# Problem 5: diagonalDifference fonksiyonu ile matrislerde çapraz toplamın mutlak farkı

def diagonalDifference(arr):
    n = len(arr) # Matrisin boyutunu (n x n) alırız
    sol_saga_toplam = 0  # Sol üstten sağ alta doğru olan köşegenin toplamı
    sag_sola_toplam = 0  # Sağ üstten sol alta doğru olan köşegenin toplamı

    # Matris üzerinde döngü yaparak iki köşegenin elemanlarını toplarız
    for i in range(n):
        sol_saga_toplam += arr[i][i]
        sag_sola_toplam += arr[i][n - 1 - i]
    return abs(sol_saga_toplam - sag_sola_toplam) # İki köşegen toplamının mutlak farkı

if __name__ == '__main__':
    try:
        n = int(input("Kare matrisin boyutunu (n) girin: ").strip())
        if n <= 0:
            print("Matris boyutu pozitif bir tam sayı olmalıdır.")
            exit()
    except ValueError:
        print("Geçersiz giriş! Lütfen bir tam sayı girin.")
        exit()

    arr = [] # Matrisi depolamak için boş bir liste oluştururuz

    print(f"{n}x{n} matrisin elemanlarını girin. Her satırda {n} tane boşlukla ayrılmış tam sayı olsun:")
    for i in range(n):
        while True:
            try:
                row_input = input(f"{i + 1}. satırı girin: ").rstrip().split()
                if len(row_input) != n:
                    print(f"Hata: {n} adet sayı girmelisiniz. Lütfen tekrar deneyin.")
                    continue
                row = list(map(int, row_input))
                arr.append(row)
                break
            except ValueError:
                print("Geçersiz giriş! Lütfen sadece tam sayıları boşlukla ayırarak girin.")
            except Exception as e:
                print(f"Bir hata oluştu: {e}")

    sonuc = diagonalDifference(arr)
    print(f"Köşegenler arasındaki mutlak fark: {sonuc}")