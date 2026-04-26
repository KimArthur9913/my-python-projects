print("--- COOL CALCULATOR ---")

# Просим ввести числа
a = float (input("Введи первое число: "))
b = float (input("Введи второе число: "))

# Просим выбрать действие 
print("Что делаем? (+, -, *, /)")
operaciya = input("Твой выбор:")
                  
# Логика расчета 
if operaciya == "+":
    rezultat = a + b 
elif operaciya == "-":
    rezultat = a - b
elif operaciya == "*":
    rezultat = a * b
elif operaciya == "/":
    rezultat = a / b
else:
    rezultat = "Ошибка! Нет такого знака."

print("Результат: "+ str(rezultat))
print("-------------------------")


