import random
dogruyer = 0
yanlisyer = 0
sayi = random.randrange(10,99)
# Programın aynı basamaklı sayı üretmesi durumunda bir döngü ile bunu kontrol ederek tekrar rastgele bir sayı üretilmesini
# ve sayı değişkenine her zaman iki basamak farklı olacak şekilde atama yapılmasını sağladım.
while (sayi% 10 == sayi//10):
    sayi = random.randrange(10,99)

tahmin = int(input(" 10 ile 98 arasında bir sayı giriniz ( 10 ve 98 dahil): "))

if tahmin <= 98 and tahmin >= 10 and tahmin %10 != tahmin //10:
    
    if tahmin % 10 == sayi % 10 :
        dogruyer += 1
    else:
        yanlisyer -= 1
        
    if tahmin // 10 == sayi//10:
        dogruyer += 1
    else:
        yanlisyer -= 1

    if dogruyer  == 2:
        print("Tebrikler! Doğru tahmin yaptınız..")

    print("Doğru yer: "+str(dogruyer) + " Yanlış yer: "+ str(yanlisyer))

else:
    print("Lütfen 10 ile 98 arasında basamakları aynı olmayan bir sayı giriniz!")
             
             
    
