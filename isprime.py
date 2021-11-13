class isprime:
    def __init__(self, num):
        self.num = num
    def isprime(num):
        divider = 2
        result = int(num) / divider
        if (result == int(result)) and (result != 1):  #Terdapat 2 kondisi untuk mencegah Angka 2 tidak ikut ke sini
            return False
        else:
            while (result != int(result)) and (result != 1):    #Ketika Bilangan ganjil dibagi oleh 2, maka akan menghasilkan sisa bagi. Pengulangan ini akan terus berlangsung jika 'result' tidak sama dengan 'int(result)' dan hasil tidak sama dengan 1.
                result = int(num) / divider
                divider += 1
            if (result == int(result)) and (result == 1):
                return True
            else:
                return False
