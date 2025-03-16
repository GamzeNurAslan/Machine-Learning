import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
notlar = np.random.randint(0, 101, 1000)

print("Ortalama:", np.mean(notlar))
print("En yüksek not:", np.max(notlar))
print("En düşük not:", np.min(notlar))
print("Standart Sapma:", np.std(notlar))

gecenler = notlar[notlar >= 50]
kalanlar = notlar[notlar < 50]

print("Geçen öğrencilerin sayısı:", len(gecenler))
print("Kalan öğrencilerin sayısı:", len(kalanlar))

plt.figure(figsize=(10,5))
plt.hist(notlar,bins=10, edgecolor="black", alpha=0.7)
plt.xlabel("Not Aralıkları")
plt.ylabel("Öğrenci Sayısı")
plt.title("Öğrenci Not Dağılımı")
plt.grid(True)
plt.show()

######################################

sirali_notlar = np.sort(notlar)

dusuk_dilim = sirali_notlar[:100]
yuksek_dilim = sirali_notlar[-100:]

print("En düşük %10 ortalama:", np.mean(dusuk_dilim))
print("En yuksek %10 ortalama:", np.mean(yuksek_dilim))

#####################################
