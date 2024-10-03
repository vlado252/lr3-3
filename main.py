day = int(input("Введи день:"))
month = int(input("Введи номер месяца:"))

if (day>=1 and day <=31 and month==12)or(day>=1 and day <=31 and month==1)or(day>=1 and day <=28 and month==2):
   print("Сезон зима") 
elif(day>=1 and day <=31 and month==3)or(day>=1 and day <=30 and month==4)or(day>=1 and day <=31 and month==5):
   print("Сезон весна") 
elif(day>=1 and day <=30 and month==6)or(day>=1 and day <=31 and month==7)or(day>=1 and day <=31 and month==8) :
   print("Сезон лето") 
elif(day>=1 and day <=30 and month==9)or(day>=1 and day <=31 and month==10)or(day>=1 and day <=30 and month==11) :
   print("Сезон осень") 
else:
   print("Неправильная дата")
