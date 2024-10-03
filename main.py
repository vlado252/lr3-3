n = int(input("Введите количество школьников:"))
k = int(input("Введите количество яблок: "))

yabloki = k // n
ostatok = k - yabloki*n


print(yabloki)
print ("По ", yabloki, "каждому школьнику.")
print(ostatok, "яблок останется в корзине.")