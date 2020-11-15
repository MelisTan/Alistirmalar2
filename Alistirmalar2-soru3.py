# Bu fonksiyon 1 den n e kadar olan sayıların çarpımını hesaplar ve geri döndürür.(n!)
def carp(n):
    if n == 1:
        return 1
    else:
        return n*carp(n-1)
