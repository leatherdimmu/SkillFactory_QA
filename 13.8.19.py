age = int(input('Введите Ваш возраст- '))
kol_vo_tiket = int(input('Введите количество билетов, которые Вы хотите приобрести на мероприятие- '))
prise_1 = 990
prise_2 = 1390
if kol_vo_tiket < 3:
  if age < 18:
    print('Проходите на конференцию бесплатно')
  elif age >= 18 and age <= 25:
    print("К оплате", prise_1, "рублей")
  elif age > 25 or age <= 100:
    print("К оплате", prise_2, "рублей")
else:
  if age < 18:
    print('Проходите на конференцию бесплатно')
  elif age >= 18 and age <= 25:
    print("К оплате", prise_1 * kol_vo_tiket * 0.9 , "рублей")
  elif age > 25 or age <= 100:
    print("К оплате", prise_2 * kol_vo_tiket * 0.9 , "рублей")