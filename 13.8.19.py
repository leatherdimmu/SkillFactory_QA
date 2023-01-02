tikets = int(input('Введите количество билетов, которые Вы хотите приобрести на мероприятие- '))
prise_1 = 990
prise_2 = 1390
prise_itog = 0
for i in range(tikets): 
  if tikets < 4:
    age = int(input('Введите Ваш возраст- '))
    if age < 18:
      prise_itog = prise_itog + 0
    elif age >= 18 and age <= 25:
      prise_itog = prise_itog + prise_1
    elif age > 25 or age <= 100:
      prise_itog = prise_itog + prise_2
  elif tikets >= 4:
    age = int(input('Введите Ваш возраст- '))
    if age < 18:
      prise_itog = prise_itog + 0
    elif age >= 18 and age <= 25:
      prise_itog = prise_itog + prise_1 * 0.9
    elif age > 25 or age <= 100:
      prise_itog = prise_itog + prise_2 * 0.9
print("Итого к оплате -", prise_itog) 
