def calculate_bmi(weight, height):
    """
    Функция для расчета индекса массы тела.

    Args:
      weight: Масса тела в килограммах.
      height: Рост в метрах.

    Returns:
      Значение индекса массы тела.
    """

    bmi = weight / (height ** 2)
    return bmi


while True:
    try:
        weight = float(input("Введите ваш вес в килограммах: "))
        height = float(input("Введите ваш рост в метрах: "))

        if weight <= 0 or height <= 0:
            print("Вес и рост должны быть положительными числами.")
        else:
            bmi = calculate_bmi(weight, height)
            print(f"Ваш индекс массы тела: {bmi:.2f}")

            if bmi < 18.5:
                print("Недостаточный вес")
            elif bmi < 25:
                print("Нормальный вес")
            elif bmi < 30:
                print("Избыточный вес")
            else:
                print("Ожирение")

            break  # Прерываем цикл после корректного ввода
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите числовые значения.")
