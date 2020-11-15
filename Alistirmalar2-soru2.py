# Bu fonksiyon 1 den n e kadar olan sayıların toplamını hersaplar ve geri döndürür.
def toplam(n):

    if n== 1:
        return 1
    else:
        return n + toplam(n-1)

