#Fonksiyonu çağırıyoruz ve Alice ve Bob'un puanlarını başlangıçta 0 olarak ayarlıyoruz.
def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0
    
    #Her kategoriyi (i = 0, 1, 2 için) karşılaştırıyoruz ve eğer a[i] > b[i] ise, Alice'in puanını 1 artar, eğer a[i] < b[i] ise, Bob'un puanını 1 artar, eğer eşitse hiçbir şey yapmaz.
    for i in range(3):
        if a[i] > b[i]:
            alice_score += 1
        elif a[i] < b[i]:
            bob_score += 1
    
    #Sonuç olarak [Alice'in puanı, Bob'un puanı] dizisini döndürüyoruz.
    return [alice_score, bob_score]

a = (54, 43, 81)
b = (32, 91, 82)
print(compareTriplets(a, b))
