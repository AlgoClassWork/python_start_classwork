surname = 'Иванов'
people_amount = 24
ticket_price = 2450
total = people_amount*ticket_price
print('Экскурсовод -',surname )
print('Стоимость пакета:', total)


adults = 2
children = 31
adult_price = 3699
child_price = 1100
total = adults*adult_price + children*child_price
print('Полная стоимость:', total)



people = 3

luggage = 890
transport = 875
health = 1345
passport = 2199

total = (luggage + transport + health + passport) * people
print('Стоимость страхования семьи:', total)


surname = input('Введите фамилию:')
country = input('Введите страну отдыха:')
season = input('Введите время года:' )
print('Запрос -', surname, country, season, '- отправлен')




name = input('Имя клиента:')
sold = input('Количество купленных путёвок:')
city = input('Предлагаемая путёвка:')
print('Здравствуйте,' , name)
print('Вы путешествовали с нами уже' , sold , 'раз(а)! Хотите снова?')
print('Наша турфирма проводит распродажу. Тур в' , city , 'со скидкой 50%!')
