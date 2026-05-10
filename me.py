import random

money = 0
skills = 0
debt = 500000 # Твой стартовый долг за комп
goal = 80000000 # Та самая цель
day = 1

print("--- ДОБРО ПОЖАЛОВАТЬ В СИМУЛЯТОР ЖИЗНИ АВТОРА ---")

while money < goal:
    print(f"\nДень {day}. Баланс: {money} тг. Долг: {debt} тг. Навыки Python: {skills}")
    
    action = input("Что делаем? (1 - Работать курьером, 2 - Учить Python, 3 - Отдыхать): ")
    
    if action == "1":
        # Работа курьером в WB
        earnings = random.randint(5000, 10000)
        money += earnings
        print(f"Ты развез заказы под дождем и заработал {earnings} тг.")
        if debt > 0:
            payment = min(debt, 36000) # Твой платеж
            money -= payment
            debt -= payment
            print(f"Списано {payment} тг в счет долга за ПК.")
            
    elif action == "2":
        # Прокачка навыков
        skills += 10
        print("Ты исправил баг с Bob! Навыки программирования выросли.")
        if skills > 100:
            salary = 500000
            money += salary
            print(f"Ты устроился Junior-разработчиком! Зарплата: {salary} тг.")
            
    elif action == "3":
        print("Ты рубишься в Poppy Playtime. Нога отдыхает, силы восстановились.")
    
    day += 1
    if day > 365 * 9: # Лимит до 25 лет
        print("Тебе исполнилось 25. Пора подводить итоги!")
        break

if money >= goal:
    print("ПОЗДРАВЛЯЮ! Ты купил квартиру в ЖК за 80 лямов!")
else:
    print("До цели еще нужно поработать, но опыт бесценен.")