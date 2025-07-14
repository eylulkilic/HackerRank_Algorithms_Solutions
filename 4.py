#Problem4: aVerybigSum fonksiyonu ile dizideki büyük sayıları toplama
def aVeryBigSum(ar):
    return sum(ar)
ar_count = int(input("Lütfen eleman sayısını girin:").strip()) 
ar = list(map(int, input(f"Lütfen {ar_count} adet sayıyı boşluklarla ayırarak girin: ").rstrip().split())) #alınan listeyi okuyup boşluklara ayırıp tam sayıya dönüştürüyoruz
result = aVeryBigSum(ar)
print("Toplam:" , result)
